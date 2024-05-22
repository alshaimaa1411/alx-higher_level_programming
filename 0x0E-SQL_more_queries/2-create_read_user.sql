-- NEW USER AND DATABASE
CREATE USER 'user_0d_2'@'localhost' IDENTITY BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT PRIVILEGE ON hbtn_0d_2 TO 'user_0d_2'@'localhost';