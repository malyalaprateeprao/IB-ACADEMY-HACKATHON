-- MySQL dump 10.13  Distrib 8.0.17, for Linux (x86_64)
--
-- Host: localhost    Database: myone
-- ------------------------------------------------------
-- Server version	8.0.17-cluster

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `doctorstable`
--

DROP TABLE IF EXISTS `doctorstable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctorstable` (
  `id` int(11) DEFAULT NULL,
  `doctorid` varchar(10) NOT NULL,
  `doctorname` varchar(30) NOT NULL,
  `qualification` varchar(25) NOT NULL,
  `services` varchar(50) NOT NULL,
  `mfrom` time NOT NULL,
  `mto` time NOT NULL,
  `afrom` time NOT NULL,
  `ato` time NOT NULL,
  `avgtime` time NOT NULL,
  KEY `fk_cat` (`id`),
  CONSTRAINT `doctorstable_ibfk_1` FOREIGN KEY (`id`) REFERENCES `hospitalregister` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctorstable`
--

LOCK TABLES `doctorstable` WRITE;
/*!40000 ALTER TABLE `doctorstable` DISABLE KEYS */;
INSERT INTO `doctorstable` VALUES (21,'12','sss','swa','fever,cough','00:00:00','00:00:00','00:00:00','00:00:00','00:00:00'),(21,'13','prateep','m.b.b.s','fever,cough','09:00:00','12:00:00','13:00:00','16:00:00','00:20:00'),(21,'13','prateep','m.b.b.s','fever,cough','09:00:00','12:00:00','13:00:00','16:00:00','00:20:00'),(21,'13','prateep','m.b.b.s','fever,cough','09:00:00','12:00:00','13:00:00','16:00:00','00:20:00'),(21,'13','prateep','m.b.b.s','fever,cough','09:00:00','12:00:00','13:00:00','16:00:00','00:20:00');
/*!40000 ALTER TABLE `doctorstable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospitalregister`
--

DROP TABLE IF EXISTS `hospitalregister`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospitalregister` (
  `name` varchar(30) NOT NULL,
  `number` bigint(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `services` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospitalregister`
--

LOCK TABLES `hospitalregister` WRITE;
/*!40000 ALTER TABLE `hospitalregister` DISABLE KEYS */;
INSERT INTO `hospitalregister` VALUES ('malyala',95538540,'malyala@gmail.com','fever,cough','ma:mogullapally,di:jayashanker bhupalpally','hanamkonda','Telangana','111111',21),('malyala11',95538540,'malyala@gmail.com','fever,cough','ma:mogullapally,di:jayashanker bhupalpally','hanamkonda','Telangana','111111',22),('malyala11',95538540,'malyala@gmail.com','fever,cough','ma:mogullapally,di:jayashanker bhupalpally','hanamkonda','Telangana','111111',23);
/*!40000 ALTER TABLE `hospitalregister` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userregister`
--

DROP TABLE IF EXISTS `userregister`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userregister` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `city` varchar(30) NOT NULL,
  `state` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `timeslot` time DEFAULT NULL,
  `hospitalid` int(11) DEFAULT NULL,
  `doctorid` int(11) DEFAULT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userregister`
--

LOCK TABLES `userregister` WRITE;
/*!40000 ALTER TABLE `userregister` DISABLE KEYS */;
INSERT INTO `userregister` VALUES (1,'malyala prateep rao','prateepraomalyala@gmail.com','hanamkonda','Telangana','1111','10:20:00',21,13),(4,'gandhi','gandhi@gmail.com','hyd','Telangana','12345',NULL,NULL,NULL);
/*!40000 ALTER TABLE `userregister` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-17  1:23:50
