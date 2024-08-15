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
-- Table structure for table `mark_uo`
--

DROP TABLE IF EXISTS `mark_uo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mark_uo` (
  `exam_id` int NOT NULL AUTO_INCREMENT,
  `sinhala` int DEFAULT NULL,
  `maths` int DEFAULT NULL,
  `science` int DEFAULT NULL,
  `english` int DEFAULT NULL,
  `religion` int DEFAULT NULL,
  `history` int DEFAULT NULL,
  `geograpy` int DEFAULT NULL,
  `ce` int DEFAULT NULL,
  `health` int DEFAULT NULL,
  `art` varchar(5) DEFAULT NULL,
  `dance` varchar(5) DEFAULT NULL,
  `music` varchar(5) DEFAULT NULL,
  `drama` varchar(5) DEFAULT NULL,
  `tamil` int DEFAULT NULL,
  `pts` int DEFAULT NULL,
  `ict` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mark_uo`
--

LOCK TABLES `mark_uo` WRITE;
/*!40000 ALTER TABLE `mark_uo` DISABLE KEYS */;
INSERT INTO `mark_uo` VALUES (1,56,89,54,78,89,56,89,52,89,'12','#','#','#',52,45,'69'),(2,95,93,86,93,96,84,80,78,60,'#','#','85','#',98,95,'#'),(3,89,92,93,96,94,51,87,69,61,'#','#','83','#',90,85,'#'),(4,52,83,45,63,0,26,59,43,60,'#','44','#','#',0,87,'0'),(5,74,66,80,95,96,68,87,82,68,'62','#','#','#',98,88,'#'),(6,79,55,83,90,85,62,84,80,76,'#','#','83','#',89,95,'#'),(7,74,82,73,91,62,67,86,78,57,'64','#','#','#',97,85,'#'),(8,84,81,80,82,94,72,79,82,72,'#','#','74','#',95,97,'#'),(9,57,88,63,80,72,31,58,48,40,'#','#','73','#',78,85,'#'),(10,66,84,56,61,80,47,74,69,55,'#','62','#','#',41,84,'#'),(11,81,88,78,70,100,57,77,66,58,'70','#','#','#',92,88,'#'),(12,86,97,91,72,92,62,63,85,78,'56','#','#','#',94,85,'#'),(13,65,13,39,92,64,40,50,46,29,'#','#','54','#',58,85,'#'),(14,84,89,70,78,56,86,82,71,52,'#','#','65','#',42,87,'#'),(15,76,61,68,63,81,59,79,69,47,'#','#','74','#',95,85,'#'),(16,67,42,19,76,46,38,60,56,10,'55','#','#','#',21,82,'#'),(17,83,84,89,73,90,71,73,71,73,'#','#','85','#',80,84,'#'),(18,87,86,76,86,94,64,87,83,70,'#','#','72','#',92,85,'#'),(19,76,71,69,58,72,52,82,74,67,'61','#','#','#',59,85,'#'),(20,73,68,52,93,92,76,78,76,74,'#','#','71','#',80,97,'#'),(21,79,87,75,49,70,33,75,51,56,'46','#','#','#',66,85,'#'),(22,72,82,54,64,81,29,62,53,42,'63','#','#','#',34,92,'#'),(23,71,91,78,98,90,75,88,78,41,'#','#','93','#',97,92,'#'),(24,65,57,24,94,65,40,61,60,23,'#','62','#','#',79,87,'#'),(25,62,45,73,51,86,61,73,74,56,'#','68','#','#',95,82,'#'),(26,76,83,48,85,59,47,52,67,22,'62','#','#','#',65,85,'#'),(27,65,68,65,66,96,43,66,61,48,'#','70','#','#',65,95,'#'),(28,79,49,28,79,36,70,75,68,20,'#','66','#','#',82,85,'#'),(29,93,56,36,85,98,64,82,80,35,'#','80','#','#',96,87,'#'),(30,63,66,70,46,78,62,61,68,65,'#','56','#','#',89,90,'#'),(31,64,62,45,90,58,24,61,65,54,'#','44','#','#',60,90,'#'),(32,74,64,91,45,76,48,76,64,55,'#','94','#','#',65,87,'#'),(33,65,43,29,51,68,38,46,56,36,'#','50','#','#',17,87,'#'),(34,85,95,85,97,91,92,90,100,78,'#','94','#','#',97,90,'#'),(35,80,21,35,74,96,41,93,71,27,'#','68','#','#',63,90,'#'),(36,79,84,52,73,74,44,79,71,83,'#','74','#','#',99,90,'#'),(37,61,82,38,81,76,39,61,50,32,'#','74','#','#',95,88,'#'),(38,80,86,79,67,90,72,95,80,64,'#','68','#','#',70,82,'#'),(39,83,68,46,94,98,48,86,87,50,'66','#','#','#',86,85,'#'),(40,41,6,29,47,46,16,43,36,16,'#','#','72','#',18,85,'#'),(41,76,55,32,82,77,76,81,72,19,'#','78','#','#',93,95,'#');
/*!40000 ALTER TABLE `mark_uo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-12  8:48:27
