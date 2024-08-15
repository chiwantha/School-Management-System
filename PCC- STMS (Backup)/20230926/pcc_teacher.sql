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
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` varchar(100) DEFAULT NULL,
  `nic` varchar(100) DEFAULT NULL,
  `family_name` varchar(100) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `e_mail` varchar(100) DEFAULT NULL,
  `pone_number` varchar(10) DEFAULT NULL,
  `sub1` varchar(100) DEFAULT NULL,
  `sub2` varchar(100) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `address_line` varchar(100) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES ('1','710920389V','Kodikara Arachchige','Nimal','Kodikara','K.A.N. Kodikara','Male','kodikaranimal5252@gmail.com','711753014','Management','Management','1971-04-01','502','Pangala Hena','Lunugama'),('2','198063101820','#','Sanjeewanie','Pathirana','C.S.A. Pathirana','Female','chathusanpathi@gmail.com','718015349','Management','Management','1980-05-10','1/A/18, Rajamalwaththa','Godagedara','Mudungoda'),('3','837211190V','Konara Mudiyanselage','Krishali','Wijerathna','K.M.K.L. Wijerathna','Female','krishaliw@gmail.com','712455311','Management','Management','1983-08-08','103/16','Henegama','Gampaha'),('4','802393571V','Amarathungage','Layanal','Pemathilaka','A.L. Pemathilaka','Male','#','776856844','Sinhala','#','1980-08-26','249','Diklanda Waththa','Mandawala'),('5','841892020V','Kariyawasam Sembukudige','Sudesh','Priyadarshana','K.S.S. Priyadarshana','Male','#','718449018','Science','#','1984-07-07','35/3/A','Moragala','Dekatana'),('6','705010501V','Hapu Arachchige','Dhampika','Jayathilaka','H.A.P.D. Jayathilaka','Female','#','779610048','Library Management','#','1970-01-01','209','Lunugama','Mandawala'),('7','755551694V','Wijesooriya Arachchige','Dilani','Wijesooriya','W.A.D.S. Wijesooriya','Female','dilanisharmilaw@gmail.com','716862154','Logic','Sinhala','1975-02-24','126/1','Malinda','Kapugoda'),('8','736500370V','Gamachchige','Geethani','Jayawardhana','G.L.G. Jayawardhana','Female','geethanijayawardhana@gmail.com','714769566','English','#','1973-05-29','390/A','Degawaththa','Dompe'),('9','748100237V','Yapa Mudiyanselage','Nilani','Wijerathna','Y.M.N. Wijerathna','Female','nilanivijerathna1974@gmail.com','718048990','Business Studies','Business & Accounting Studies','1974-11-05','65/A','Moragala','Dekatana'),('10','791350174V','Wanniarachchi Kankanamalage','Wasantha','Wanniarachchi','W.K.W.K. Wanniarachchi','Male','wasanthawanni79@gmail.com','723936525','Dancing','#','1979-05-14','75/E','Diyawala','Kirindiwela'),('11','766242103V','Kuda Thanthirige','Yamuna','Gunathilaka','K.T.Y.N. Gunathilaka','Female','#','711305834','Home Science','Tamil','1976-05-03','21/4','Liyanegama','Dompe'),('13','847700114V','Bogoda Appuhamilage','Shakila','Nayomi','B.A.S. Nayomi','Female','shakilabogoda@gmail.com','712151077','Tamail','Political Science','1984-09-26','77','Demalagama (Wp)','#'),('14','805251727V','Hapu Arachchige','Harsha','Kumudunie','H.A.H. Kumudinie','Female','kumuduniesenanayake80@gmail.com','778962270','IT','GIT','1980-01-25','407/A','Meegahawaththa','Lunugama'),('15','817462464V','Kandana Arachchilage','Chathurika','Nadeeshani','K.A.C. Nadeeshani','Female','chathu81nadeeshani@gmail.com','718065879','Buddihist Civilization','Buddhism','1981-09-02','133/A','Rajahena','Dekatana'),('16','767601557V','Liyanasooriyalage','Iresha','Liyanasooriya','L.I.P. Liyanasooriya','Female','ireshaliyanasooriya12@gmail.com','711997356','Dancing','#','1976-09-16','267/B','New Road','Dompe'),('17','665782905V','Samarasingha Arachchige','Sandya','Kalyani','S.A.S. Kalyani','Female','sandyakalyani710@gmail.com','112409280','Economics','#','1966-03-18','86/6','Korambe','Dompe'),('18','836960483V','Madduma Arachchige','Chandrika ','Kumari','M.A.C. Kumari','Female','#','716204989','Agriculture','Science','1983-07-14','21/4','Ganegoda','Dompe'),('19','698050659V','Katuwawala Arachchige','Kusala','Madhuranganie','K.A.K. Maduranganie','Female','kusalamadurangani@gmail.com','723546171','Mathematics','#','1969-10-31','171/3','Polkotuwa Waththa','Dompe'),('20','835651614V','Marasingha Mudiyanselage','Renuka','Marasingha','M.M.N.R. Marasingha','Female','renukamarasinghe9@gmail.com','715659488','Health','#','1983-03-05','84','Demalagama (Wp)','#'),('21','778172046V','Bandula Kankanamalage','Chamila','Bandula','B.K.C.N. Bandula','Female','hasithadammika222@gmail.com','771653411','Geography','#','1977-11-12','51','Wanaluwawa','Gampaha'),('22','656410698V','Thissanayaka Mudiyanselage','Leelawathie','#','T.M. Leelawathie','Female','m.nambukarawasam@gmail.com','767356400','Agriculture','PTS','1965-06-20','291/5','Amanda Uyana','Dompe'),('23','915201458V','Mahawaththage Dona','Sewwandi','Kumarasingha','M.D.S.J. Kumarasingha','Female','sewwandikumarasinghe3@gmail.com','715172655','English','General English','1991-01-20','373/A','Mandawala Road','Radawana'),('24','848660930V','Udage Arachchige','Lanka','Udagearachchi','U.A.D.L. Udagearachchi','Female','#','112409507','Media','#','1984-12-31','81','Wanaluwawa','Dompe'),('25','895132110V','Nanayakkara Ranaweerage','Dulanjalie','Nanayakkara','N.R.D.N. Nanayakkara','Female','niranganr@gmail.com','715983682','Science','#','1989-01-13','66/B','Walpola','Ruggahawila'),('26','877280799V','Koswaththage','Wathsala','Perera','K.W.L. Perera','Female','wathsala15perera@gmail.com','711270132','Combined Maths','Mathematics','1987-08-15','322/3','Colombo Road','Gampaha'),('27','811680150V','Walakumbure Jayasingha Mudiyanselage','Manjula','Jayasingha','W.J.M.M.P. Jayasingha','Male','#','718456655','Art','#','1981-06-16','103','Kanda Road','Mandawala'),('28','810621575V','Wanasingha Arachchige','Sameera ','Jayathilaka','W.A.S.P. Jayathilaka','Male','#','718204590','History','Sinhala','1981-03-02','46/6','Kalukondayawa','Malwana'),('29','831131942V','Athukoralalage','Mayura','Athukorala','A.M.U. Athukorala','Male','mayura.e@gmail.com','702642637','History','Sinhala','1983-04-22','492/4','Dangalla','Pepiliyawala'),('30','765283019V','Madduma Kankanige','Achini','Inoka','M.K.A. Inoka','Female','#','778184680','Drama','#','1976-01-28','147/C','Keerthirathna Mawatha','Radawana'),('31','756020986V','#','Duleeka','Gunarathna','D. Gunarathna','Female','dulika411@gmail.com','702668750','Accounting','Business & Accounting Studies','1975-04-11','361','Parangoda','Dekatana'),('32','827852040V','Heenkenda Mudiyanselage','Helanthi','Ranaweera','H.M.H.S. Ranaweera','Female','helanthi@gmail.com','714400419','Mathematics','#','1982-10-11','131/A','Kirikiththa','Weliweriya'),('33','856353699V','Madurapperuma Arachchige','Jeewanie','Madurapperuma','M.A.J.R. Madurapperuma','Female','jeewani.madurapperuma@gmail.com','777552102','Science','#','1985-05-14','113/8','Pelahela','Dompe'),('34','796370645V','#','Nilanka','Rathnayaka','N.R. Rathnayaka','Female','roshinirathnayaka1979@gmail.com','712143336','English','#','1979-05-16','140/A/12, Kehelhena','Udupila','Delgoda'),('35','825511580V','Ranathunga Arachchilage','Pradeepa','Ranathunga','R.A.P.T. Ranathunaga','Female','pradeeparanathunga1982@gmail.com','779121682','Civic','Sinhala','1982-02-20','284/3','Dekatana South','Dekatana'),('36','687450124V','Gunasekara Dissanayakalage','Devika','Priyadarshanie','G.D.D. Priyadarshanie','Female','anusewwandi1998@gmail.com','716753538','Music','#','1968-09-01','309/1','Degalhamulla','Lunugama'),('37','707830085V','Patikiri Arachchige Dona','Preethi','Thilakarathna','P.A.D.P. Thilakarathana','Female','#','715203575','English','#','1970-10-09','202/7, Madugahavila','Indolamulla','Dompe'),('38','785202635V','#','Thushari','Gunawardhana','T.S.W. Gunawardhana','Female','thushari.gunawardana@gmail.com','#','IT','GIT','1978-01-20','557/2','Nedungahahena','Weliweriya'),('39','698242744V','Weerasekarage','Wajira','Weerasingha','W.W.M. Weerasingha','Female','wajiraweerasinghe1@gmail.com','718024871','Mathematics','#','1969-11-19','37/8','Kalukondayawa','Malwana'),('40','666952294V','Edirisingha Arachchige','Wasantaha','Edirisingha','E.A.W. Edirisingha','Female','wasanthaed12@gmail.com','711071027','Science','#','1966-07-13','72/1, Layanal Siriwardhana Mawatha','Linugama','Wanaluwawa'),('41','770452015V','Don','Hiyantha','Munasingha','D.H.N. Munasingha','Male','hiyanthanishan@gmail.com','719008333','Sinhala','Sinhala Literature','1977-02-14','553/3','Pahala Lunugama','Lunugama'),('42','756870505V','Kodithuwakku Kankanamalage','Priyanthi','Menaka','K.K.P. Menaka','Female','priyanthimenaka18@gmail.com','702170307','Sinhala','#','1975-07-15','224/20','Isurupura','Dekatana'),('43','800500400V','Gannoru Kankanamalage','Nishantha','Gannoruwa','G.K.R.N. Gannoruwa','Male','rgannoruwa@gmail.com','718030550','Mathematics','#','1980-02-19','124/A','Parathapa Kanda','Pugoda'),('44','637351419V','Rajapaksha Gunasekara Mudiyanselage','Anoma','Rajapaksha','R.G.M.A.N. Rajapaksha','Female','#','718098109','Health','#','1963-08-22','114/A','Mahenawaththa','Mandawala'),('45','686801098V','Kanangama Arachchige','Renuka','#','K.A. Renuka','Female','dushanisamraweera270@gmail.com','112536015','Sinhala','Civic','1968-06-28','120','Indolamulla','Dompe'),('46','196481901197','Hewawasam Haggallage','Kumudu','Hewawasam','H.H.K.M. Hewawasam','Female','kumuduhewawasam1@gmail.com','754325035','History','Geography','1964-11-14','349','Ambaraluwa (South)','Weliweriya'),('47','826454741V','Wijethungage','Chamari','Dissanayaka','W.C.N. Dissanayaka','Female','chamarisissanayaka1982@gmail.com','775482562','Home Science','PTS','1982-05-24','372/1','Dangalla','Pepiliyawala'),('48','887203350V','Weerapperumage','Nayomi','Sanika','W.N. Shanika','Female','#','777530567','Health','#','1988-08-07','294/1/14/1','Hansagiri Mawatha','Gampaha'),('49','870930151V','Makolage','Dilip','Kumara ','M.C.D. Kumara','Male','dilipmakolage233@gmail.com','718836434','History','#','1987-04-02','124','Meryland','Wathurugama'),('50','746471203V','Muthuporuthotage','Iroma','Perea','M.I. Perera','Female','iromaperera233@gmail.com','714501467','Buddihism','Hindi','1974-05-26','170/A 23','Kanduboda','Delgoda'),('51','696052581V','Niwunhelle Acharige','Rasika','Darshanie','N.A.R.W. Darshanie','Female','#','729437054','Political Science','Geography','1969-04-14','373','Medalanda','Dompe'),('52','647750354V','Edirisingha Arachchige','Anoma','Ranjanie','E.A.A. Ranjanie','Female','#','729821432','PTS','#','1964-10-01','231','Samanabedda','Thiththapaththara'),('53','198053300163','Kuruppu Gedara','Janitaha','Kuruppu','K.G.J.C. Kuruppu','Female','kgjckuruppu@gmail.com','773506908','Media','Geography','1980-02-02','200 D','Seewalie Mawatha','Dompe'),('54','806613673V','Herath Mudiyanselage','Chandanie','Herath','H.M.C. Herath','Female','herathchandani8@gmail.com','714068485','Bissiness Studies','Entrepreneurship Studies','1980-06-09','211','Batepola','Wathurugama'),('55','637211749V','Angam Podige ','Manel','Chandralatha','A.P.S.M. Chandralatha','Female','#','778921118','History','#','1963-08-08','364','Merilwaththa','Radawana'),('56','888073744V','Mambula Marapperuma Arachchige','Nimna','Abhayawardhana','M.M.A.S.N. Abhayawardhana','Female','mail2nimna98@gmail.com','714166966','Music','Sinhala','1988-11-02','361','Ahugammana','Demalagama'),('57','866222080V','Jayasingha Mudiyanselage','Chandra','Jayasingha','J.M.C. Jayasingha','Female','jayasinghechandra798@gmail.com','712843078','Sinhala','Tamil','1986-05-01','401/5','Degawaththa','Dompe'),('58','846692096V','#','Inoka','Kalansooriya','I.D. Kalansooriya','Female','kalansooriyaid@gmail.com','775072023','Mathematics','#','1984-06-17','138/01','Udamapitigama','Dompe'),('59','668481426V','Amuwala Dewage','Malanie','Priyangika','A.D.M. Priyangika','Female','malanipriyangika66@gmail.com','715104642','Civic','History','1966-12-13','273','Ahugammana','Demalagama'),('60','675070059V','Liyana Athukoralage Dona','Samanthika','Kulathunga','L.A.D.S.S. Kulathunga','Female','samanthikaathukorala822@gmail.com','712689135','English','General English','1967-01-07','43/1','Guruwala','Dompe'),('61','787012230V','Singankutti Athukoralage','Gayani','Athukorala','S.A.N.G. Athukorala','Female','gayaniathukorala@gmail.com','714396585','Accounting','#','1978-07-19','156/1','Helummahara','Delgoda'),('62','708492760V','Hiththetiya Vidana Kankanamalage','Susara','Sajeewanie','H.V.K.S. Sajeewanie','Female','susarasajeewani@70gmail.com','779440270','Music','#','1970-12-14','22','Wanaluwawa South','#'),('63','725041675V','Thennakoon Mudiyanselage','Nishanthi','Thennakoon','T.M.N.D.P. Thennakoon','Female','thennakoonnishanthi49@gmail.com','332247848','Bio Science','Science','1972-01-04','70/G/1','Amuhena','Pepiliyawala'),('64','198955901378','Mapa Mudiyanselage','Gayani','Mapa','M.M.G.K. Mapa','Female','gayanikamalika@gmail.com','779633006','Civic','13 Years','1982-02-28','178/D','Eliet Road','Gall'),('65','887423377V','#','Shanika','Uggalbada','D.S. Uggalbada','Female','dilshanikauggalbada@gmail.com','776121858','13 Years','Dancing','1988-08-29','81/5','Pallegama','Pepiliyawala'),('66','652610080V','Udage Arachchige','Eranda','Gunasekara','U.A.E. Gunasekara','Male','uaegunas@gmail.com','703836960','Mathematics','#','1965-09-17','164/A','Iddamalwaththa','Dompe'),('67','197866502804','Mallika Appuhamilage','Saroja','Prasadinie','M.A.S. Prasadinie','Female','sarojaprasadini@gmail.com','718024606','Art','#','1978-06-13','151','Helummahara','Delgoda'),('68','868241500V','Weerasooriya Arachchi Appuhamilage','Krishani','Weerasooriya','W.A.A.K.S.Weerasooriya','Female','krishanisadamali95@gmail.com','786779975','Economics','Civic','1986-11-19','101/1, Pepiliyawala Road','Karawudeniya','Mandawala'),('69','846463488V','Dissanayaka Mudiyanselage','Nilanthi','Weerasingha','D.M.N.K. Weerasingha','Female','nilanthi.weerasinghe1984@gmail.com','772600862','Buddhism','Sinhala','1984-05-25','1 H','Getakanda Road','Dekatana'),('70','945450746V','Range','Dulari','Samarathunga','R.S.D. Samarathunga','Female','dularisamarathunga@gmail.com','713228356','English','General English','1994-02-14','86/14','Siyane Road','Gampaha'),('71','946030945V','#','Hiruni','Balasooriya','H.M. Balasooriya','Female','maleeshahiruni28@gmail.com','769469038','PTS','#','1994-04-12','324/D, Korala Ima','Malagala','Padukka'),('72','756161717V','Kumarapeli Arachchige','Rasika','Arachchige','R.C.K. Arachchige','Female','rasikac0425@gmail.com','773165700','Sinhala','#','1975-04-25','153/7','Helummahara','Delgoda'),('73','686113418V','Dewanamuni','Priyanka','Senevirathan','D.P.N. Senevirathna','Female','priyankasenevirathna1968@gmail.com','717413409','Dancing','#','1968-04-20','484','Polgaslanda Road','Mandawala'),('74','728312882V','Senarath Wasala Wijethunaga Mudiyanse Ralahamilage Adhikaram Walawuwe','Ajantha','Senarath','S.W.W.M.R.A.W.A. Senarath','Female','ajanthasenarath02@gmail.com','112403903','English','#','1972-11-26','379/B','Delgoda','#'),('75','685770300V','Epa Appuhamilage','Prema','Ranjanie','E.A.P. Ranjanie','Female','premaranjanie.1968@gmail.com','712456762','Geography','#','1968-03-17','192','Giridara','Kapugoda'),('76','876403382V','Wijesekara Vidana Pathiranage','Thanuja','Nadeeshani','W.V.P.T. Nadeeshani','Female','nadeeshanithanuja397@gmail.com','716042907','Science','#','1987-05-19','162/75, Sapumal Uyana, Maharagama','Nedungamuwa','Gampaha'),('77','901330220V','Bandagiriye ','Wimalasara','#','B. Wimalasara','Male','#','707104056','Buddhist Civilization','Buddhism','1990-05-12','Sri Shakyasingharamaya','Pelahela','Dompe'),('78','918452311V','Loku Nishshanka Arachchige','Nayanathara','Nishshanka','L.N.A.N. Nishshanka','Female','nayanatharanissanka@gmail.com','713030148','13 Years','Geography','1991-12-10','172/A/1','Palugama','Dompe'),('79','815261968V','Siththara Arachchige','Pavithra','Piyasena','S.A.P.I. Piyasena','Female','pawithrapiyasena1981@gmail.com','718034085','Science','#','1981-01-26','2023-09-02 00:00:00','Weliweriya West','Weliweriya'),('80','767751079V','Hapu Arachchige','Thamara','Jayasekara','H.A.T. Jayasekara','Female','smudunlahiru@gmail.com','776053830','Psysics','#','1976-10-01','156/1','Mahena ','Mandawala'),('81','735390678V','#','Champika','Ilangakoon','C.W. Illangakoon','Female','champikaillangakoon@gmail.com','703003144','Science','#','1973-02-08','25/1','Liyanegama','Dompe'),('82','197873402230','Edirisingha Arachchige','Randika','Kumudunie','E.A.R. Kumudunie','Female','#','702958804','Chemistry','Science','1978-08-21','138/2 B','Main Street','Hanwella'),('83','881941023V','Mahapatabendige','Roshan','Pradeep','M.R. Pradeep','Male','#','715577014','Science','#','1988-07-12','26/4/A','Siyambalape Waththa','Delgoda'),('84','815671139V','Sirisingha Arachchige','Nirosha','Sirisingha','S.A.N.C. Sirisingha','Female','kmlpadmasiri@gmail.com','712490041','Health','#','1981-03-07','151/A','Palugama','Dompe'),('85','197982503212','Sirisingha Arachchilage','Sannaya','Sobhanie','S.A.S. Sobhanie','Female','#','702846863','PTS','Buddhism','1979-11-20','302/H, Dunmadalagahawaththa','Nakkanamulla','Dompe'),('86','727221204V','Kariyawasam Gamage','Manori','Kariyawasam','K.G.M.P. Kariyawasam','Female','mpriyangikadmv@gmail.com','718088229','English','#','1972-08-09','180/A, School Road','Giridara','Kapugoda');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-26 10:50:50
