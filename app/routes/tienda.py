from flask import Blueprint, request, jsonify
from app import db
from ..models.tienda import Producto, Venta

tienda_bp = Blueprint('tienda', __name__, url_prefix='/tienda')

@tienda_bp.route('/productos', methods=['POST'])
def crear_producto():
    """
    Agregar un nuevo producto al inventario
    ---
    tags:
      - Tienda Online
        - Productos 
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            nombre: {type: string, example: "Monitor 4K"}
            precio: {type: number, example: 7500.0}
            stock: {type: integer, example: 15}
    responses:
      201:
        description: Producto creado
    """
    datos = request.get_json()
    nuevo = Producto(nombre=datos['nombre'], precio=datos['precio'], stock=datos['stock'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Producto registrado"}), 201


# --- LISTAR TODOS LOS PRODUCTOS (GET) ---
@tienda_bp.route('/productos', methods=['GET'])
def listar_productos():
    """
    Ver el catálogo completo de la tienda
    ---
    tags:
      - Tienda Online
        - Productos 

    responses:
      200:
        description: Lista de productos obtenida
    """
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos]), 200

# --- ACTUALIZAR PRECIO O STOCK (PUT) ---
@tienda_bp.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    """
    Modificar precio o existencias de un producto
    ---
    tags:
      - Tienda Online    
        - Productos 

    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        schema:
          properties:
            precio: {type: number}
            stock: {type: integer}
    responses:
      200:
        description: Producto actualizado
    """
    producto = Producto.query.get_or_404(id)
    datos = request.get_json()
    
    producto.precio = datos.get('precio', producto.precio)
    producto.stock = datos.get('stock', producto.stock)
    
    db.session.commit()
    return jsonify({"mensaje": "Datos actualizados", "producto": producto.to_dict()}), 200

# --- ELIMINAR PRODUCTO (DELETE) ---
@tienda_bp.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    """
    Quitar un producto del catálogo
    ---
    tags:
      - Tienda Online 
        - Productos 
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Producto eliminado
    """
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"mensaje": f"Producto {id} eliminado correctamente"}), 200


@tienda_bp.route('/ventas', methods=['POST'])
def realizar_venta():
    """
    Realizar una venta (Valida stock y descuenta automáticamente)
    ---
    tags:
      - Tienda Online
        - Ventas 
    parameters:
      - name: body
        in: body
        required: true
        schema:
          properties:
            producto_id: {type: integer, example: 1}
            cantidad: {type: integer, example: 3}
    responses:
      201:
        description: Venta exitosa
      400:
        description: Stock insuficiente
    """
    datos = request.get_json()
    producto = Producto.query.get_or_404(datos['producto_id'])
    cantidad_compra = datos['cantidad']

    # Lógica de Validación de Stock
    if producto.stock < cantidad_compra:
        return jsonify({"error": f"Invalido. Solo hay {producto.stock} piezas"}), 400

    # Lógica de Negocio: Calcular y Descontar
    monto_total = producto.precio * cantidad_compra
    producto.stock -= cantidad_compra 
    
    nueva_venta = Venta(producto_id=producto.id, cantidad=cantidad_compra, total=monto_total)
    db.session.add(nueva_venta)
    db.session.commit()

    return jsonify({"mensaje": "Venta exitosa", "total": monto_total, "quedan": producto.stock}), 201

# --- LISTAR TODAS LAS VENTAS (GET) ---
@tienda_bp.route('/ventas', methods=['GET'])
def listar_ventas():
    """
    Ver el historial completo de ventas realizadas
    ---
    tags:
      - Tienda Online
        - Ventas 
    responses:
      200:
        description: Historial de ventas obtenido
    """
    ventas = Venta.query.all()
    return jsonify([v.to_dict() for v in ventas]), 200

# --- REPORTE DE INGRESOS TOTALES (GET) ---
@tienda_bp.route('/reporte', methods=['GET'])
def reporte_ingresos():
    """
    Calcular el total de dinero recaudado por todas las ventas
    ---
    tags:
      - Tienda Online
        - Ventas
    responses:
      200:
        description: Total de ingresos calculado
    """
    total_recaudado = db.session.query(db.func.sum(Venta.total)).scalar() or 0.0
    total_productos_vendidos = db.session.query(db.func.sum(Venta.cantidad)).scalar() or 0
    
    return jsonify({
        "ingresos_totales": total_recaudado,
        "productos_vendidos_total": total_productos_vendidos,
        "mensaje": f"Has ganado un total de ${total_recaudado} pesos"
    }), 200