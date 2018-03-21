-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: naver
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `apt_real_trade_price`
--

DROP TABLE IF EXISTS `apt_real_trade_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apt_real_trade_price` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '거래금액',
  `completion_date` year(4) DEFAULT NULL COMMENT '건축년도\n',
  `year` year(4) DEFAULT NULL,
  `road_address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명',
  `road_main_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명건물본번호코드',
  `road_sub_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명건물부번호코드',
  `road_sigungu_code` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '도로명시군구코드',
  `road_serial_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명일련번호코드',
  `road_under_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명지상지하코드',
  `road_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '도로명코드',
  `law_name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동',
  `law_main_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동본번코드',
  `law_sub_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동부번코드',
  `law_sigungu_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동시군구코드',
  `law_umd_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동읍면동코드',
  `law_jibun_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '법정동지번코드',
  `apt_name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  `day` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `serial_number` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '일련번호',
  `private_area` float DEFAULT NULL COMMENT '전용면적',
  `jibun` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `region_code` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '지역코드',
  `floor` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apt_real_trade_price`
--

LOCK TABLES `apt_real_trade_price` WRITE;
/*!40000 ALTER TABLE `apt_real_trade_price` DISABLE KEYS */;
/*!40000 ALTER TABLE `apt_real_trade_price` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-21 11:33:34
