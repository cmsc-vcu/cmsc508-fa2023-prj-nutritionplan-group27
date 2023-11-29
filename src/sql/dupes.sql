DROP TABLE IF EXISTS test_duplicates;

CREATE TABLE test_duplicates (
    ID INT AUTO_INCREMENT NOT NULL,
    recipe_id int NOT NULL,
    mealplan_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id),
    FOREIGN KEY (mealplan_id) REFERENCES mealplans(id)
);

-- Insert distinct values into the new table
INSERT INTO test_duplicates (recipe_id, mealplan_id)
SELECT DISTINCT recipe_id, mealplan_id
FROM mealplanRecipes;

DROP TABLE mealplanRecipes;
ALTER TABLE test_duplicates RENAME TO mealplanRecipes;
