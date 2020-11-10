-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: iot_reto
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `heart_meditions`
--

DROP TABLE IF EXISTS `heart_meditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `heart_meditions` (
  `heartbeat_rate` float DEFAULT NULL,
  `rate_date` date DEFAULT NULL,
  `hour` time DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `id_person` int DEFAULT NULL,
  `id_heart` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_heart`),
  KEY `id_person` (`id_person`),
  CONSTRAINT `heart_meditions_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `persons` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `heart_meditions`
--

LOCK TABLES `heart_meditions` WRITE;
/*!40000 ALTER TABLE `heart_meditions` DISABLE KEYS */;
INSERT INTO `heart_meditions` VALUES (150,'2020-10-15','08:00:00','ya colgo los tenis',1,1),(150,'2020-10-15','08:00:00','ya colgo los tenis',1,2),(12,'2020-10-15','12:01:12','anemia',1,3);
/*!40000 ALTER TABLE `heart_meditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oxygen_meditions`
--

DROP TABLE IF EXISTS `oxygen_meditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `oxygen_meditions` (
  `oxygen_blood` float DEFAULT NULL,
  `rate_date` date DEFAULT NULL,
  `hour` time DEFAULT NULL,
  `id_person` int DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `oxygen_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`oxygen_id`),
  KEY `id_person` (`id_person`),
  CONSTRAINT `oxygen_meditions_ibfk_1` FOREIGN KEY (`id_person`) REFERENCES `persons` (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oxygen_meditions`
--

LOCK TABLES `oxygen_meditions` WRITE;
/*!40000 ALTER TABLE `oxygen_meditions` DISABLE KEYS */;
INSERT INTO `oxygen_meditions` VALUES (12,'2020-10-15','12:01:12',1,'anemia',1);
/*!40000 ALTER TABLE `oxygen_meditions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persons`
--

DROP TABLE IF EXISTS `persons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persons` (
  `name` varchar(30) DEFAULT NULL,
  `id_person` int NOT NULL AUTO_INCREMENT,
  `birth_date` date DEFAULT NULL,
  `complexion` int DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id_person`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persons`
--

LOCK TABLES `persons` WRITE;
/*!40000 ALTER TABLE `persons` DISABLE KEYS */;
INSERT INTO `persons` VALUES ('emilia',1,'2020-10-15',1,'antunez');
/*!40000 ALTER TABLE `persons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-10 11:28:32
