-- Tabla empresa
CREATE TABLE IF NOT EXISTS `empresa` (
  `id_empresa` VARCHAR(20) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `razon_social` VARCHAR(85) NULL DEFAULT NULL,
  `descripcion` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id_empresa`)
) ENGINE = InnoDB;



-- Tabla accion
CREATE TABLE IF NOT EXISTS `accion` (
  `id_accion` INT(11) NOT NULL AUTO_INCREMENT,
  `simbolo` VARCHAR(45) NULL DEFAULT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  `precio_venta_actual` FLOAT NULL DEFAULT NULL,
  `cantidad_venta_diaria` INT(11) NULL DEFAULT NULL,
  `fecha_apertura` DATETIME NOT NULL,
  `minimo_diario` FLOAT NULL DEFAULT NULL,
  `maximo_diario` FLOAT NULL DEFAULT NULL,
  `ultimo_cierre` DATETIME NULL DEFAULT NULL,
  `id_empresa` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`id_accion`),
  INDEX `fk_accion_empresa` (`id_empresa`),
  CONSTRAINT `fk_accion_empresa`
    FOREIGN KEY (`id_empresa`)
    REFERENCES `empresa` (`id_empresa`)
    ON DELETE CASCADE
) ENGINE = InnoDB;

-- Tabla portafolio
CREATE TABLE IF NOT EXISTS `portafolio` (
  `id_portafolio` INT(11) NOT NULL AUTO_INCREMENT,
  `saldo_actual` FLOAT NULL DEFAULT NULL,
  `fecha_inicio` DATE NOT NULL,
  PRIMARY KEY (`id_portafolio`)
) ENGINE = InnoDB;

-- Tabla detalle_portafolio
CREATE TABLE IF NOT EXISTS `detalle_portafolio` (
  `id_detalle_portafolio` INT(11) NOT NULL AUTO_INCREMENT,
  `cantidad_acciones_compradas` INT(11) NULL DEFAULT NULL,
  `precio_por_accion` FLOAT NULL DEFAULT NULL,
  `fecha_compra` DATETIME NULL DEFAULT NULL,
  `accion_id_accion` INT(11) NOT NULL,
  `portafolio_id_portafolio` INT(11) NOT NULL,
  PRIMARY KEY (`id_detalle_portafolio`),
  INDEX `fk_detalle_portafolio_accion1_idx` (`accion_id_accion`),
  INDEX `fk_detalle_portafolio_portafolio1_idx` (`portafolio_id_portafolio`),
  CONSTRAINT `fk_detalle_portafolio_accion1`
    FOREIGN KEY (`accion_id_accion`)
    REFERENCES `accion` (`id_accion`),
  CONSTRAINT `fk_detalle_portafolio_portafolio1`
    FOREIGN KEY (`portafolio_id_portafolio`)
    REFERENCES `portafolio` (`id_portafolio`)
) ENGINE = InnoDB;


-- Tabla tipo_inversor
CREATE TABLE IF NOT EXISTS `tipo_inversor` (
  `id_tipo_inversor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_inversor`)
) ENGINE = InnoDB;


-- Tabla tipo_documento
CREATE TABLE IF NOT EXISTS `tipo_documento` (
  `id_tipo_documento` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_documento`)
) ENGINE = InnoDB;



-- Tabla permiso
CREATE TABLE IF NOT EXISTS `permiso` (
  `id_permiso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_permiso`)
) ENGINE = InnoDB;

-- Tabla perfil
CREATE TABLE IF NOT EXISTS `perfil` (
  `id_perfil` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  `permiso_id_permiso` INT(11) NOT NULL,
  PRIMARY KEY (`id_perfil`),
  INDEX `fk_perfil_permiso1_idx` (`permiso_id_permiso`),
  CONSTRAINT `fk_perfil_permiso1`
    FOREIGN KEY (`permiso_id_permiso`)
    REFERENCES `permiso` (`id_permiso`)
) ENGINE = InnoDB;

-- Tabla usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_user` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `id_perfil` INT(11) NOT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `user_UNIQUE` (`id_user`),
  INDEX `fk_user_perfil1_idx` (`id_perfil`),
  CONSTRAINT `fk_id_perfil_usuario`
    FOREIGN KEY (`id_perfil`)
    REFERENCES `perfil` (`id_perfil`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
) ENGINE = InnoDB;

-- Tabla inversor
CREATE TABLE IF NOT EXISTS `inversor` (
  `cuit` VARCHAR(20) NOT NULL,
  `numero_documento` INT(11) NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `id_portafolio` INT(11) NULL DEFAULT NULL,
  `id_tipo_inversor` INT(11) NULL DEFAULT NULL,
  `id_tipo_documento` INT(11) NULL DEFAULT NULL,
  `id_usuario` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`cuit`),
  INDEX `fk_inversor_portafolio1_idx` (`id_portafolio`),
  INDEX `fk_inversor_tipo_inversor1_idx` (`id_tipo_inversor`),
  INDEX `fk_inversor_tipo_documento1_idx` (`id_tipo_documento`),
  INDEX `fk_inversor_usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_inversor_portafolio`
    FOREIGN KEY (`id_portafolio`)
    REFERENCES `portafolio` (`id_portafolio`),
  CONSTRAINT `fk_inversor_tipo_inversor`
    FOREIGN KEY (`id_tipo_inversor`)
    REFERENCES `tipo_inversor` (`id_tipo_inversor`),
  CONSTRAINT `fk_inversor_tipo_documento`
    FOREIGN KEY (`id_tipo_documento`)
    REFERENCES `tipo_documento` (`id_tipo_documento`),
  CONSTRAINT `fk_inversor_usuario`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `usuario` (`id_user`)
) ENGINE = InnoDB;

CREATE TABLE tipo_transaccion (
  id_tipo_transaccion INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  descripcion VARCHAR(200) DEFAULT NULL,
  PRIMARY KEY (id_tipo_transaccion)
);


CREATE TABLE IF NOT EXISTS transaccion (
  id_transaccion INT NOT NULL AUTO_INCREMENT,
  fecha_hora DATETIME DEFAULT NULL,
  cantidad_acciones INT DEFAULT NULL,
  precio FLOAT DEFAULT NULL,
  comision_broker FLOAT DEFAULT NULL,
  inversor_cuit VARCHAR(45) NOT NULL,
  accion_id_accion INT NOT NULL,
  tipo_transaccion_id_tipo_transaccion INT NOT NULL,
  PRIMARY KEY (id_transaccion),
  INDEX fk_transaccion_inversor1_idx (inversor_cuit),
  INDEX fk_transaccion_accion1_idx (accion_id_accion),
  INDEX fk_transaccion_tipo_transaccion1_idx (tipo_transaccion_id_tipo_transaccion),
  CONSTRAINT fk_transaccion_accion1
    FOREIGN KEY (accion_id_accion)
    REFERENCES accion (id_accion),
  CONSTRAINT fk_transaccion_inversor1
    FOREIGN KEY (inversor_cuit)
    REFERENCES inversor (cuit),
  CONSTRAINT fk_transaccion_tipo_transaccion1
    FOREIGN KEY (tipo_transaccion_id_tipo_transaccion)
    REFERENCES tipo_transaccion (id_tipo_transaccion)
) ENGINE=InnoDB;

-- Tabla perfil
CREATE TABLE IF NOT EXISTS `perfil` (
  `id_perfil` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  `permiso_id_permiso` INT(11) NOT NULL,
  PRIMARY KEY (`id_perfil`),
  INDEX `fk_perfil_permiso1_idx` (`permiso_id_permiso`),
  CONSTRAINT `fk_perfil_permiso1`
    FOREIGN KEY (`permiso_id_permiso`)
    REFERENCES `permiso` (`id_permiso`)
) ENGINE = InnoDB;
