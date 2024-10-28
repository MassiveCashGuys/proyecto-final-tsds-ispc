

-- 3. INSERT(5):
-- 
INSERT INTO tipo_documento (nombre, descripcion) VALUES
('DNI', 'Documento Nacional de Identidad'),
('LE', 'Libreta de Enrolamiento'),
('LC', 'Libreta Cívica'),
('PASAPORTE', 'Pasaporte'),
('CI', 'Cédula de Identidad');

-- 
INSERT INTO tipo_inversor (nombre, descripcion) VALUES
('CONSERVADOR', 'Inversor que prefiere minimizar riesgos y asegurar su capital'),
('MODERADO', 'Inversor que busca un equilibrio entre riesgo y retorno'),
('AGRESIVO', 'Inversor que busca maximizar el rendimiento, asumiendo mayores riesgos'),
('ESPECULADOR', 'Inversor que busca obtener beneficios a corto plazo con alta volatilidad'),
('INSTITUCIONAL', 'Inversor que representa a una organización y maneja grandes cantidades de capital');

-- 
insert into empresa (id_empresa,nombre,razon_social,descripcion)value(1,"MegaConstructores", "Mega","empresa contructora de avellaneda");

INSERT INTO permiso (
    nombre, 
    descripcion
) VALUES
('Administrador', 'Perfil con acceso total a todas las funcionalidades del sistema.'),
('Trader', 'Perfil para usuarios que realizan operaciones de compra y venta de acciones.'),
('Analista', 'Perfil para usuarios que analizan datos de mercado y generan reportes.'),
('Asistente', 'Perfil con acceso limitado para tareas administrativas.'),
('Invitado', 'Perfil con acceso restringido a funcionalidades básicas.');


INSERT INTO perfil (nombre, descripcion,permiso_id_permiso) VALUES
('ADMIN', 'Permiso de administrador con acceso total',1),
('USER', 'Permiso de usuario regular con acceso limitado',2),
('EDITOR', 'Permiso para editar contenido',3),
('VIEWER', 'Permiso solo para ver contenido',4);

INSERT INTO accion (
    id_accion, 
    simbolo, 
    nombre, 
    cantidad, 
    precio_venta_actual, 
    cantidad_venta_diaria, 
    fecha_apertura, 
    minimo_diario, 
    maximo_diario, 
    ultimo_cierre, 
    id_empresa
) VALUES
(1, 'TSLA', 'Tesla Inc.', 1500, 800.50, 1200, '2024-01-01 09:00:00', 780.00, 820.00, '2024-10-22 17:00:00', '1'),
(2, 'AAPL', 'Apple Inc.', 2000, 150.75, 1800, '2024-01-01 09:00:00', 145.00, 155.00, '2024-10-22 17:00:00', '1'),
(3, 'GOOGL', 'Alphabet Inc.', 1000, 2800.00, 800, '2024-01-01 09:00:00', 2700.00, 2900.00, '2024-10-22 17:00:00', '1'),
(4, 'AMZN', 'Amazon.com Inc.', 1200, 3200.50, 1000, '2024-01-01 09:00:00', 3100.00, 3300.00, '2024-10-22 17:00:00', '1'),
(5, 'MSFT', 'Microsoft Corp.', 1800, 299.75, 1600, '2024-01-01 09:00:00', 290.00, 310.00, '2024-10-22 17:00:00', '1');


INSERT INTO  tipo_transaccion (nombre, descripcion)
VALUES 
('Compra', 'Transacción de compra de productos o servicios'),
('Venta', 'Transacción de venta de productos o servicios'),
('Devolución', 'Transacción de devolución de productos'),
('Transferencia', 'Transacción de transferencia de fondos'),
('Pago', 'Transacción de pago de servicios o productos');
--



INSERT INTO usuario (id_user,password, id_perfil) VALUES ("clau@gmail.com", "colesterol202",1);


UPDATE transaccion 
SET 
    fecha_hora = '2024-10-26 00:00:00', 
    cantidad_acciones = 200, 
    precio = 800.5, 
    comision_broker = 4670 
WHERE 
    id_transaccion = 1;


UPDATE accion 
SET  
    simbolo = 'TSLA',
    nombre = 'Tesla SRL.', 
    cantidad = 1000,
    precio_venta_actual = 800.5, 
    cantidad_venta_diaria = 1200,
    fecha_apertura = '2024-01-01 09:00:00', 
    minimo_diario = 780, 
    maximo_diario = 820, 
    ultimo_cierre = '2024-10-22 17:00:00', 
    id_empresa = '20345678901'
WHERE 
    id_accion = 1;

UPDATE inversor 
SET 
    cuit = '11111111112',
    numero_documento = 11111111,
    nombre = 'Otra',
    apellido = 'prueba',
    id_portafolio = 54, 
    id_tipo_inversor = 9, 
    id_tipo_documento = 26,
    id_usuario = 'aweb@cla.com'
WHERE 
    cuit = '11111111112';


UPDATE tipo_documento 
SET 
    nombre = 'Ci',
    descripcion = 'Cédula de Identidad'
WHERE 
    id_tipo_documento = 27; 

UPDATE perfil 
SET 
    nombre = 'Administrador Total',
    descripcion = 'Perfil con acceso total a todas las funcionalidades del sistema.',
    permiso_id_permiso = 6 
WHERE 
    id_perfil = 1;



-- 5. SELECT(5):
-- Muestra todos los registros de la tabla accion:
SELECT * FROM accion;
-- Muestra todos los registro de la tablas inversores:
SELECT * FROM inversor;
-- Muestra todos los tipos de inversores:
SELECT * FROM tipo_inversor ;
-- Mustra el usuario con email clau@gmail.com que es su id. En la tabla usuario se contienen las contraseñas hasheadas:
SELECT * FROM usuario WHERE id_user = "clau@gmail.com";
-- Muestra el portafolio del usuario, ingresando el nº del portafolio del usuario:
SELECT * FROM portafolio WHERE id_portafolio= 1;







-- 6. CONSULTAS MULTITABLAS(3):
-- Consulta multitabla-Combina y Obtiene datos de las tablas accion y transaccion del usuario con CIUT: 20357856591
SELECT 
    T.id_transaccion,
    T.fecha_hora,
    T.cantidad_acciones,
    T.precio,
    A.id_accion,
    A.simbolo,
    T.tipo_transaccion_id_tipo_transaccion
FROM 
    transaccion T
JOIN 
    accion A ON A.id_accion = T.accion_id_accion
WHERE 
    T.inversor_cuit = '20357856591'; 

-- Consulta multitabla: Obtiene todas las transacciones segun un cuit combinando las tablas transaccion y tipo de transaccion del usuario con CIUT: 20357856591: 
SELECT 
    T.id_transaccion,
    T.fecha_hora,
    T.cantidad_acciones,
    T.precio,                        
    A.id_accion,
    A.simbolo,  
    T.tipo_transaccion_id_tipo_transaccion, 
    TP.nombre                
FROM 
    transaccion T
JOIN 
    accion A ON A.id_accion = T.accion_id_accion
JOIN 
    tipo_transaccion TP ON TP.id_tipo_transaccion = T.tipo_transaccion_id_tipo_transaccion
WHERE 
    T.inversor_cuit = '12306333375'; 

-- Consulta multitabla-Combina y Obtiene datos de las tablas accion y empresa                        
SELECT 
    A.id_accion, 
    A.simbolo, 
    A.nombre, 
    A.cantidad,
    A.precio_venta_actual, 
    A.cantidad_venta_diaria,
    A.fecha_apertura, 
    A.minimo_diario, 
    A.maximo_diario, 
    A.ultimo_cierre, 
    E.id_empresa, 
    E.nombre AS empresa_nombre,  -- Use alias for clarity
    E.razon_social, 
    E.descripcion
FROM 
    accion A
JOIN 
    empresa E ON A.id_empresa = E.id_empresa 
WHERE 
    A.cantidad > 0;