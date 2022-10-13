-- creates database `hbnb_test_db`
-- creates a new user 'hbnb_test' in localhost
--	password: hbnb_test_pwd
--	privileges: all priveleges on 'hbnb_test_db', select privlege on 'performance_schema'.

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
