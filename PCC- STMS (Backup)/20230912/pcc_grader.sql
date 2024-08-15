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
-- Table structure for table `grader`
--

DROP TABLE IF EXISTS `grader`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grader` (
  `nic` varchar(50) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `class_group` varchar(50) DEFAULT NULL,
  `class` varchar(50) DEFAULT NULL,
  `pass` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grader`
--

LOCK TABLES `grader` WRITE;
/*!40000 ALTER TABLE `grader` DISABLE KEYS */;
INSERT INTO `grader` VALUES ('707830085V','P.A.D.P. Thilakarathana','Secondary','9B','1234'),('847700114V','B.A.S. Nayomi','Secondary','6C','277288'),('831131942V','A.M.U. Athukorala','Secondary','8A','002016'),('856353699V','M.A.J.R. Madurapperuma','Under O/L','11F','027231'),('666952294V','E.A.W. Edirisingha','Secondary','9F','144980'),('727221204V','K.G.M.P. Kariyawasam','Secondary','6A','074346'),('746471203V','M.I. Perera','Secondary','6B','244872'),('866222080V','J.M.C. Jayasingha','Secondary','6D','312499'),('946030945V','H.M. Balasooriya','Secondary','6A','421699'),('755551694V','W.A.D.S. Wijesooriya','Secondary','7A','116376'),('945450746V','R.S.D. Samarathunga','Secondary','7B','820706'),('652610080V','U.A.E. Gunasekara','Secondary','7C','401089'),('728312882V','S.W.W.M.R.A.W.A. Senarath','Secondary','7D','693140'),('825511580V','R.A.P.T. Ranathunaga','Secondary','7E','244872'),('197982503212','S.A.S. Sobhanie','Secondary','7F','981871'),('686801098V','K.A. Renuka','Secondary','8C','496125'),('668481426V','A.D.M. Priyangika','Secondary','8D','966729'),('915201458V','M.D.S.J. Kumarasingha','Secondary','8E','793459'),('876403382V','W.V.P.T. Nadeeshani','Secondary','8F','956612'),('810621575V','W.A.S.P. Jayathilaka','Secondary','9A','967250'),('815261968V','S.A.P.I. Piyasena','Secondary','9C','127677'),('196481901197','H.H.K.M. Hewawasam','Secondary','9D','703017'),('827852040V','H.M.H.S. Ranaweera','Secondary','9E','014247'),('800500400V','G.K.R.N. Gannoruwa','Under O/L','10A','135465'),('736500370V','G.L.G. Jayawardhana','Under O/L','10B','820420'),('698050659V','K.A.K. Maduranganie','Under O/L','10C','546325'),('756870505V','K.K.P. Menaka','Under O/L','10D','968098'),('197873402230','E.A.R. Kumudunie','Under O/L','10E','639613'),('846692096V','I.D. Kalansooriya','Under O/L','10F','028809'),('870930151V','M.C.D. Kumara','Under O/L','11A','382875'),('796370645V','N.R. Rathnayaka','Under O/L','11B','067816'),('698242744V','W.W.M. Weerasingha','Under O/L','11C','722542'),('817462464V','K.A.C. Nadeeshani','Under O/L','11D','606672'),('756161717V','R.C.K. Arachchige','Under O/L','11E','615413'),('778172046V','B.K.C.N. Bandula','Under A/L','12artA','097430'),('848660930V','U.A.D.L. Udagearachchi','Under A/L','12artB','082861'),('756020986V','D. Gunarathna','Under A/L','12commerceA','989443'),('665782905V','S.A.S. Kalyani','Under A/L','12commerceB','548990'),('725041675V','T.M.N.D.P. Thennakoon','Under A/L','12scienceA','930832'),('685770300V','E.A.P. Ranjanie','Under A/L','13artA','842656'),('901330220V','B. Wimalasara','Under A/L','13artB','077746'),('748100237V','Y.M.N. Wijerathna','Under A/L','13commerceA','192912'),('806613673V','H.M.C. Herath','Under A/L','13commerceB','533936'),('767751079V','H.A.T. Jayasekara','Under A/L','13scienceA','825478'),('198955901378','M.M.G.K. Mapa','13 Years','13 year A','051672'),('887423377V','D.S. Uggalbada','13 Years','13 year B','720682');
/*!40000 ALTER TABLE `grader` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-12  8:48:28
