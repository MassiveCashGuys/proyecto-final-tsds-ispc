-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema u947306787_IspcPF2024
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema u947306787_IspcPF2024
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `u947306787_IspcPF2024` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
USE `u947306787_IspcPF2024` ;

-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`empresa` (
  `id_empresa` VARCHAR(20) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `razon_social` VARCHAR(85) NULL DEFAULT NULL,
  `descripcion` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id_empresa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`accion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`accion` (
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
  INDEX `fk_accion_empresa` (`id_empresa` ASC) VISIBLE,
  CONSTRAINT `fk_accion_empresa`
    FOREIGN KEY (`id_empresa`)
    REFERENCES `u947306787_IspcPF2024`.`empresa` (`id_empresa`)
    ON DELETE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`portafolio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`portafolio` (
  `id_portafolio` INT(11) NOT NULL AUTO_INCREMENT,
  `saldo_actual` FLOAT NULL DEFAULT NULL,
  `fecha_inicio` DATE NOT NULL,
  PRIMARY KEY (`id_portafolio`))
ENGINE = InnoDB
AUTO_INCREMENT = 84
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`detalle_portafolio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`detalle_portafolio` (
  `id_detalle_portafolio` INT(11) NOT NULL AUTO_INCREMENT,
  `cantidad_acciones_compradas` INT(11) NULL DEFAULT NULL,
  `precio_por_accion` FLOAT NULL DEFAULT NULL,
  `fecha_compra` DATETIME NULL DEFAULT NULL,
  `accion_id_accion` INT(11) NOT NULL,
  `portafolio_id_portafolio` INT(11) NOT NULL,
  PRIMARY KEY (`id_detalle_portafolio`),
  INDEX `fk_detalle_portafolio_accion1_idx` (`accion_id_accion` ASC) VISIBLE,
  INDEX `fk_detalle_portafolio_portafolio1_idx` (`portafolio_id_portafolio` ASC) VISIBLE,
  CONSTRAINT `fk_detalle_portafolio_accion1`
    FOREIGN KEY (`accion_id_accion`)
    REFERENCES `u947306787_IspcPF2024`.`accion` (`id_accion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_detalle_portafolio_portafolio1`
    FOREIGN KEY (`portafolio_id_portafolio`)
    REFERENCES `u947306787_IspcPF2024`.`portafolio` (`id_portafolio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 24
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`tipo_documento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`tipo_documento` (
  `id_tipo_documento` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_documento`))
ENGINE = InnoDB
AUTO_INCREMENT = 28
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`tipo_inversor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`tipo_inversor` (
  `id_tipo_inversor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_inversor`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`permiso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`permiso` (
  `id_permiso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  PRIMARY KEY (`id_permiso`))
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`perfil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`perfil` (
  `id_perfil` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(300) NULL DEFAULT NULL,
  `permiso_id_permiso` INT(11) NOT NULL,
  PRIMARY KEY (`id_perfil`),
  INDEX `fk_perfil_permiso1_idx` (`permiso_id_permiso` ASC) VISIBLE,
  CONSTRAINT `fk_perfil_permiso1`
    FOREIGN KEY (`permiso_id_permiso`)
    REFERENCES `u947306787_IspcPF2024`.`permiso` (`id_permiso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`usuario` (
  `id_user` VARCHAR(100) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `id_perfil` INT(11) NOT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE INDEX `user_UNIQUE` (`id_user` ASC) VISIBLE,
  INDEX `fk_user_perfil1_idx` (`id_perfil` ASC) VISIBLE,
  CONSTRAINT `fk_id_perfil_usuario`
    FOREIGN KEY (`id_perfil`)
    REFERENCES `u947306787_IspcPF2024`.`perfil` (`id_perfil`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`inversor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`inversor` (
  `cuit` VARCHAR(20) NOT NULL,
  `numero_documento` INT(11) NOT NULL,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `id_portafolio` INT(11) NULL DEFAULT NULL,
  `id_tipo_inversor` INT(11) NULL DEFAULT NULL,
  `id_tipo_documento` INT(11) NULL DEFAULT NULL,
  `id_usuario` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`cuit`),
  INDEX `fk_inversor_portafolio1_idx` (`id_portafolio` ASC) VISIBLE,
  INDEX `fk_inversor_tipo_inversor1_idx` (`id_tipo_inversor` ASC) VISIBLE,
  INDEX `fk_inversor_tipo_documento1_idx` (`id_tipo_documento` ASC) VISIBLE,
  INDEX `fk_inversor_user1_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_inversor_portafolio1`
    FOREIGN KEY (`id_portafolio`)
    REFERENCES `u947306787_IspcPF2024`.`portafolio` (`id_portafolio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inversor_tipo_documento1`
    FOREIGN KEY (`id_tipo_documento`)
    REFERENCES `u947306787_IspcPF2024`.`tipo_documento` (`id_tipo_documento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inversor_tipo_inversor1`
    FOREIGN KEY (`id_tipo_inversor`)
    REFERENCES `u947306787_IspcPF2024`.`tipo_inversor` (`id_tipo_inversor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inversor_user1`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `u947306787_IspcPF2024`.`usuario` (`id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`tipo_transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`tipo_transaccion` (
  `id_tipo_transaccion` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`id_tipo_transaccion`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `u947306787_IspcPF2024`.`transaccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `u947306787_IspcPF2024`.`transaccion` (
  `id_transaccion` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha_hora` DATETIME NULL DEFAULT NULL,
  `cantidad_acciones` INT(11) NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  `comision_broker` FLOAT NULL DEFAULT NULL,
  `inversor_cuit` VARCHAR(45) NOT NULL,
  `accion_id_accion` INT(11) NOT NULL,
  `tipo_transaccion_id_tipo_transaccion` INT(11) NOT NULL,
  PRIMARY KEY (`id_transaccion`),
  INDEX `fk_transaccion_inversor1_idx` (`inversor_cuit` ASC) VISIBLE,
  INDEX `fk_transaccion_accion1_idx` (`accion_id_accion` ASC) VISIBLE,
  INDEX `fk_transaccion_tipo_transaccion1_idx` (`tipo_transaccion_id_tipo_transaccion` ASC) VISIBLE,
  CONSTRAINT `fk_transaccion_accion1`
    FOREIGN KEY (`accion_id_accion`)
    REFERENCES `u947306787_IspcPF2024`.`accion` (`id_accion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transaccion_inversor1`
    FOREIGN KEY (`inversor_cuit`)
    REFERENCES `u947306787_IspcPF2024`.`inversor` (`cuit`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transaccion_tipo_transaccion1`
    FOREIGN KEY (`tipo_transaccion_id_tipo_transaccion`)
    REFERENCES `u947306787_IspcPF2024`.`tipo_transaccion` (`id_tipo_transaccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 56
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
