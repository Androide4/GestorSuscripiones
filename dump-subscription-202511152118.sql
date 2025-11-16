/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.0.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: subscription
-- ------------------------------------------------------
-- Server version	12.0.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add Moneda',7,'add_moneda'),
(26,'Can change Moneda',7,'change_moneda'),
(27,'Can delete Moneda',7,'delete_moneda'),
(28,'Can view Moneda',7,'view_moneda'),
(29,'Can add Proveedor',8,'add_proveedor'),
(30,'Can change Proveedor',8,'change_proveedor'),
(31,'Can delete Proveedor',8,'delete_proveedor'),
(32,'Can view Proveedor',8,'view_proveedor'),
(33,'Can add Método de pago',9,'add_metodopago'),
(34,'Can change Método de pago',9,'change_metodopago'),
(35,'Can delete Método de pago',9,'delete_metodopago'),
(36,'Can view Método de pago',9,'view_metodopago'),
(37,'Can add Plan',10,'add_plan'),
(38,'Can change Plan',10,'change_plan'),
(39,'Can delete Plan',10,'delete_plan'),
(40,'Can view Plan',10,'view_plan'),
(41,'Can add Suscripción',11,'add_suscripcion'),
(42,'Can change Suscripción',11,'change_suscripcion'),
(43,'Can delete Suscripción',11,'delete_suscripcion'),
(44,'Can view Suscripción',11,'view_suscripcion'),
(45,'Can add Pago',12,'add_pago'),
(46,'Can change Pago',12,'change_pago'),
(47,'Can delete Pago',12,'delete_pago'),
(48,'Can view Pago',12,'view_pago'),
(49,'Can add Notificación',13,'add_notificacion'),
(50,'Can change Notificación',13,'change_notificacion'),
(51,'Can delete Notificación',13,'delete_notificacion'),
(52,'Can view Notificación',13,'view_notificacion'),
(53,'Can add Comentario',14,'add_comentario'),
(54,'Can change Comentario',14,'change_comentario'),
(55,'Can delete Comentario',14,'delete_comentario'),
(56,'Can view Comentario',14,'view_comentario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(14,'suscripciones','comentario'),
(9,'suscripciones','metodopago'),
(7,'suscripciones','moneda'),
(13,'suscripciones','notificacion'),
(12,'suscripciones','pago'),
(10,'suscripciones','plan'),
(8,'suscripciones','proveedor'),
(11,'suscripciones','suscripcion');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
set autocommit=0;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-11-16 01:20:16.662225'),
(2,'auth','0001_initial','2025-11-16 01:20:16.937785'),
(3,'admin','0001_initial','2025-11-16 01:20:16.999085'),
(4,'admin','0002_logentry_remove_auto_add','2025-11-16 01:20:17.009410'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-11-16 01:20:17.017554'),
(6,'contenttypes','0002_remove_content_type_name','2025-11-16 01:20:17.074316'),
(7,'auth','0002_alter_permission_name_max_length','2025-11-16 01:20:17.105691'),
(8,'auth','0003_alter_user_email_max_length','2025-11-16 01:20:17.132425'),
(9,'auth','0004_alter_user_username_opts','2025-11-16 01:20:17.141914'),
(10,'auth','0005_alter_user_last_login_null','2025-11-16 01:20:17.169368'),
(11,'auth','0006_require_contenttypes_0002','2025-11-16 01:20:17.170943'),
(12,'auth','0007_alter_validators_add_error_messages','2025-11-16 01:20:17.179354'),
(13,'auth','0008_alter_user_username_max_length','2025-11-16 01:20:17.200044'),
(14,'auth','0009_alter_user_last_name_max_length','2025-11-16 01:20:17.221227'),
(15,'auth','0010_alter_group_name_max_length','2025-11-16 01:20:17.245201'),
(16,'auth','0011_update_proxy_permissions','2025-11-16 01:20:17.255370'),
(17,'auth','0012_alter_user_first_name_max_length','2025-11-16 01:20:17.275535'),
(18,'sessions','0001_initial','2025-11-16 01:20:17.301234'),
(19,'suscripciones','0001_initial','2025-11-16 01:20:18.232773'),
(20,'suscripciones','0002_remove_notificacion_suscripcion_usuario_ee5639_idx_and_more','2025-11-16 01:59:46.053602');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_comentario`
--

DROP TABLE IF EXISTS `suscripciones_comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_comentario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `texto` longtext NOT NULL,
  `metadatos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`metadatos`)),
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` datetime(6) NOT NULL,
  `suscripcion_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suscripciones_coment_suscripcion_id_df272c52_fk_suscripci` (`suscripcion_id`),
  CONSTRAINT `suscripciones_coment_suscripcion_id_df272c52_fk_suscripci` FOREIGN KEY (`suscripcion_id`) REFERENCES `suscripciones_suscripcion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_comentario`
--

LOCK TABLES `suscripciones_comentario` WRITE;
/*!40000 ALTER TABLE `suscripciones_comentario` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_comentario` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_metodopago`
--

DROP TABLE IF EXISTS `suscripciones_metodopago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_metodopago` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(30) NOT NULL,
  `token` varchar(255) NOT NULL,
  `ultimos4` varchar(4) DEFAULT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `es_predeterminado` tinyint(1) NOT NULL,
  `metadatos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`metadatos`)),
  `creado_en` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_metodopago`
--

LOCK TABLES `suscripciones_metodopago` WRITE;
/*!40000 ALTER TABLE `suscripciones_metodopago` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_metodopago` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_moneda`
--

DROP TABLE IF EXISTS `suscripciones_moneda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_moneda` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(3) NOT NULL,
  `simbolo` varchar(5) NOT NULL,
  `decimales` smallint(5) unsigned NOT NULL CHECK (`decimales` >= 0),
  `ultima_actualizacion` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_moneda`
--

LOCK TABLES `suscripciones_moneda` WRITE;
/*!40000 ALTER TABLE `suscripciones_moneda` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_moneda` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_notificacion`
--

DROP TABLE IF EXISTS `suscripciones_notificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_notificacion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `enviar_en` datetime(6) NOT NULL,
  `enviado_en` datetime(6) DEFAULT NULL,
  `datos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`datos`)),
  `leida` tinyint(1) NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `suscripcion_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `suscripcion_enviado_18cceb_idx` (`enviado_en`),
  KEY `suscripcion_leida_9b0e8c_idx` (`leida`),
  KEY `suscripciones_notifi_suscripcion_id_4397c318_fk_suscripci` (`suscripcion_id`),
  KEY `suscripcion_enviar__890d6f_idx` (`enviar_en`),
  CONSTRAINT `suscripciones_notifi_suscripcion_id_4397c318_fk_suscripci` FOREIGN KEY (`suscripcion_id`) REFERENCES `suscripciones_suscripcion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_notificacion`
--

LOCK TABLES `suscripciones_notificacion` WRITE;
/*!40000 ALTER TABLE `suscripciones_notificacion` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_notificacion` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_pago`
--

DROP TABLE IF EXISTS `suscripciones_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_pago` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `monto` decimal(12,2) NOT NULL,
  `tasa_cambio` decimal(18,8) DEFAULT NULL,
  `comision` decimal(12,2) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `referencia` varchar(255) DEFAULT NULL,
  `respuesta_gateway` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`respuesta_gateway`)),
  `pagado_en` datetime(6) DEFAULT NULL,
  `creado_en` datetime(6) NOT NULL,
  `metodo_pago_id` bigint(20) DEFAULT NULL,
  `moneda_id` bigint(20) NOT NULL,
  `suscripcion_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `suscripcion_referen_33b4dc_idx` (`referencia`),
  KEY `suscripcion_estado_d967de_idx` (`estado`),
  KEY `suscripciones_pago_metodo_pago_id_6361e0ef_fk_suscripci` (`metodo_pago_id`),
  KEY `suscripciones_pago_moneda_id_450c2ccb_fk_suscripciones_moneda_id` (`moneda_id`),
  KEY `suscripciones_pago_suscripcion_id_a2e0c9e6_fk_suscripci` (`suscripcion_id`),
  KEY `suscripcion_creado__b7a6f8_idx` (`creado_en`),
  CONSTRAINT `suscripciones_pago_metodo_pago_id_6361e0ef_fk_suscripci` FOREIGN KEY (`metodo_pago_id`) REFERENCES `suscripciones_metodopago` (`id`),
  CONSTRAINT `suscripciones_pago_moneda_id_450c2ccb_fk_suscripciones_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `suscripciones_moneda` (`id`),
  CONSTRAINT `suscripciones_pago_suscripcion_id_a2e0c9e6_fk_suscripci` FOREIGN KEY (`suscripcion_id`) REFERENCES `suscripciones_suscripcion` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_pago`
--

LOCK TABLES `suscripciones_pago` WRITE;
/*!40000 ALTER TABLE `suscripciones_pago` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_pago` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_plan`
--

DROP TABLE IF EXISTS `suscripciones_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_plan` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(120) NOT NULL,
  `duracion_dias` int(10) unsigned NOT NULL CHECK (`duracion_dias` >= 0),
  `precio` decimal(12,2) NOT NULL,
  `descripcion` longtext NOT NULL,
  `creado_en` datetime(6) NOT NULL,
  `moneda_id` bigint(20) NOT NULL,
  `proveedor_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suscripciones_plan_proveedor_id_nombre_43852d14_uniq` (`proveedor_id`,`nombre`),
  KEY `suscripciones_plan_moneda_id_c10b74bc_fk_suscripciones_moneda_id` (`moneda_id`),
  CONSTRAINT `suscripciones_plan_moneda_id_c10b74bc_fk_suscripciones_moneda_id` FOREIGN KEY (`moneda_id`) REFERENCES `suscripciones_moneda` (`id`),
  CONSTRAINT `suscripciones_plan_proveedor_id_c3cde683_fk_suscripci` FOREIGN KEY (`proveedor_id`) REFERENCES `suscripciones_proveedor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_plan`
--

LOCK TABLES `suscripciones_plan` WRITE;
/*!40000 ALTER TABLE `suscripciones_plan` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_plan` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_proveedor`
--

DROP TABLE IF EXISTS `suscripciones_proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_proveedor` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(120) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `sitio_web` varchar(200) DEFAULT NULL,
  `categoria` varchar(50) NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `creado_en` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_proveedor`
--

LOCK TABLES `suscripciones_proveedor` WRITE;
/*!40000 ALTER TABLE `suscripciones_proveedor` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_proveedor` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Table structure for table `suscripciones_suscripcion`
--

DROP TABLE IF EXISTS `suscripciones_suscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `suscripciones_suscripcion` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_inicio` datetime(6) NOT NULL,
  `fecha_fin` datetime(6) NOT NULL,
  `renovacion_automatica` tinyint(1) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `descripcion` longtext DEFAULT NULL,
  `id_externo` varchar(255) DEFAULT NULL,
  `metadatos` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`metadatos`)),
  `creado_en` datetime(6) NOT NULL,
  `actualizado_en` datetime(6) NOT NULL,
  `moneda_id` bigint(20) NOT NULL,
  `plan_id` bigint(20) DEFAULT NULL,
  `proveedor_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `suscripcion_fecha_f_0ad475_idx` (`fecha_fin`),
  KEY `suscripcion_proveed_d51dd2_idx` (`proveedor_id`,`estado`),
  KEY `suscripciones_suscri_moneda_id_3489d211_fk_suscripci` (`moneda_id`),
  KEY `suscripciones_suscri_plan_id_38dba44f_fk_suscripci` (`plan_id`),
  KEY `suscripcion_estado_694884_idx` (`estado`),
  CONSTRAINT `suscripciones_suscri_moneda_id_3489d211_fk_suscripci` FOREIGN KEY (`moneda_id`) REFERENCES `suscripciones_moneda` (`id`),
  CONSTRAINT `suscripciones_suscri_plan_id_38dba44f_fk_suscripci` FOREIGN KEY (`plan_id`) REFERENCES `suscripciones_plan` (`id`),
  CONSTRAINT `suscripciones_suscri_proveedor_id_bb16e32a_fk_suscripci` FOREIGN KEY (`proveedor_id`) REFERENCES `suscripciones_proveedor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suscripciones_suscripcion`
--

LOCK TABLES `suscripciones_suscripcion` WRITE;
/*!40000 ALTER TABLE `suscripciones_suscripcion` DISABLE KEYS */;
set autocommit=0;
/*!40000 ALTER TABLE `suscripciones_suscripcion` ENABLE KEYS */;
UNLOCK TABLES;
commit;

--
-- Dumping routines for database 'subscription'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-11-15 21:18:49
