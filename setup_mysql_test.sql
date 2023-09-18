-- script that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Granting permmission  to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.*
TO 'hbnb_test'@'localhost';

GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';
