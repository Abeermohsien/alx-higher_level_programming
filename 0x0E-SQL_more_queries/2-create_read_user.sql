-- Create the database.
CREATE DATABASE IF NOT EXISTS user_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT SELECT ON 'user_0d_2'.*  TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
