-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 16, 2021 at 08:23 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clg_prject`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_up`
--

CREATE TABLE `admin_up` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_up`
--

INSERT INTO `admin_up` (`id`, `username`, `password`) VALUES
(1, 'admin12', 'ec6a6536ca304edf844d1d248a4f08dc'),
(3, 'admin2', '81dc9bdb52d04dc20036dbd8313ed055');

-- --------------------------------------------------------

--
-- Table structure for table `answer`
--

CREATE TABLE `answer` (
  `Id` int(11) NOT NULL,
  `Qp_code` varchar(255) NOT NULL,
  `student_name` varchar(255) NOT NULL,
  `stud_id` int(11) NOT NULL,
  `Question_id` int(11) NOT NULL,
  `selected_answer` varchar(255) NOT NULL,
  `right_answer` varchar(255) NOT NULL,
  `Quest_attempted` int(11) NOT NULL,
  `status` bit(1) NOT NULL,
  `marks_obtained` int(11) NOT NULL,
  `CreatedOn` timestamp NOT NULL DEFAULT current_timestamp(),
  `CollegeId` int(11) NOT NULL,
  `Class` varchar(255) NOT NULL,
  `Exam_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `answer`
--

INSERT INTO `answer` (`Id`, `Qp_code`, `student_name`, `stud_id`, `Question_id`, `selected_answer`, `right_answer`, `Quest_attempted`, `status`, `marks_obtained`, `CreatedOn`, `CollegeId`, `Class`, `Exam_name`) VALUES
(1, 'MT Unit 1Sem 4dbms', 'test', 6, 1, 'D', 'D', 1, b'1', 2, '2021-05-16 18:07:01', 3, '', ''),
(2, 'MT Unit 1Sem 4dbms', 'test', 6, 2, 'C', 'C', 1, b'1', 2, '2021-05-16 18:07:01', 3, '', ''),
(3, 'MT Unit 1Sem 4dbms', 'test', 6, 3, 'A', 'D', 1, b'0', 0, '2021-05-16 18:07:01', 3, '', '');

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `classid` int(11) NOT NULL,
  `classname` varchar(255) NOT NULL,
  `teacher` varchar(255) NOT NULL,
  `stream` varchar(255) NOT NULL,
  `CollegeId` int(11) NOT NULL,
  `Createdon` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`classid`, `classname`, `teacher`, `stream`, `CollegeId`, `Createdon`) VALUES
(1, 'FY', 'sarita', 'IT', 3, '2021-05-15 14:35:16'),
(2, 'SY', 'sarita', 'IT', 3, '2021-05-15 14:39:38');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `deptid` int(11) NOT NULL,
  `DeptName` varchar(255) NOT NULL,
  `Createdon` datetime NOT NULL DEFAULT current_timestamp(),
  `Updatedon` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp(),
  `CollegeId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`deptid`, `DeptName`, `Createdon`, `Updatedon`, `CollegeId`) VALUES
(1, 'IT', '2021-04-13 23:44:39', '2021-04-13 23:44:39', 3),
(10, 'extc', '2021-04-14 01:05:37', '0000-00-00 00:00:00', 3),
(13, 'Bsc IT', '2021-04-14 01:20:53', '0000-00-00 00:00:00', 3),
(14, 'electrical', '2021-04-14 01:27:17', '0000-00-00 00:00:00', 3),
(15, 'mechanical', '2021-04-14 01:30:33', '0000-00-00 00:00:00', 3),
(16, 'COMPUTER', '2021-04-14 01:42:19', '0000-00-00 00:00:00', 3),
(18, 'Instrumente', '2021-05-15 19:26:17', '0000-00-00 00:00:00', 3);

-- --------------------------------------------------------

--
-- Table structure for table `exam_list`
--

CREATE TABLE `exam_list` (
  `Exam_id` int(11) NOT NULL,
  `Exame_name` varchar(255) NOT NULL,
  `Exam_descrp` varchar(255) NOT NULL,
  `Class` varchar(255) NOT NULL,
  `DeptName` varchar(255) NOT NULL,
  `Exam_date` date NOT NULL,
  `Exam_status` int(11) NOT NULL,
  `Exam_start_time` time NOT NULL,
  `Exam_end_time` time NOT NULL,
  `subject` varchar(255) NOT NULL,
  `QP_code` varchar(255) NOT NULL,
  `CollegeId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `exam_list`
--

INSERT INTO `exam_list` (`Exam_id`, `Exame_name`, `Exam_descrp`, `Class`, `DeptName`, `Exam_date`, `Exam_status`, `Exam_start_time`, `Exam_end_time`, `subject`, `QP_code`, `CollegeId`) VALUES
(1, 'Maths UT1', 'UT1', 'FY', 'IT', '2021-05-16', 0, '22:00:00', '23:59:00', 'Maths', 'MT Unit 1Sem 4dbms', 3);

-- --------------------------------------------------------

--
-- Table structure for table `papers`
--

CREATE TABLE `papers` (
  `id` int(11) NOT NULL,
  `Question_type` varchar(225) NOT NULL,
  `Paper_set_name` varchar(255) NOT NULL,
  `Qp_code` varchar(255) NOT NULL,
  `Class` varchar(255) NOT NULL,
  `No_of_questions` int(11) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `CollegeId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `papers`
--

INSERT INTO `papers` (`id`, `Question_type`, `Paper_set_name`, `Qp_code`, `Class`, `No_of_questions`, `subject`, `CollegeId`) VALUES
(5, 'mcq', 'MT Unit 1', 'MT Unit 1Sem 4dbms', 'fy', 4, 'dbms', 3),
(6, 'mcq', 'Unit2', 'Unit24FYdbmsMaths', 'FY', 3, 'Maths', 3);

-- --------------------------------------------------------

--
-- Table structure for table `question_paper`
--

CREATE TABLE `question_paper` (
  `Qp_id` int(11) NOT NULL,
  `Paper_set_name` varchar(255) NOT NULL,
  `Qp_code` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `Class` varchar(255) NOT NULL,
  `No_of_questions` int(11) NOT NULL,
  `Total_marks` int(11) NOT NULL,
  `Question_type` varchar(255) NOT NULL,
  `Question` varchar(255) NOT NULL,
  `Option1` varchar(255) NOT NULL,
  `Option2` varchar(255) NOT NULL,
  `Option3` varchar(225) NOT NULL,
  `Option4` varchar(225) NOT NULL,
  `Right_answer` varchar(225) NOT NULL,
  `CollegeId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `question_paper`
--

INSERT INTO `question_paper` (`Qp_id`, `Paper_set_name`, `Qp_code`, `subject`, `Class`, `No_of_questions`, `Total_marks`, `Question_type`, `Question`, `Option1`, `Option2`, `Option3`, `Option4`, `Right_answer`, `CollegeId`) VALUES
(1, 'MT Unit 1', 'MT Unit 1Sem 4dbms', 'dbms', 'FY', 4, 2, 'mcq', 'What is SQL', 'Noting', 'Queryinh', 'Language', 'Structured Query Language', 'D', 3),
(2, 'MT Unit 1', 'MT Unit 1Sem 4dbms', 'dbms', 'FY', 4, 2, 'mcq', 'What is SP', 'Somethin', 'Samepass', 'Stored Procedure', 'Structured Proc', 'C', 3),
(3, 'MT Unit 1', 'MT Unit 1Sem 4dbms', 'dbms', 'FY', 4, 2, 'mcq', 'what is dbms', 'database', 'management', 'system', 'None', 'D', 3),
(4, 'MT Unit 1', 'MT Unit 1Sem 4dbms', 'dbms', 'FY', 4, 2, 'mcq', 'Founderof MSSQL', 'MSsql', 'Sql', 'Microsoft', 'Oracle', 'C', 3),
(5, 'Unit2', 'Unit24FYdbmsMaths', 'Maths', 'FY', 3, 0, 'mcq', 'What is 1+3', '13', '31', '1+3', '4', 'D', 3),
(6, 'Unit2', 'Unit24FYdbmsMaths', 'Maths', 'FY', 3, 0, 'mcq', 'Rational Numbers', '1,2,3', '-1,-2,-3', '0,1,2,3', '0', 'A', 3),
(7, 'Unit2', 'Unit24FYdbmsMaths', 'Maths', 'FY', 3, 0, 'mcq', 'What is 0', 'zero', '001', '00', 'None', 'A', 3);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Stud_id` int(11) NOT NULL,
  `Stud_Name` varchar(255) NOT NULL,
  `Stud_Contact` int(11) NOT NULL,
  `Stud_Email` varchar(255) NOT NULL,
  `Parent_name` varchar(255) NOT NULL,
  `Parent_contact` int(11) NOT NULL,
  `class` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Profile_Img` varchar(255) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `CreatedOn` datetime NOT NULL DEFAULT current_timestamp(),
  `UpdateOn` datetime DEFAULT NULL,
  `CollegeId` int(11) NOT NULL,
  `DeptName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Stud_id`, `Stud_Name`, `Stud_Contact`, `Stud_Email`, `Parent_name`, `Parent_contact`, `class`, `Address`, `Profile_Img`, `Username`, `Password`, `CreatedOn`, `UpdateOn`, `CollegeId`, `DeptName`) VALUES
(2, 'sagar jadhav', 2147483647, 'saragar@gmail.com', 'veer jadhav', 454565421, 'FY', 'Ad avenue dfsefte  fgrd', '', 'sagar1', '81dc9bdb52d04dc20036dbd8313ed055', '2021-04-14 21:55:38', NULL, 3, 'computer'),
(3, 'rita rathod', 624555447, 'sarita@gmail.com', 'karima rathod', 663358455, 'FY', 'gdfef dggfsefr rgf', '', 'sarita1', '81dc9bdb52d04dc20036dbd8313ed055', '2021-04-26 21:00:45', NULL, 3, 'IT'),
(6, 'test', 324324324, 'test@gmail.com', 'veer jadhav', 34545345, 'FY', 'test', '', 'test', '098f6bcd4621d373cade4e832627b4f6', '2021-05-16 17:57:03', NULL, 3, 'IT');

-- --------------------------------------------------------

--
-- Table structure for table `stud_up`
--

CREATE TABLE `stud_up` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stud_up`
--

INSERT INTO `stud_up` (`id`, `username`, `password`) VALUES
(1, 'stud1', '81dc9bdb52d04dc20036dbd8313ed055'),
(2, 'stud2', '827ccb0eea8a706c4c34a16891f84e7b');

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `Sub_id` int(11) NOT NULL,
  `SubName` varchar(255) NOT NULL,
  `SubCode` int(11) NOT NULL,
  `Class` int(11) NOT NULL,
  `Teacherid` int(11) NOT NULL,
  `teacher` varchar(255) NOT NULL,
  `CreatedOn` timestamp NOT NULL DEFAULT current_timestamp(),
  `UpdatedOn` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `CollegeId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subject`
--

INSERT INTO `subject` (`Sub_id`, `SubName`, `SubCode`, `Class`, `Teacherid`, `teacher`, `CreatedOn`, `UpdatedOn`, `CollegeId`) VALUES
(1, 'dbms', 3311, 0, 0, '', '2021-04-14 10:22:15', '0000-00-00 00:00:00', 3),
(4, 'Maths', 3311, 0, 2, 'riya chavan', '2021-05-15 14:34:41', '2021-05-15 14:34:41', 3);

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `Teacher_id` int(11) NOT NULL,
  `T_name` varchar(255) NOT NULL,
  `T_Contact` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Qualification` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Class` int(11) NOT NULL,
  `User_Role` varchar(255) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `CreatedOn` timestamp NOT NULL DEFAULT current_timestamp(),
  `UpdateOn` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE current_timestamp(),
  `CollegeId` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`Teacher_id`, `T_name`, `T_Contact`, `Email`, `Qualification`, `Address`, `Class`, `User_Role`, `Username`, `Password`, `CreatedOn`, `UpdateOn`, `CollegeId`) VALUES
(1, 'sarita', '64646469', 'saritamourya27@gmail.com', 'diploma pass', 'fdwesrewr feeesr', 0, '1', 'sarita', '7b5bb2acf3e2d7261f0636352615f0ec', '2021-04-11 20:12:23', '2021-05-15 19:57:17', 3),
(2, 'riya chavan', '6484849', 'chavan@gmail.com', 'phd', 'dffrfv  gergee fsefr ferw', 0, 'C-c', 'rchavan', '40e592df56e6e34bb26bc840cce82a7a', '2021-04-11 20:24:33', '2021-05-15 19:57:22', 3),
(4, 'mahima more', '6484849884', 'morem@gmail.com', 'MD pHD', 'dffrfv  gergee fsefr ferw uhui', 0, 'college staff', 'mmore', 'c40e7f01a2c031f1188cd0d827110de9', '2021-04-13 16:50:24', '2021-05-15 19:57:26', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'sarita', '363ab055963fb24eff2cfc02437ec228'),
(3, 'sahish', 'a85864c0ccb95a7a41c2d6eb0aff49ae');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_up`
--
ALTER TABLE `admin_up`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `answer`
--
ALTER TABLE `answer`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`classid`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`deptid`);

--
-- Indexes for table `exam_list`
--
ALTER TABLE `exam_list`
  ADD PRIMARY KEY (`Exam_id`);

--
-- Indexes for table `papers`
--
ALTER TABLE `papers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `question_paper`
--
ALTER TABLE `question_paper`
  ADD PRIMARY KEY (`Qp_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Stud_id`);

--
-- Indexes for table `stud_up`
--
ALTER TABLE `stud_up`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subject`
--
ALTER TABLE `subject`
  ADD PRIMARY KEY (`Sub_id`);

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`Teacher_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_up`
--
ALTER TABLE `admin_up`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `answer`
--
ALTER TABLE `answer`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `classid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `deptid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `exam_list`
--
ALTER TABLE `exam_list`
  MODIFY `Exam_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `papers`
--
ALTER TABLE `papers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `question_paper`
--
ALTER TABLE `question_paper`
  MODIFY `Qp_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `Stud_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `stud_up`
--
ALTER TABLE `stud_up`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `subject`
--
ALTER TABLE `subject`
  MODIFY `Sub_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `Teacher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
