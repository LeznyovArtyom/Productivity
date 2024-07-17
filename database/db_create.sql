-- -----------------------------------------------------
-- Schema Productivity
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `Productivity` DEFAULT CHARACTER SET utf8;
USE `Productivity`;


-- -----------------------------------------------------
-- Table `Productivity`.`role`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productivity`.`role` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `Productivity`.`importance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productivity`.`importance` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `Productivity`.`status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productivity`.`status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `Productivity`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productivity`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `login` VARCHAR(30) NULL,
  `password` VARCHAR(50) NULL,
  `image` MEDIUMBLOB NULL,
  `role_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_role_idx` (`role_id` ASC) VISIBLE,
  CONSTRAINT `fk_role`
    FOREIGN KEY (`role_id`)
    REFERENCES `Productivity`.`role` (`id`)
  );


-- -----------------------------------------------------
-- Table `Productivity`.`task`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Productivity`.`task` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` TEXT(1000) NULL,
  `importance_id` INT NOT NULL,
  `status_id` INT NOT NULL,
  `deadline` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_importance_idx` (`importance_id` ASC) VISIBLE,
  INDEX `fk_status_idx` (`status_id` ASC) VISIBLE,
  INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_importance`
    FOREIGN KEY (`importance_id`)
    REFERENCES `Productivity`.`importance` (`id`),
  CONSTRAINT `fk_status`
    FOREIGN KEY (`status_id`)
    REFERENCES `Productivity`.`status` (`id`),
  CONSTRAINT `fk_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Productivity`.`user` (`id`)
  );