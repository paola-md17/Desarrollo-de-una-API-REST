--
-- PostgreSQL database dump
--

\restrict peMKH7Pf9wJN9JYPI8Tfa4F7Y9doCnYMisCBxo4dwEWFYkdyBznPr0maXWUzAvu

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

-- Started on 2026-02-28 01:44:11

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 222 (class 1259 OID 16489)
-- Name: calificaciones; Type: TABLE; Schema: public; Owner: flask_paus
--

CREATE TABLE public.calificaciones (
    id integer NOT NULL,
    materia character varying(100) NOT NULL,
    puntaje double precision NOT NULL,
    fecha_evaluacion timestamp without time zone,
    estudiante_id integer NOT NULL
);


ALTER TABLE public.calificaciones OWNER TO flask_paus;

--
-- TOC entry 221 (class 1259 OID 16488)
-- Name: calificaciones_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_paus
--

CREATE SEQUENCE public.calificaciones_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.calificaciones_id_seq OWNER TO flask_paus;

--
-- TOC entry 5061 (class 0 OID 0)
-- Dependencies: 221
-- Name: calificaciones_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_paus
--

ALTER SEQUENCE public.calificaciones_id_seq OWNED BY public.calificaciones.id;


--
-- TOC entry 220 (class 1259 OID 16472)
-- Name: estudiantes; Type: TABLE; Schema: public; Owner: flask_paus
--

CREATE TABLE public.estudiantes (
    id integer NOT NULL,
    matricula character varying(10) NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100) NOT NULL,
    email character varying(120) NOT NULL,
    carrera character varying(100) NOT NULL,
    semestre integer,
    fecha_registro timestamp without time zone
);


ALTER TABLE public.estudiantes OWNER TO flask_paus;

--
-- TOC entry 219 (class 1259 OID 16471)
-- Name: estudiantes_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_paus
--

CREATE SEQUENCE public.estudiantes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.estudiantes_id_seq OWNER TO flask_paus;

--
-- TOC entry 5062 (class 0 OID 0)
-- Dependencies: 219
-- Name: estudiantes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_paus
--

ALTER SEQUENCE public.estudiantes_id_seq OWNED BY public.estudiantes.id;


--
-- TOC entry 224 (class 1259 OID 16505)
-- Name: materias; Type: TABLE; Schema: public; Owner: flask_paus
--

CREATE TABLE public.materias (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    creditos integer
);


ALTER TABLE public.materias OWNER TO flask_paus;

--
-- TOC entry 223 (class 1259 OID 16504)
-- Name: materias_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_paus
--

CREATE SEQUENCE public.materias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.materias_id_seq OWNER TO flask_paus;

--
-- TOC entry 5063 (class 0 OID 0)
-- Dependencies: 223
-- Name: materias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_paus
--

ALTER SEQUENCE public.materias_id_seq OWNED BY public.materias.id;


--
-- TOC entry 226 (class 1259 OID 16516)
-- Name: productos; Type: TABLE; Schema: public; Owner: flask_paus
--

CREATE TABLE public.productos (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    precio double precision NOT NULL,
    stock integer
);


ALTER TABLE public.productos OWNER TO flask_paus;

--
-- TOC entry 225 (class 1259 OID 16515)
-- Name: productos_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_paus
--

CREATE SEQUENCE public.productos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.productos_id_seq OWNER TO flask_paus;

--
-- TOC entry 5064 (class 0 OID 0)
-- Dependencies: 225
-- Name: productos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_paus
--

ALTER SEQUENCE public.productos_id_seq OWNED BY public.productos.id;


--
-- TOC entry 228 (class 1259 OID 16526)
-- Name: ventas; Type: TABLE; Schema: public; Owner: flask_paus
--

CREATE TABLE public.ventas (
    id integer NOT NULL,
    producto_id integer,
    cantidad integer NOT NULL,
    total double precision
);


ALTER TABLE public.ventas OWNER TO flask_paus;

--
-- TOC entry 227 (class 1259 OID 16525)
-- Name: ventas_id_seq; Type: SEQUENCE; Schema: public; Owner: flask_paus
--

CREATE SEQUENCE public.ventas_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ventas_id_seq OWNER TO flask_paus;

--
-- TOC entry 5065 (class 0 OID 0)
-- Dependencies: 227
-- Name: ventas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: flask_paus
--

ALTER SEQUENCE public.ventas_id_seq OWNED BY public.ventas.id;


--
-- TOC entry 4877 (class 2604 OID 16492)
-- Name: calificaciones id; Type: DEFAULT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.calificaciones ALTER COLUMN id SET DEFAULT nextval('public.calificaciones_id_seq'::regclass);


--
-- TOC entry 4876 (class 2604 OID 16475)
-- Name: estudiantes id; Type: DEFAULT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.estudiantes ALTER COLUMN id SET DEFAULT nextval('public.estudiantes_id_seq'::regclass);


--
-- TOC entry 4878 (class 2604 OID 16508)
-- Name: materias id; Type: DEFAULT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.materias ALTER COLUMN id SET DEFAULT nextval('public.materias_id_seq'::regclass);


--
-- TOC entry 4879 (class 2604 OID 16519)
-- Name: productos id; Type: DEFAULT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.productos ALTER COLUMN id SET DEFAULT nextval('public.productos_id_seq'::regclass);


--
-- TOC entry 4880 (class 2604 OID 16529)
-- Name: ventas id; Type: DEFAULT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.ventas ALTER COLUMN id SET DEFAULT nextval('public.ventas_id_seq'::regclass);


--
-- TOC entry 5049 (class 0 OID 16489)
-- Dependencies: 222
-- Data for Name: calificaciones; Type: TABLE DATA; Schema: public; Owner: flask_paus
--

COPY public.calificaciones (id, materia, puntaje, fecha_evaluacion, estudiante_id) FROM stdin;
1	Desarrollo Web	10	2026-02-28 02:50:00.77021	1
2	Metodologías Ágiles	8	2026-02-28 02:50:33.069613	3
3	Programación Python	10	2026-02-28 02:50:43.637792	4
4	Inglés Técnico	9	2026-02-28 02:50:51.323171	1
5	Inglés Técnico	9.9	2026-02-28 02:51:00.677934	2
6	Bases de Datos	9.5	2026-02-28 02:51:10.46851	4
7	Bases de Datos	9.5	2026-02-28 02:51:14.913646	1
\.


--
-- TOC entry 5047 (class 0 OID 16472)
-- Dependencies: 220
-- Data for Name: estudiantes; Type: TABLE DATA; Schema: public; Owner: flask_paus
--

COPY public.estudiantes (id, matricula, nombre, apellido, email, carrera, semestre, fecha_registro) FROM stdin;
2	202602	Luis	Ramírez	luis.ramirez@utng.edu.mx	Redes y Ciberseguridad	1	2026-02-28 02:35:23.800957
3	202603	María	Fernández	maria.fer@utng.edu.mx	Diseño Digital	1	2026-02-28 02:35:33.328659
4	202604	Carlos	Ortiz	c.ortiz@utng.edu.mx	Desarrollo de Software	1	2026-02-28 02:35:41.424208
5	202605	Ana	Jasso	ana.jasso@utng.edu.mx	Negocios e Innovación	1	2026-02-28 02:35:58.875784
6	202606	Diego	Torres	diego.t@utng.edu.mx	Sistemas Automotrices	1	2026-02-28 02:36:07.968139
1	202601	Paola	Moya	paum.estudiante@utng.edu.mx	Ingeniería en Ciberseguridad	1	2026-02-28 02:26:13.493566
\.


--
-- TOC entry 5051 (class 0 OID 16505)
-- Dependencies: 224
-- Data for Name: materias; Type: TABLE DATA; Schema: public; Owner: flask_paus
--

COPY public.materias (id, nombre, creditos) FROM stdin;
1	Base de Datos	8
2	Programación Python	10
3	Desarrollo Web	7
\.


--
-- TOC entry 5053 (class 0 OID 16516)
-- Dependencies: 226
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: flask_paus
--

COPY public.productos (id, nombre, precio, stock) FROM stdin;
1	Sudadera UTNG Gris	480.5	18
2	Kit Reglas y Compás Pro	150	40
3	USB 64GB Kingston	220	25
4	Termo UTNG 500ml	350	14
5	Calculadora Casio FX	890	1
\.


--
-- TOC entry 5055 (class 0 OID 16526)
-- Dependencies: 228
-- Data for Name: ventas; Type: TABLE DATA; Schema: public; Owner: flask_paus
--

COPY public.ventas (id, producto_id, cantidad, total) FROM stdin;
1	1	2	961
2	2	10	1500
3	3	5	1100
4	4	1	350
5	5	9	8010
\.


--
-- TOC entry 5066 (class 0 OID 0)
-- Dependencies: 221
-- Name: calificaciones_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_paus
--

SELECT pg_catalog.setval('public.calificaciones_id_seq', 7, true);


--
-- TOC entry 5067 (class 0 OID 0)
-- Dependencies: 219
-- Name: estudiantes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_paus
--

SELECT pg_catalog.setval('public.estudiantes_id_seq', 6, true);


--
-- TOC entry 5068 (class 0 OID 0)
-- Dependencies: 223
-- Name: materias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_paus
--

SELECT pg_catalog.setval('public.materias_id_seq', 3, true);


--
-- TOC entry 5069 (class 0 OID 0)
-- Dependencies: 225
-- Name: productos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_paus
--

SELECT pg_catalog.setval('public.productos_id_seq', 5, true);


--
-- TOC entry 5070 (class 0 OID 0)
-- Dependencies: 227
-- Name: ventas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: flask_paus
--

SELECT pg_catalog.setval('public.ventas_id_seq', 5, true);


--
-- TOC entry 4888 (class 2606 OID 16498)
-- Name: calificaciones calificaciones_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.calificaciones
    ADD CONSTRAINT calificaciones_pkey PRIMARY KEY (id);


--
-- TOC entry 4882 (class 2606 OID 16487)
-- Name: estudiantes estudiantes_email_key; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_email_key UNIQUE (email);


--
-- TOC entry 4884 (class 2606 OID 16485)
-- Name: estudiantes estudiantes_matricula_key; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_matricula_key UNIQUE (matricula);


--
-- TOC entry 4886 (class 2606 OID 16483)
-- Name: estudiantes estudiantes_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.estudiantes
    ADD CONSTRAINT estudiantes_pkey PRIMARY KEY (id);


--
-- TOC entry 4890 (class 2606 OID 16514)
-- Name: materias materias_nombre_key; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.materias
    ADD CONSTRAINT materias_nombre_key UNIQUE (nombre);


--
-- TOC entry 4892 (class 2606 OID 16512)
-- Name: materias materias_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.materias
    ADD CONSTRAINT materias_pkey PRIMARY KEY (id);


--
-- TOC entry 4894 (class 2606 OID 16524)
-- Name: productos productos_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT productos_pkey PRIMARY KEY (id);


--
-- TOC entry 4896 (class 2606 OID 16533)
-- Name: ventas ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_pkey PRIMARY KEY (id);


--
-- TOC entry 4897 (class 2606 OID 16499)
-- Name: calificaciones calificaciones_estudiante_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.calificaciones
    ADD CONSTRAINT calificaciones_estudiante_id_fkey FOREIGN KEY (estudiante_id) REFERENCES public.estudiantes(id);


--
-- TOC entry 4898 (class 2606 OID 16534)
-- Name: ventas ventas_producto_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: flask_paus
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT ventas_producto_id_fkey FOREIGN KEY (producto_id) REFERENCES public.productos(id);


-- Completed on 2026-02-28 01:44:11

--
-- PostgreSQL database dump complete
--

\unrestrict peMKH7Pf9wJN9JYPI8Tfa4F7Y9doCnYMisCBxo4dwEWFYkdyBznPr0maXWUzAvu

