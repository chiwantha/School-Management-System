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
-- Table structure for table `acadamic`
--

DROP TABLE IF EXISTS `acadamic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acadamic` (
  `id` varchar(100) DEFAULT NULL,
  `exam` varchar(4) DEFAULT NULL,
  `batch` varchar(5) DEFAULT NULL,
  `admission` varchar(50) DEFAULT NULL,
  `a` int DEFAULT NULL,
  `b` int DEFAULT NULL,
  `c` int DEFAULT NULL,
  `s` int DEFAULT NULL,
  `w` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acadamic`
--

LOCK TABLES `acadamic` WRITE;
/*!40000 ALTER TABLE `acadamic` DISABLE KEYS */;
INSERT INTO `acadamic` VALUES ('13598','O/L','2020','60677546',4,2,2,1,0),('11304','A/L','2019','5310377',0,0,0,0,3),('11314','A/L','2019','5310385',0,0,0,0,3),('11374','A/L','2019','5310300',0,0,0,1,2),('11375','A/L','2019','5310318',0,0,0,2,1),('11418','A/L','2019','5310326',0,0,0,3,0),('11442','A/L','2019','5310334',0,0,1,1,1),('11456','A/L','2019','5310342',0,0,0,1,2),('12625','O/L','2021','10615679',5,3,0,1,0),('12753','O/L','2021','10615768',2,1,4,2,0),('12823','O/L','2021','10615830',2,3,4,0,0),('12833','O/L','2021','10615849',4,2,3,0,0),('12836','O/L','2021','10615857',4,3,2,0,0),('12644','O/L','2021','10615911',1,1,3,4,0),('12691','O/L','2021','10615970',2,2,3,2,0),('12726','O/L','2021','10616004',3,3,3,0,0),('12845','O/L','2021','10616055',8,1,0,0,0),('12866','O/L','2021','10616063',9,0,0,0,0),('12653','O/L','2021','10615920',3,4,1,1,0),('12648','O/L','2021','10615687',1,1,0,4,3),('12650','O/L','2021','10615695',0,0,2,4,3),('12680','O/L','2021','10615709',0,0,1,6,2),('12703','O/L','2021','10615717',0,0,2,5,2),('12712','O/L','2021','10615725',0,0,2,4,3),('12748','O/L','2021','10615741',0,0,3,4,2),('12752','O/L','2021','10615750',0,1,5,2,1),('12755','O/L','2021','10615776',0,0,0,3,6),('12779','O/L','2021','10615806',0,3,5,1,0),('12822','O/L','2021','10615822',0,1,1,5,2),('11956','A/L','2021','5467179',0,0,0,3,0),('11828','A/L','2021','5467381',0,0,1,1,0),('11896','A/L','2021','5467454',0,0,0,3,0),('11916','A/L','2021','5467500',0,0,0,0,3),('14091','A/L','2021','5467756',0,0,0,0,3),('11834','A/L','2021','5467861',0,0,0,0,3),('11819','A/L','2021','5467993',1,2,0,0,0),('11970','A/L','2021','5468116',0,0,0,0,3),('11777','A/L','2021','5468426',0,0,3,0,0),('11806','A/L','2021','5469074',1,2,0,0,0),('11859','A/L','2021','5469104',0,0,0,0,3),('11892','A/L','2021','5469120',0,0,0,0,3),('11925','A/L','2021','5469155',0,0,0,0,3),('11960','A/L','2021','5469201',0,0,0,0,3),('11849','A/L','2021','5469333',0,0,0,1,2);
/*!40000 ALTER TABLE `acadamic` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-26 10:50:49