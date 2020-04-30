/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 15.1 		*/
/*  Created On : 30-Abr-2020 05:37:05 p.m. 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0
; 
/* Drop Tables */

DROP TABLE IF EXISTS `Grupo` CASCADE
;

DROP TABLE IF EXISTS `Materia` CASCADE
;

DROP TABLE IF EXISTS `RegistroIngreso` CASCADE
;

DROP TABLE IF EXISTS `Usuario` CASCADE
;

DROP TABLE IF EXISTS `Uweb` CASCADE
;

/* Create Tables */

CREATE TABLE `Grupo`
(
	`id_grupo` DECIMAL(8,0) NOT NULL,
	`nombre` VARCHAR(12) NOT NULL,
	`id_materia` DECIMAL(6,0) NULL,
	CONSTRAINT `PK_Grupo` PRIMARY KEY (`id_grupo` ASC)
)

;

CREATE TABLE `Materia`
(
	`id_materia` DECIMAL(6,0) NOT NULL,
	`nombre` VARCHAR(50) NOT NULL,
	`correo` VARCHAR(40) NOT NULL,
	CONSTRAINT `PK_Materia` PRIMARY KEY (`id_materia` ASC)
)

;

CREATE TABLE `RegistroIngreso`
(
	`id_registro` DECIMAL(10,0) NOT NULL,
	`fecha` DATETIME NOT NULL,
	`ip` VARCHAR(32) NULL,
	`correo` VARCHAR(40) NULL,
	CONSTRAINT `PK_RegistroIngreso` PRIMARY KEY (`id_registro` ASC)
)

;

CREATE TABLE `Usuario`
(
	`correo` VARCHAR(40) NOT NULL,
	`contrasena` VARCHAR(25) NOT NULL,
	`fRegistro` DATETIME NOT NULL,
	CONSTRAINT `PK_Usuario` PRIMARY KEY (`correo` ASC)
)

;

CREATE TABLE `Uweb`
(
	`id_uweb` DECIMAL(6,0) NOT NULL,
	`url` VARCHAR(1000) NOT NULL,
	`id_materia` DECIMAL(6,0) NULL,
	CONSTRAINT `PK_Uweb` PRIMARY KEY (`id_uweb` ASC)
)

;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE `Grupo` 
 ADD INDEX `IXFK_Grupo_Materia` (`id_materia` ASC)
;

ALTER TABLE `Materia` 
 ADD INDEX `IXFK_Materia_Usuario` (`correo` ASC)
;

ALTER TABLE `RegistroIngreso` 
 ADD INDEX `IXFK_RegistroIngreso_Usuario` (`correo` ASC)
;

ALTER TABLE `Uweb` 
 ADD INDEX `IXFK_Uweb_Materia` (`id_materia` ASC)
;

/* Create Foreign Key Constraints */

ALTER TABLE `Grupo` 
 ADD CONSTRAINT `FK_Grupo_Materia`
	FOREIGN KEY (`id_materia`) REFERENCES `Materia` (`id_materia`) ON DELETE Restrict ON UPDATE Restrict
;

ALTER TABLE `Materia` 
 ADD CONSTRAINT `FK_Materia_Usuario`
	FOREIGN KEY (`correo`) REFERENCES `Usuario` (`correo`) ON DELETE Restrict ON UPDATE Restrict
;

ALTER TABLE `RegistroIngreso` 
 ADD CONSTRAINT `FK_RegistroIngreso_Usuario`
	FOREIGN KEY (`correo`) REFERENCES `Usuario` (`correo`) ON DELETE Restrict ON UPDATE Restrict
;

ALTER TABLE `Uweb` 
 ADD CONSTRAINT `FK_Uweb_Materia`
	FOREIGN KEY (`id_materia`) REFERENCES `Materia` (`id_materia`) ON DELETE Restrict ON UPDATE Restrict
;

SET FOREIGN_KEY_CHECKS=1
; 
