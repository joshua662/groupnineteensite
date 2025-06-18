-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 16, 2025 at 07:54 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `groupnineteendj_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add genders', 1, 'add_genders'),
(2, 'Can change genders', 1, 'change_genders'),
(3, 'Can delete genders', 1, 'delete_genders'),
(4, 'Can view genders', 1, 'view_genders'),
(5, 'Can add student', 2, 'add_student'),
(6, 'Can change student', 2, 'change_student'),
(7, 'Can delete student', 2, 'delete_student'),
(8, 'Can view student', 2, 'view_student'),
(9, 'Can add teacher', 3, 'add_teacher'),
(10, 'Can change teacher', 3, 'change_teacher'),
(11, 'Can delete teacher', 3, 'delete_teacher'),
(12, 'Can view teacher', 3, 'view_teacher'),
(13, 'Can add task', 4, 'add_task'),
(14, 'Can change task', 4, 'change_task'),
(15, 'Can delete task', 4, 'delete_task'),
(16, 'Can view task', 4, 'view_task'),
(17, 'Can add profile', 5, 'add_profile'),
(18, 'Can change profile', 5, 'change_profile'),
(19, 'Can delete profile', 5, 'delete_profile'),
(20, 'Can view profile', 5, 'view_profile'),
(21, 'Can add log entry', 6, 'add_logentry'),
(22, 'Can change log entry', 6, 'change_logentry'),
(23, 'Can delete log entry', 6, 'delete_logentry'),
(24, 'Can view log entry', 6, 'view_logentry'),
(25, 'Can add permission', 7, 'add_permission'),
(26, 'Can change permission', 7, 'change_permission'),
(27, 'Can delete permission', 7, 'delete_permission'),
(28, 'Can view permission', 7, 'view_permission'),
(29, 'Can add group', 8, 'add_group'),
(30, 'Can change group', 8, 'change_group'),
(31, 'Can delete group', 8, 'delete_group'),
(32, 'Can view group', 8, 'view_group'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add content type', 10, 'add_contenttype'),
(38, 'Can change content type', 10, 'change_contenttype'),
(39, 'Can delete content type', 10, 'delete_contenttype'),
(40, 'Can view content type', 10, 'view_contenttype'),
(41, 'Can add session', 11, 'add_session'),
(42, 'Can change session', 11, 'change_session'),
(43, 'Can delete session', 11, 'delete_session'),
(44, 'Can view session', 11, 'view_session'),
(45, 'Can add assigned task', 12, 'add_assignedtask'),
(46, 'Can change assigned task', 12, 'change_assignedtask'),
(47, 'Can delete assigned task', 12, 'delete_assignedtask'),
(48, 'Can view assigned task', 12, 'view_assignedtask'),
(49, 'Can add section', 13, 'add_section'),
(50, 'Can change section', 13, 'change_section'),
(51, 'Can delete section', 13, 'delete_section'),
(52, 'Can view section', 13, 'view_section');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$1Zb9MaZHKnSXzyq3FlEFD7$7x8XVPPjQC2uZy9xbRRN8I9blZBPi4xj4NXoOA4CDkI=', '2025-06-12 02:08:47.799828', 0, 'lesterlawag', '', '', 'johnlesterlawag03@gmail.com', 0, 1, '2025-06-11 02:58:05.284211'),
(2, 'pbkdf2_sha256$600000$DRxc4s7dew7WwPowK8ppVN$T/WjWjtoC62XSYxsdEkO+iN+3JJmq0va6nXA9GBquEs=', '2025-06-13 06:08:18.327628', 1, 'lesterlawag123', '', '', 'lesterlawag@gmail.com', 1, 1, '2025-06-13 06:07:53.130845');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `crud_section`
--

CREATE TABLE `crud_section` (
  `id` bigint(20) NOT NULL,
  `name` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `crud_section`
--

INSERT INTO `crud_section` (`id`, `name`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'admin', 'logentry'),
(8, 'auth', 'group'),
(7, 'auth', 'permission'),
(9, 'auth', 'user'),
(10, 'contenttypes', 'contenttype'),
(12, 'crud', 'assignedtask'),
(1, 'crud', 'genders'),
(5, 'crud', 'profile'),
(13, 'crud', 'section'),
(2, 'crud', 'student'),
(4, 'crud', 'task'),
(3, 'crud', 'teacher'),
(11, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-11 02:38:29.821304'),
(2, 'auth', '0001_initial', '2025-06-11 02:38:30.429650'),
(3, 'admin', '0001_initial', '2025-06-11 02:38:30.576426'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-06-11 02:38:30.586739'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-11 02:38:30.606925'),
(6, 'contenttypes', '0002_remove_content_type_name', '2025-06-11 02:38:30.685556'),
(7, 'auth', '0002_alter_permission_name_max_length', '2025-06-11 02:38:30.753959'),
(8, 'auth', '0003_alter_user_email_max_length', '2025-06-11 02:38:30.770665'),
(9, 'auth', '0004_alter_user_username_opts', '2025-06-11 02:38:30.781657'),
(10, 'auth', '0005_alter_user_last_login_null', '2025-06-11 02:38:30.840540'),
(11, 'auth', '0006_require_contenttypes_0002', '2025-06-11 02:38:30.845397'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2025-06-11 02:38:30.858771'),
(13, 'auth', '0008_alter_user_username_max_length', '2025-06-11 02:38:30.875789'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2025-06-11 02:38:30.893033'),
(15, 'auth', '0010_alter_group_name_max_length', '2025-06-11 02:38:30.909910'),
(16, 'auth', '0011_update_proxy_permissions', '2025-06-11 02:38:30.921150'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2025-06-11 02:38:30.938720'),
(18, 'crud', '0001_initial', '2025-06-11 02:38:31.356366'),
(19, 'sessions', '0001_initial', '2025-06-11 02:38:31.401112'),
(20, 'crud', '0002_remove_task_student_task_deadline_alter_task_table_and_more', '2025-06-11 13:45:19.112366'),
(21, 'crud', '0003_alter_assignedtask_table_alter_task_table', '2025-06-11 13:47:32.860097'),
(22, 'crud', '0004_assignedtask_submission_file', '2025-06-14 02:44:35.762474'),
(23, 'crud', '0005_remove_profile_gender_remove_profile_user_and_more', '2025-06-15 04:20:45.124257'),
(24, 'crud', '0006_section_student_section_task_section', '2025-06-15 11:32:30.633805'),
(25, 'crud', '0007_remove_section_section_section_name', '2025-06-15 11:42:29.574571'),
(26, 'crud', '0008_remove_task_section_assignedtask_section_and_more', '2025-06-15 12:12:07.672858'),
(27, 'crud', '0009_remove_student_subject', '2025-06-15 12:47:38.623716'),
(28, 'crud', '0010_assignedtask_rating', '2025-06-15 13:03:44.745359'),
(29, 'crud', '0011_task_section', '2025-06-15 13:20:57.302693'),
(30, 'crud', '0012_alter_assignedtask_section_alter_task_section', '2025-06-15 13:32:03.130635'),
(31, 'crud', '0013_assignedtask_created_at_assignedtask_updated_at', '2025-06-15 17:18:39.149731'),
(32, 'crud', '0014_assignedtask_submitted_at', '2025-06-15 17:20:22.247768');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('xppo8ny01ju1v1gi1p6ghdr6b8afqwuw', '.eJyrViouKU1JzSuJz0xRsjI20IHzS4tTi_ISc1OVrGBChsZKOkqZxfEwFYmlJRlAOjM5sSQVqLmkqDS1FgCWWB2a:1uR2YR:p7I3OMo0Zg3UTzV8R6Lw_oZzS0TaQ-T7UBKcU-3U9_M', '2025-06-30 05:38:47.640831');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_assigned_task`
--

CREATE TABLE `tbl_assigned_task` (
  `id` bigint(20) NOT NULL,
  `assigned_at` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `student_id` bigint(20) NOT NULL,
  `task_id` bigint(20) NOT NULL,
  `submission_file` varchar(100) DEFAULT NULL,
  `section_id` bigint(20) DEFAULT NULL,
  `rating` int(10) UNSIGNED DEFAULT NULL CHECK (`rating` >= 0),
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `submitted_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_assigned_task`
--

INSERT INTO `tbl_assigned_task` (`id`, `assigned_at`, `status`, `student_id`, `task_id`, `submission_file`, `section_id`, `rating`, `created_at`, `updated_at`, `submitted_at`) VALUES
(64, '2025-06-15 15:27:57.946793', 'submitted', 20, 19, 'submissions/Screenshot_1.png', 1, NULL, '2025-06-15 17:18:39.063189', '2025-06-15 20:32:07.108822', '2025-06-15 20:32:07.101195'),
(66, '2025-06-15 15:27:57.956448', 'submitted', 30, 19, 'submissions/Screenshot_3_PtiQv9G.png', 1, NULL, '2025-06-15 17:18:39.063189', '2025-06-16 05:41:52.173568', '2025-06-16 05:41:52.166092'),
(72, '2025-06-16 04:55:43.343815', 'submitted', 20, 21, 'submissions/Screenshot_3_dvf59M1.png', 1, NULL, '2025-06-16 04:55:43.343910', '2025-06-16 05:06:16.367694', '2025-06-16 05:06:16.358387'),
(73, '2025-06-16 04:55:43.348759', 'pending', 30, 21, '', 1, NULL, '2025-06-16 04:55:43.348880', '2025-06-16 04:55:43.348898', '2025-06-16 04:55:43.348814'),
(74, '2025-06-16 04:56:01.649113', 'pending', 21, 22, '', 2, NULL, '2025-06-16 04:56:01.649245', '2025-06-16 04:56:01.649262', '2025-06-16 04:56:01.649167'),
(75, '2025-06-16 04:56:01.655075', 'pending', 24, 22, '', 2, NULL, '2025-06-16 04:56:01.655187', '2025-06-16 04:56:01.655204', '2025-06-16 04:56:01.655125'),
(76, '2025-06-16 04:56:01.663748', 'pending', 25, 22, '', 2, NULL, '2025-06-16 04:56:01.663840', '2025-06-16 04:56:01.663851', '2025-06-16 04:56:01.663791'),
(77, '2025-06-16 04:56:01.670172', 'pending', 31, 22, '', 2, NULL, '2025-06-16 04:56:01.670264', '2025-06-16 04:56:01.670274', '2025-06-16 04:56:01.670216'),
(78, '2025-06-16 04:56:01.675513', 'pending', 34, 22, '', 2, NULL, '2025-06-16 04:56:01.675650', '2025-06-16 04:56:01.675677', '2025-06-16 04:56:01.675564'),
(79, '2025-06-16 04:56:01.680845', 'pending', 39, 22, '', 2, NULL, '2025-06-16 04:56:01.680974', '2025-06-16 04:56:01.680992', '2025-06-16 04:56:01.680899'),
(80, '2025-06-16 04:56:38.048950', 'submitted', 20, 23, 'submissions/Screenshot_3_Is3jVYT.png', 1, NULL, '2025-06-16 04:56:38.049050', '2025-06-16 05:04:52.790014', '2025-06-16 05:04:52.781669'),
(81, '2025-06-16 04:56:38.054613', 'pending', 30, 23, '', 1, NULL, '2025-06-16 04:56:38.054696', '2025-06-16 04:56:38.054707', '2025-06-16 04:56:38.054654');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_student`
--

CREATE TABLE `tbl_student` (
  `student_id` bigint(20) NOT NULL,
  `username` varchar(150) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  `suffix` varchar(20) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `birth_date` date NOT NULL,
  `age` int(10) UNSIGNED NOT NULL CHECK (`age` >= 0),
  `email` varchar(254) NOT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `section_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_student`
--

INSERT INTO `tbl_student` (`student_id`, `username`, `password`, `first_name`, `middle_name`, `last_name`, `suffix`, `gender`, `birth_date`, `age`, `email`, `contact_number`, `created_at`, `updated_at`, `address`, `section_id`) VALUES
(19, 'student2', 'pbkdf2_sha256$600000$VfaQaGxWQsP6h2dhCslocL$S21yuG5MBAw2OVQT0JEgTZ5AKnw07YhvdlRKlYprU3A=', 'First2', 'Middle2', 'Last2', '', 'other', '2005-03-02', 20, 'student2@example.com', '09171000002', '2025-06-15 12:48:35.216359', '2025-06-15 19:30:03.338054', ' ', 3),
(20, 'student3', 'pbkdf2_sha256$600000$O8vpIWxfaDEx7fpkhD2AAV$mwCwYH5g2+hxopflKeP1C2BgS/xZQQES/jMBXv2OuBo=', 'First3', 'Middle3', 'Last3', '', 'male', '2005-04-01', 20, 'student3@example.com', '09171000003', '2025-06-15 12:48:35.964768', '2025-06-15 12:48:35.964803', '3 Example St, City', 1),
(21, 'student4', 'pbkdf2_sha256$600000$phwmDlgXPhvjxDv2hQWn0m$CWo9lxfC1ecfrbSBNYX12PN8cpxvgUw0Ljn6h3PdhQw=', 'First4', 'Middle4', 'Last4', '', 'female', '2005-05-01', 20, 'student4@example.com', '09171000004', '2025-06-15 12:48:36.729047', '2025-06-15 12:48:36.729100', '4 Example St, City', 2),
(22, 'student5', 'pbkdf2_sha256$600000$0jojzILRvVpo7N6GP85A77$hGHvLHvbPs8DnwvCHiIE0W7TGwAql/Vqz5+/pikTQAo=', 'First5', 'Middle5', 'Last5', 'Jr.', 'male', '2005-05-31', 20, 'student5@example.com', '09171000005', '2025-06-15 12:48:37.523546', '2025-06-15 12:48:37.523594', '5 Example St, City', 3),
(23, 'student6', 'pbkdf2_sha256$600000$w4zRaexBWPr587EHFlgUBv$YaMHMlgH03LkFkquRO/OxBBabZ+A2pFbr9KchWalnVc=', 'First6', 'Middle6', 'Last6', '', 'female', '2005-06-30', 19, 'student6@example.com', '09171000006', '2025-06-15 12:48:38.289648', '2025-06-15 12:48:38.289685', '6 Example St, City', 3),
(24, 'student7', 'pbkdf2_sha256$600000$B4apGygsbTsMb4aqF1X2Qg$wuTh0XppBwNFrr7Xj0Rz9/UC3Ct9cQrRPoO88Ne/unM=', 'First7', 'Middle7', 'Last7', '', 'female', '2005-07-30', 19, 'student7@example.com', '09171000007', '2025-06-15 12:48:39.063563', '2025-06-15 12:48:39.063608', '7 Example St, City', 2),
(25, 'student8', 'pbkdf2_sha256$600000$azFF9rlXza9EOkzu5Vb5Dv$6+ZL3S1MNkQtRXCULLxOspDuL1FWjUH/Awhyg04T/1U=', 'First8', 'Middle8', 'Last8', '', 'other', '2005-08-29', 19, 'student8@example.com', '09171000008', '2025-06-15 12:48:39.842629', '2025-06-15 12:48:39.842666', '8 Example St, City', 2),
(26, 'student9', 'pbkdf2_sha256$600000$bhUBWpwnhOeFadqzy4SSEe$aqrAQN0y/R8Io8H6ANwFxSdkt8ecc+uklcOtjH2BULE=', 'First9', 'Middle9', 'Last9', '', 'other', '2005-09-28', 19, 'student9@example.com', '09171000009', '2025-06-15 12:48:40.642008', '2025-06-15 12:48:40.642050', '9 Example St, City', 3),
(27, 'student10', 'pbkdf2_sha256$600000$2wy97qqD7gnwzyw8pWGEQe$vqt1O05IZJnl/inD2GJ7MtNyDSKjWnavxNMpLvxpBd4=', 'First10', 'Middle10', 'Last10', 'Jr.', 'female', '2005-10-28', 19, 'student10@example.com', '09171000010', '2025-06-15 12:48:41.405820', '2025-06-15 12:48:41.405862', '10 Example St, City', 3),
(28, 'student11', 'pbkdf2_sha256$600000$8UZjAEkXTS1crNWo0ED3uO$6f95iWPbACz5awxENHrBGttwaOmVOHdUJdri0+3kkP4=', 'First11', 'Middle11', 'Last11', '', 'other', '2005-11-27', 19, 'student11@example.com', '09171000011', '2025-06-15 12:48:42.178162', '2025-06-15 12:48:42.178201', '11 Example St, City', 3),
(30, 'student13', 'pbkdf2_sha256$600000$Dvt5xYrvy0tcZF2SDbOotJ$koOLhQ9eaGuXuWnfGWAddxQIeEXcaPmudmPXmTHPBAw=', 'First13', 'Middle13', 'Last13', '', 'female', '2006-01-26', 19, 'student13@example.com', '09171000013', '2025-06-15 12:48:43.695285', '2025-06-15 12:48:43.695317', '13 Example St, City', 1),
(31, 'student14', 'pbkdf2_sha256$600000$xy0u4gKrMw7hFJAHP4NnGA$KlPqYdSqwaexx+TsGRthtY+whqMHZXQXaG9+QcN9dKs=', 'First14', 'Middle14', 'Last14', '', 'male', '2006-02-25', 19, 'student14@example.com', '09171000014', '2025-06-15 12:48:44.454106', '2025-06-15 12:48:44.454147', '14 Example St, City', 2),
(32, 'student15', 'pbkdf2_sha256$600000$4bilmHAjZdT3lTQZudXJv5$pGWaQsKSnAn9ywCplzSIACs1N3ssMpxmySh2OV40YL4=', 'First15', 'Middle15', 'Last15', 'Jr.', 'female', '2006-03-27', 19, 'student15@example.com', '09171000015', '2025-06-15 12:48:45.237519', '2025-06-15 12:48:45.237555', '15 Example St, City', 3),
(33, 'student16', 'pbkdf2_sha256$600000$0S6qABuzzVtA617NlnawrJ$AmhFS/aDPVgkWYQOCmH2sDbMBCke0Hz8UuR+AXHHy5I=', 'First16', 'Middle16', 'Last16', '', 'male', '2006-04-26', 19, 'student16@example.com', '09171000016', '2025-06-15 12:48:46.022224', '2025-06-15 12:48:46.022257', '16 Example St, City', 3),
(34, 'student17', 'pbkdf2_sha256$600000$4OS0QIHrNgRKZKDqhpiPDw$MathZc0Nu6bE7ZfSuUjIqhk0epqDaEUYRbnF/TCRTNA=', 'First17', 'Middle17', 'Last17', '', 'female', '2006-05-26', 19, 'student17@example.com', '09171000017', '2025-06-15 12:48:46.764355', '2025-06-15 12:48:46.764390', '17 Example St, City', 2),
(35, 'student18', 'pbkdf2_sha256$600000$aXtHqTe38v2GqG82Ng8UAT$A0tCXl5hF4sf6EXu23Nx+MthkzM9cpxCSP3TH1TPoTg=', 'First18', 'Middle18', 'Last18', '', 'female', '2006-06-25', 18, 'student18@example.com', '09171000018', '2025-06-15 12:48:47.555134', '2025-06-15 12:48:47.555170', '18 Example St, City', 3),
(36, 'student19', 'pbkdf2_sha256$600000$94sAuWAYZ2i8gvLksXWyK8$el8HmKx49EWZxi0U7OvurVttQU5bpRQR68ZLGH/bPTM=', 'First19', 'Middle19', 'Last19', '', 'female', '2006-07-25', 18, 'student19@example.com', '09171000019', '2025-06-15 12:48:48.305294', '2025-06-15 12:48:48.305328', '19 Example St, City', 3),
(37, 'student20', 'pbkdf2_sha256$600000$McV7Kc1EWAckZQPO1IZoHB$qMPF8VBWPfZGgzLvvpIyUsSg1vcnFWnyzL/L0zAC0R0=', 'First20', 'Middle20', 'Last20', 'Jr.', 'female', '2006-08-24', 18, 'student20@example.com', '09171000020', '2025-06-15 12:48:49.109243', '2025-06-15 12:48:49.109279', '20 Example St, City', 3),
(38, 'masi123', 'pbkdf2_sha256$600000$LRxtU5To1F1uRdJuOP1SJy$wMps2r2CUP4f2HUr129GVxP1g9Ra1anklads5+00z1Y=', 'masahide', 'Pinalba', 'Yanagisawa', '', 'male', '2004-02-22', 21, 'yanagisawa@gmail.com', '02349423234', '2025-06-15 18:39:16.158204', '2025-06-15 18:39:16.158250', 'Sappian', 3),
(39, 'vicente123', 'pbkdf2_sha256$600000$iBgmaogS03Ns5kfcsrsjk1$MVhGERsxqkVL1RdPwTOowowq9d9GrRJFsG/Gm2D9ykM=', 'Vicentetete', '', 'Delid', 'III', 'male', '2002-12-22', 22, 'wqeweq@qweqw', '09171234567', '2025-06-15 18:41:54.104916', '2025-06-15 19:32:57.440951', 'Banica', 2),
(40, 'lesterlawag', 'pbkdf2_sha256$600000$NoKZjp6anQ8X09WepJyqjE$S3+hKjj6EB8qT+8PCMBdPPAe7VlMogw0EHp1AAXSXWo=', 'John Lester', 'Villasoto', 'Lawag', '', 'male', '2003-12-15', 21, 'johnlesterlawag03@gmail.com', '09506005960', '2025-06-16 05:35:21.545583', '2025-06-16 05:35:21.545640', 'Yabton', 3);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_task`
--

CREATE TABLE `tbl_task` (
  `id` bigint(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `teacher_id` bigint(20) NOT NULL,
  `deadline` datetime(6) DEFAULT NULL,
  `section_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_task`
--

INSERT INTO `tbl_task` (`id`, `title`, `description`, `created_at`, `updated_at`, `teacher_id`, `deadline`, `section_id`) VALUES
(19, 'Science', '1', '2025-06-15 15:27:57.932005', '2025-06-16 05:16:49.139838', 1, NULL, 1),
(21, 'ART 1', 'section A', '2025-06-16 04:55:43.331350', '2025-06-16 04:55:43.331385', 1, NULL, 1),
(22, 'ART 2', 'section B', '2025-06-16 04:56:01.611510', '2025-06-16 04:56:01.611564', 1, NULL, 2),
(23, 'ART 3', 'section C', '2025-06-16 04:56:38.009070', '2025-06-16 04:56:38.009121', 1, NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_teacher`
--

CREATE TABLE `tbl_teacher` (
  `teacher_id` bigint(20) NOT NULL,
  `username` varchar(150) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) NOT NULL,
  `suffix` varchar(20) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `birth_date` date NOT NULL,
  `age` int(10) UNSIGNED NOT NULL CHECK (`age` >= 0),
  `email` varchar(254) NOT NULL,
  `contact_number` varchar(20) DEFAULT NULL,
  `subject` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_teacher`
--

INSERT INTO `tbl_teacher` (`teacher_id`, `username`, `password`, `first_name`, `middle_name`, `last_name`, `suffix`, `gender`, `birth_date`, `age`, `email`, `contact_number`, `subject`, `created_at`, `updated_at`, `address`) VALUES
(1, 'chandler', 'pbkdf2_sha256$600000$Ykr1syXHD5bHLKupJqQGcR$q2X4hGHKiaoE8wC3+XItjNcCc/KSOooo+2xApB9wD7Y=', 'Cole', 'A.', 'Chandler', '', 'male', '1980-04-12', 45, 'cchandler@example.com', '09180000001', 'Mathematics', '2025-06-11 13:35:14.165396', '2025-06-15 15:14:09.463615', NULL),
(2, 'msmith', 'pbkdf2_sha256$600000$8gFcDc7PRYB6Sar3kz4xaM$iIzOfFMuadwmIj6qRXlSQ73vI/UsfLuP4IWmdk74cuU=', 'Maria', 'B.', 'Smith', 'PhD', 'female', '1975-09-23', 50, 'msmith@example.com', '09180000002', 'Science', '2025-06-11 13:35:17.336976', '2025-06-15 05:16:18.894914', NULL),
(3, 'lesterlawag', 'pbkdf2_sha256$600000$zofU9j4xUk4rL8fu0dpfct$5883ub+1g8y5ANKmzhJuDT1m2sMBOCQVT1iDuQQYcU8=', 'John Lester', 'Villasoto', 'Lawag', '', 'male', '2003-12-15', 21, 'johnlesterlawag03@gmail.com', '09506005960', '', '2025-06-15 04:53:41.142861', '2025-06-15 09:18:26.445941', ''),
(4, '2234123132', 'pbkdf2_sha256$600000$weVyaneJ2Ay3ul8vYXKIVR$EK7cFSlCwoD8u30ECZUhRskMUHihffSoP60rSgSfdLI=', '123123', '123123', '123123', '123123', 'male', '2222-02-22', 0, '123123123@123312', '123123123123', '', '2025-06-15 04:58:36.800916', '2025-06-15 04:58:36.800958', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `crud_section`
--
ALTER TABLE `crud_section`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_assigned_task`
--
ALTER TABLE `tbl_assigned_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `crud_assignedtask_student_id_8b47f8ca_fk_tbl_student_student_id` (`student_id`),
  ADD KEY `crud_assignedtask_task_id_cc5664b8_fk_crud_task_id` (`task_id`),
  ADD KEY `tbl_assigned_task_section_id_5fd651f4_fk_crud_section_id` (`section_id`);

--
-- Indexes for table `tbl_student`
--
ALTER TABLE `tbl_student`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `tbl_student_section_id_267bf5ef_fk_crud_section_id` (`section_id`);

--
-- Indexes for table `tbl_task`
--
ALTER TABLE `tbl_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tbl_task_teacher_id_6d81a137_fk_tbl_teacher_teacher_id` (`teacher_id`),
  ADD KEY `tbl_task_section_id_04e68732_fk_crud_section_id` (`section_id`);

--
-- Indexes for table `tbl_teacher`
--
ALTER TABLE `tbl_teacher`
  ADD PRIMARY KEY (`teacher_id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `crud_section`
--
ALTER TABLE `crud_section`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `tbl_assigned_task`
--
ALTER TABLE `tbl_assigned_task`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=82;

--
-- AUTO_INCREMENT for table `tbl_student`
--
ALTER TABLE `tbl_student`
  MODIFY `student_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `tbl_task`
--
ALTER TABLE `tbl_task`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `tbl_teacher`
--
ALTER TABLE `tbl_teacher`
  MODIFY `teacher_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_assigned_task`
--
ALTER TABLE `tbl_assigned_task`
  ADD CONSTRAINT `crud_assignedtask_student_id_8b47f8ca_fk_tbl_student_student_id` FOREIGN KEY (`student_id`) REFERENCES `tbl_student` (`student_id`),
  ADD CONSTRAINT `crud_assignedtask_task_id_cc5664b8_fk_crud_task_id` FOREIGN KEY (`task_id`) REFERENCES `tbl_task` (`id`),
  ADD CONSTRAINT `tbl_assigned_task_section_id_5fd651f4_fk_crud_section_id` FOREIGN KEY (`section_id`) REFERENCES `crud_section` (`id`);

--
-- Constraints for table `tbl_student`
--
ALTER TABLE `tbl_student`
  ADD CONSTRAINT `tbl_student_section_id_267bf5ef_fk_crud_section_id` FOREIGN KEY (`section_id`) REFERENCES `crud_section` (`id`);

--
-- Constraints for table `tbl_task`
--
ALTER TABLE `tbl_task`
  ADD CONSTRAINT `tbl_task_section_id_04e68732_fk_crud_section_id` FOREIGN KEY (`section_id`) REFERENCES `crud_section` (`id`),
  ADD CONSTRAINT `tbl_task_teacher_id_6d81a137_fk_tbl_teacher_teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `tbl_teacher` (`teacher_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
