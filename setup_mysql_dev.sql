-- script that prepares a MySQL server for the AirBnB_clone_v2 project
-- database: hbnb_dev_db
-- new user: hbnb_dev (in localhost) 
--	privileges: all privileges on the 'hbnb_dev_db' database
-- new user's password: hbnb_dev_pwd

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
