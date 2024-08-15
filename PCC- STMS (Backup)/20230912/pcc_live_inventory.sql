-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: pcc
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `live_inventory`
--

DROP TABLE IF EXISTS `live_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `live_inventory` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `whom` varchar(200) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `book` varchar(100) DEFAULT NULL,
  `item_category` varchar(100) DEFAULT NULL,
  `item_model` varchar(100) DEFAULT NULL,
  `item_diss` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `live_inventory`
--

LOCK TABLES `live_inventory` WRITE;
/*!40000 ALTER TABLE `live_inventory` DISABLE KEYS */;
INSERT INTO `live_inventory` VALUES (1,'2023-01-01','MINISTRY OF EDUCATION',27,'ICT LAB','TABLE','COMPUTER TABLE',''),(2,'2023-01-01','MINISTRY OF EDUCATION',41,'ICT LAB','CHAIR','STUDENT COMPUTER CHAIR',''),(3,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','CUPBOARD','STEEL',''),(4,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','SCANNER','EPSON',''),(5,'2023-01-01','MINISTRY OF EDUCATION',19,'ICT LAB','SOUND DEVICES','SONY HEADSET',''),(6,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','PRINTER','L6XMARK MS310DN',''),(7,'2023-01-01','MINISTRY OF EDUCATION',42,'ICT LAB','UPS','PROLINK 700',''),(8,'2023-01-01','MINISTRY OF EDUCATION',2,'ICT LAB','MULTIMEDIA','BOXLIGHT P5X32N',''),(9,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','BOARD','MAGNETIC BOARD',''),(10,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','FIRE ARM','CARBONDIOXIDE',''),(11,'2023-01-01','MINISTRY OF EDUCATION',1,'ICT LAB','FIRE ARM','WATER',''),(12,'2023-05-10','COMMON INVENTORY BOOK PG.NO.1',1,'ICT LAB','BOARD','WHITE BOARD','');
/*!40000 ALTER TABLE `live_inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-12  8:48:26
