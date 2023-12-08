# Welcome to Semester Project repository

## Team Members
* Jeffi Thomas
* Zachariah Dellimore
* Suhas Narayanan

## Title
Nutrition Database - CMSC 508 Semester Project

## Overview
This project looks at a Nutritional Database. It contains information regarding all the reports for our project progress.

## Folder Structure
- reports: contains the quarto and html files of our reports
- src: contains all of the code that builds our API
    - api: contains the code that runs the server and sends data to the server
        - routes: contains the routes that the server uses to establish multiple endpoints
    - sql: contains the dml and ddl sql files that, if run, rebuild the database from scratch

## How to run/build this project
To run/build this project run the following command in the folder containing deliver4.qmd
"quarto render deliver4.qmd"
Quarto should then output and html file for your use.
Because this is the only files in the project so far this is all you can build.

## How to use this project
This project is intended to document the entire process of making out nutrition database. Opening the report htmls will show how our ideas have evolved overtime and examples of our API.