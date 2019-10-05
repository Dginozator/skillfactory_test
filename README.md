# skillfactory_test

It's test with course structure parsing.

## Environment

* ubuntu-18.04.3-live-server-amd64  
* python 3.7.1, lib pymysql  
* MariaDB 10.4.8 

## Description

This script does next steps:  
1. Load data from http://analytics.skillfactory.ru:5000/api/v1.0/get_structure_course/ with POST request.
2. Print in console and save data to `struct.txt` file.
3. Rewrite gained data to MySQL database.
