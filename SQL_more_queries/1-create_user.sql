-- Check if the user exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') INTO @user_exists;

-- If the user doesn't exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created and granted all privileges.';
ELSE
    SELECT 'User user_0d_1 already exists.';
END IF;
