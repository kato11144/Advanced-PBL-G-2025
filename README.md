# Advanced-PBL-G-2025

This guide provides instructions for setting up the experimental environment using Docker

### <u>Setup Container</u>

Build and Start Container
```sh
docker compose up -d --build
```

Access the Container
```sh
docker compose exec ubuntu /bin/bash
```

### <u>Setup MySQL</u>

#### Start MySQL
```sh
service mysql start
```

#### Run MySQL Secure Installation
```sh
mysql_secure_installation
```

#### During the prompts, enter the following responses
```sh
Would you like to setup VALIDATE PASSWORD component? (Press y|Y for Yes, any other key for No): y

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0

Remove anonymous users? (Press y|Y for Yes, any other key for No): y

Disallow root login remotely? (Press y|Y for Yes, any other key for No): y

Remove test database and access to it? (Press y|Y for Yes, any other key for No): y

Reload privilege tables now? (Press y|Y for Yes, any other key for No): y
```

#### Log in to MySQL
```sh
mysql -u root
```

#### Modify Password Settings
```sql
SET GLOBAL validate_password.length = 4;

SET GLOBAL validate_password.check_user_name = OFF;
```

#### Verify Password Settings
```sql
SHOW VARIABLES LIKE 'validate_password%';
```

#### Create Database and User
```sql
CREATE DATABASE RhoMethod;

CREATE USER 'attacker'@'localhost' IDENTIFIED BY '0000';

GRANT ALL ON RhoMethod.* TO 'attacker'@'localhost';
```

### <u>MySQL Commands</u>
```sql
-- Show all Databases
SHOW DATABASES;

-- Use a Database
USE <Database Name>;

-- Show all Tables
SHOW TABLES;

-- Retrieve all Records
SELECT * FROM <Table Name>;
```

### <u>Clean Up</u>
Stop and Remove Container
```sh
docker compose down
```

Remove the Docker Image
```sh
docker rmi advanced-pbl-g-2025-ubuntu:latest
```
