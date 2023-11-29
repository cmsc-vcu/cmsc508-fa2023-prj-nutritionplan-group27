# semester project sql file

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS mealplans;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS mealplanRecipes;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(256) NOT NULL,
    password varchar(256) NOT NULL,
    mealplan_id int,
    PRIMARY KEY (id)
);

CREATE TABLE mealplans (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE recipes (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    nutrition varchar(50) NOT NULL,
    ingredients varchar(4096) NOT NULL,
    instructions varchar(4096) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE mealplanRecipes (
    id int NOT NULL AUTO_INCREMENT,
    recipe_id int NOT NULL,
    mealplan_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id),
    FOREIGN KEY (mealplan_id) REFERENCES mealplans(id)
);

CREATE TABLE goals (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    description varchar(2048) NOT NULL,
    PRIMARY KEY (id)
);