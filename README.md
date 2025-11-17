# Project Overview
You are given a large, denormalized JSON file in data/ containing property-related information:

Property details

HOA information

Rehab estimates

Valuations

Rent estimates

Misc attributes

These fields are mixed together, lacking relational structure.
# Goal
Normalize the raw JSON property dataset into a clean relational MySQL schema.

Design and create SQL tables with proper primary keys, foreign keys, and relationships.

Build a Python ETL pipeline to extract, clean, transform, and load the data into MySQL.

Ensure full reproducibility using proper documentation, error handling, and dependency management.

# ETL Workflow
Extract:
Load the raw JSON file from the data/ directory and parse all property records.

Validate & Clean:
Use Pydantic models to validate fields, fix invalid/missing values, and standardize formats.

Transform:
Split each record into normalized components (property details, HOA, valuations, rehab, etc.) based on the Field Config.

Load to MySQL:
Insert cleaned data into normalized tables using foreign keys for relationships.

Logging & Error Handling:
Log every step (info/errors) and skip invalid records without breaking the pipeline.

# Database Setup (Without Docker)
Installed MySQL 8.0 locally on Windows using the official MySQL Installer.

Created database & user using SQL commands (home_db, db_user, 6equj5_db_user).

Imported schema using:

USE home_db;
SOURCE path/to/schema.sql;


Updated ETL script to connect to local MySQL at localhost:3306.

# How to Reproduce
# 1.Install MySQL 8.0 locally
Download MySQL Installer → Install MySQL Server & Workbench → Set root password.

# 2.Create database and user
Run these commands in MySQL:

CREATE DATABASE home_db;

CREATE USER 'db_user'@'localhost' IDENTIFIED BY '6equj5_db_user';

GRANT ALL PRIVILEGES ON home_db.* TO 'db_user'@'localhost';

FLUSH PRIVILEGES;


# Import the provided schema
Open MySQL shell and run:

# USE home_db;
SOURCE E:/data_engineer_assessment/schema.sql;


# Install Python dependencies
In your project folder:

pip install -r requirements.txt


# Run the ETL script
Execute the ETL:

python src/etl.py


# Verify loaded data
In MySQL:

USE home_db;
SELECT COUNT(*) FROM properties;
