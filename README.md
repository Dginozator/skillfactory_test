# skillfactory_test

It's test with course structure parsing.

## Environment

* ubuntu-18.04.3-live-server-amd64  
* python 3.6.8, lib pymysql  
* MariaDB 10.1.41 

## Description

This script does next steps:  
1. Load data from http://analytics.skillfactory.ru:5000/api/v1.0/get_structure_course/ with POST request.
2. Rewrite gained data to MySQL database.
