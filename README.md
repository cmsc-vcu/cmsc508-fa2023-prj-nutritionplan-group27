# Welcome to Semester Project repository

## Team Members
* Jeffi Thomas
* Zachariah Dellimore
* Suhas Narayanan

## Title
Nutrition Database - CMSC 508 Semester Project

## Overview
This project creates a Nutritional Database and an API to connect to it. It contains information regarding all the reports for our project progress as well as all the code used to create it.

## Folder Structure
- reports: contains the quarto and html files of our reports
- src: contains all of the code that builds our API
    - api: contains the code that runs the server and sends data to the server
        - routes: contains the routes that the server uses to establish multiple endpoints
    - sql: contains the dml and ddl sql files that, if run, rebuild the database from scratch

## How to run/build this project
To create the server to run the API go to the src/api folder and run server.py. Detailed instructions on how to run the server are there.

To view our reports on making the project go to the reports folder and either run the quarto files or open the premade html files to view our progress.

## How to use this project
This project is intended to document the entire process of making out nutrition database as well as serve as a way for users to run their own API service and connect to the database. Opening the report htmls will show how our ideas have evolved overtime and examples of our API.