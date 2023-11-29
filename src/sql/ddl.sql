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

insert into users (username, password) values ("dellimorez", "password1");
insert into users (username, password) values ("thomasgj", "password2");
insert into users (username, password) values ("narayanans", "password3");

CREATE TABLE mealplans (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    PRIMARY KEY (id)
);

insert into mealplans (name) values ("Protein Punch");
insert into mealplans (name) values ("Weight Loss");
insert into mealplans (name) values ("Weight Gain");
insert into mealplans (name) values ("Vegetarian");
insert into mealplans (name) values ("Vegan");
insert into mealplans (name) values ("Pescatarian");
insert into mealplans (name) values ("Dirty Bulk");

CREATE TABLE recipes (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(256) NOT NULL,
    nutrition varchar(50) NOT NULL,
    ingredients varchar(4096) NOT NULL,
    instructions varchar(4096) NOT NULL,
    PRIMARY KEY (id)
);

insert into recipes (name, nutrition, ingredients, instructions) values ("Chicken and Rice", "500cal", "Chicken, Rice, ...", "Season chicken ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Steak Bowl", "782cal", "Steak, Rice, ...", "Season steak ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Caesar Salad", "289cal", "Lettuce, Salt, ...", "Wash Lettuce ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Tofu Lasagna", "5052cal", "Tofu, Salt, ...", "Press Tofu ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Strawberry Shake", "400cal", "Strawberry, Milk, ...", "Wash Strawberry ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Salmon Bake", "452cal", "Salmon, Salt, ...", "Cook Salmon ...");
insert into recipes (name, nutrition, ingredients, instructions) values ("Big Mac", "899cal", "Beef, Sauce, ...", "Cook Patty ...");

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

insert into goals (name, description) values ("Weight Loss", "Lose 20lbs healthily in 6 months");
insert into goals (name, description) values ("Weight Gain", "Gain Healthy 20lbs in 6 months");
insert into goals (name, description) values ("Maintain Weight", "Maintain within 5lbs for 6 months");
insert into goals (name, description) values ("Vegetarianism", "Have vegetarian diet");
insert into goals (name, description) values ("Dirty Bulk", "Gain weight fast");
insert into goals (name, description) values ("Eat Healthier", "Eat more organic foods");