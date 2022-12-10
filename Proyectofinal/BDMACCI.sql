CREATE DATABASE `db_macci` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE 'db_macci'
CREATE TABLE `referencias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Ref` varchar(45) NOT NULL,
  `Titulo` varchar(255) NOT NULL,
  `Autor` varchar(255) DEFAULT NULL,
  `Ubicacion` varchar(255) NOT NULL,
  `Tipo` varchar(255) NOT NULL,
  `compatibilidad` int NOT NULL,
  `observ` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

