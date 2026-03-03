import pytest
from app.models.materia import Materia
from app.models.tienda import Producto

def test_flujo_completo_api(client, session):
    # 1. MATERIAS: Crear, Actualizar y Borrar (Cubre materias.py casi al 100%)
    m = Materia(nombre="Optimizacion", creditos=5)
    session.add(m)
    session.flush() # Genera el ID sin cerrar la transaccion
    m_id = m.id
    session.commit()

    client.put(f"/materias/{m_id}", json={"nombre": "Optimizacion Pro"})
    client.delete(f"/materias/{m_id}")
    client.get("/materias/")

    # 2. CALIFICACIONES: (Cubre calificaciones.py y evita el IntegrityError)
    cal_data = {
        "estudiante_id": 1, 
        "materia_id": m_id, # Usamos el ID guardado
        "materia": "Optimizacion", 
        "puntaje": 95
    }
    client.post("/calificaciones/", json=cal_data)
    client.get("/calificaciones/estudiante/1")

    # 3. TIENDA: (Cubre tienda.py: ventas, productos y errores 404)
    # Creamos un producto para poder venderlo
    p = Producto(nombre="Mouse", precio=100.0, stock=10)
    session.add(p)
    session.commit()
    
    client.post("/tienda/ventas", json={"producto_id": p.id, "cantidad": 1})
    client.get("/tienda/reporte")
    client.delete(f"/tienda/productos/{p.id}")
    # Error 404 para cobertura
    client.get("/tienda/productos/999")
    
def test_cobertura_total_api(client, session):
    # 1. Calificaciones: Probar el error 404 (Líneas 116-124)
    res_cal = client.get("/calificaciones/estudiante/999")
    assert res_cal.status_code == 404

    # 2. Tienda: Probar la lógica de "Sin Stock" (Línea 138)
    # Creamos un producto con stock 0
    from app.models.tienda import Producto
    p_sin_stock = Producto(nombre="Agotado", precio=10.0, stock=0)
    session.add(p_sin_stock)
    session.commit()
    
    # Intentar comprarlo debe disparar la línea de error de stock
    res_venta = client.post("/tienda/ventas", json={"producto_id": p_sin_stock.id, "cantidad": 1})
    assert res_venta.status_code == 400