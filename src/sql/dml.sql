# semester project sql file

SET FOREIGN_KEY_CHECKS=0;

# Meal plans
insert into mealplans (name) values ("Protein Punch");
insert into mealplans (name) values ("Weight Loss");
insert into mealplans (name) values ("Weight Gain");
insert into mealplans (name) values ("Vegetarian");
insert into mealplans (name) values ("Vegan");
insert into mealplans (name) values ("Pescatarian");
insert into mealplans (name) values ("Dirty Bulk");

# Recipes
insert into recipes (name, calories, ingredients, instructions) values ("Chicken and Rice", 500, "Chicken, Rice, ...", "Season chicken ...");
insert into recipes (name, calories, ingredients, instructions) values ("Steak Bowl", 782, "Steak, Rice, ...", "Season steak ...");
insert into recipes (name, calories, ingredients, instructions) values ("Caesar Salad", 289, "Lettuce, Salt, ...", "Wash Lettuce ...");
insert into recipes (name, calories, ingredients, instructions) values ("Tofu Lasagna", 552, "Tofu, Salt, ...", "Press Tofu ...");
insert into recipes (name, calories, ingredients, instructions) values ("Strawberry Shake", 400, "Strawberry, Milk, ...", "Wash Strawberry ...");
insert into recipes (name, calories, ingredients, instructions) values ("Salmon Bake", 452, "Salmon, Salt, ...", "Cook Salmon ...");
insert into recipes (name, calories, ingredients, instructions) values ("Big Mac", 899, "Beef, Sauce, ...", "Cook Patty ...");
insert into recipes (name, calories, ingredients, instructions) values ("Perfect Grilled Skirt Steak Recipe", 584, "1/4 cup canola oil 1/4 cup Meat Seasoning* 2 tablespoons garlic, chopped 2 tablespoons lemon juice, fresh 2 pounds skirt steak, trimmed", "Season steak ...");
insert into recipes (name, calories, ingredients, instructions) values ("Roasted Corn & Shiitake Mushrooms", 228, "2 tablespoons reduced-sodium soy sauce 3 scallions, minced 4 cups sliced shiitake mushroom caps 3 tablespoons Shao Hsing (or Shaoxing) or dry sherry (see Note) 3 cups fresh corn kernels (about 3 large ears; see Tip) or frozen 2 tablespoons canola oil, divided", "Roast mushrooms ...");
insert into recipes (name, calories, ingredients, instructions) values ("Pesto Pasta Soup", 255, "2 Tablespoons olive oil 1 medium onion, chopped 2 cloves garlic, minced 2 Cups carrot, chopped 1 Cup celery, chopped 6 Cups chicken stock or broth 2 Cups dried medium shell pasta 6 Tablespoons basil pesto Parmigiano-Reggiano cheese, shredded (optional)", "Chop celery ...");
insert into recipes (name, calories, ingredients, instructions) values ("BBQ Pulled Pork Enchiladas", 1000, "5 pound pork shoulder roast (bone-in recommended) 18 ounces homemade or store-bought barbecue sauce 6 flour tortillas 8 ounces cheddar or jack cheese (i used a combination of both), grated 6 ounces homemade or store-bought barbecue sauce", "Roast Pork ...");

#mealplanRecipes
insert into mealplanRecipes (recipe_id, mealplan_id) values (1,1);
insert into mealplanRecipes (recipe_id, mealplan_id) values (1,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (1,5);
insert into mealplanRecipes (recipe_id, mealplan_id) values (2,3);
insert into mealplanRecipes (recipe_id, mealplan_id) values (2,4);
insert into mealplanRecipes (recipe_id, mealplan_id) values (3,6);
insert into mealplanRecipes (recipe_id, mealplan_id) values (3,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (3,5);
insert into mealplanRecipes (recipe_id, mealplan_id) values (3,7);
insert into mealplanRecipes (recipe_id, mealplan_id) values (4,3);
insert into mealplanRecipes (recipe_id, mealplan_id) values (4,4);
insert into mealplanRecipes (recipe_id, mealplan_id) values (4,5);
insert into mealplanRecipes (recipe_id, mealplan_id) values (5,3);
insert into mealplanRecipes (recipe_id, mealplan_id) values (5,4);
insert into mealplanRecipes (recipe_id, mealplan_id) values (6,3);
insert into mealplanRecipes (recipe_id, mealplan_id) values (6,6);
insert into mealplanRecipes (recipe_id, mealplan_id) values (7,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (7,5);
insert into mealplanRecipes (recipe_id, mealplan_id) values (7,7);
insert into mealplanRecipes (recipe_id, mealplan_id) values (8,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (9,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (9,4);
insert into mealplanRecipes (recipe_id, mealplan_id) values (9,5);
insert into mealplanRecipes (recipe_id, mealplan_id) values (9,6);
insert into mealplanRecipes (recipe_id, mealplan_id) values (10,2);
insert into mealplanRecipes (recipe_id, mealplan_id) values (11,3);
insert into mealplanRecipes (recipe_id, mealplan_id) values (11,7);

# Goals
insert into goals (name, description) values ("Weight Loss", "Lose 20lbs healthily in 6 months");
insert into goals (name, description) values ("Weight Gain", "Gain Healthy 20lbs in 6 months");
insert into goals (name, description) values ("Maintain Weight", "Maintain within 5lbs for 6 months");
insert into goals (name, description) values ("Vegetarianism", "Have vegetarian diet");
insert into goals (name, description) values ("Dirty Bulk", "Gain weight fast");
insert into goals (name, description) values ("Eat Healthier", "Eat more organic foods");

# Users
insert into users (username, password, about_me, mealplan_id, goal_id) values ("dellimorez", "password1", "Co-creator of this database!", 1, 6);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("thomasgj", "password2", "I am a gnome", 7, 5);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("narayanans", "password3", "Big boy on tha block", 3, 2);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("StarNova", "WompWomp205!", "Allergic to bees but ready to partee!", 2, 1);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("SuhasNar", "LeanMch1ne", "Gym rat, love to cook, and cat dad <3", 1, 3);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("x_swag_x", "D4rkn3ss", "Leave me alone, dont talk to me, no one understands", 3, 2);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("TaylorZa", "Icantthink1!", "I love my family!", 7, 6);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("SwagMan9", "Meow128312", "Yo wut up!", 2, 7);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("Brorher2", "Bark1298", "I'm that dawg", 4, 4);
insert into users (username, password, about_me, mealplan_id, goal_id) values ("Groudon3", "Earthquake1", "Fish stink!", 5, 5);