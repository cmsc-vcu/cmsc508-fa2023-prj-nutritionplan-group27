import json
import pymysql.cursors
from enum import Enum

MealPlan = Enum('Goals', ['Protein Punch', 'Weight Loss', 'Weight Gain', 
                          'Vegetarian', 'Vegan', 'Pescatarian', 'Dirty Bulk' ])

class recipe_data:
    name = "",
    nutrition = "",
    ingredients = "",
    instructions = "",
    protein = 0.0,
    meal_plans = []

def getMealPlans(hits, data = recipe_data()):
    meal_plans = []
    calories = hits["recipe"]["calories"] / hits["recipe"]["yield"]
    if(calories <= 600): meal_plans.append(MealPlan['Weight Loss'])
    if(calories > 600): meal_plans.append(MealPlan['Weight Gain'])
    if(data.protein/calories >= 0.25): meal_plans.append(MealPlan['Protein Punch'])
    if("Vegetarian" in hits["recipe"]["healthLabels"]): meal_plans.append(MealPlan['Vegetarian'])
    if("Vegan" in hits["recipe"]["healthLabels"]): meal_plans.append(MealPlan['Vegan'])
    if("Pescatarian" in hits["recipe"]["healthLabels"]): meal_plans.append(MealPlan['Pescatarian'])
    if(calories >= 700): meal_plans.append(MealPlan['Dirty Bulk'])
    
    return meal_plans

config = {
  'user': '23FA_dellimorez',
  'password': 'Shout4_dellimorez_GOME',
  'host': 'cmsc508.com',
  'database': '23FA_groups_group27',
  'raise_on_warnings': True
}

cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)

# Open JSON file
file = open("src/api/json/vegetarian.json")

# Convert JSON file to dictionary
json_data = json.load(file)

# Create array of recipe data
recipes = []

# get recipe data from json
for hits in json_data["hits"]:
    data = recipe_data() # Creates recipe_data class
    data.ingredients = " ".join([str(item) for item in hits["recipe"]["ingredientLines"]]) # gets all ingredients
    data.name = hits["recipe"]["label"] # gets name
    data.nutrition = str( hits["recipe"]["calories"] / hits["recipe"]["yield"] ) # gets calories per serving
    data.protein = hits["recipe"]["totalNutrients"]["PROCNT"]["quantity"] / hits["recipe"]["yield"]
    data.meal_plans = getMealPlans(hits, data)
    for item in data.meal_plans:
        print("{}: {}".format(data.name, item.name))
    recipes.append(data) # Add the data to the recipes array
    # print("{}\n\t{}\n\t\t{}".format(data.name, data.nutrition, data.ingredients)) # prints data

# Connecting to database and inserting the data

with cnx:
    with cnx.cursor() as cursor:
        for recipe in recipes:
            sql = "INSERT INTO `recipes` (`name`, `nutrition`, `ingredients`, `instructions`) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (recipe.name, recipe.nutrition, recipe.ingredients, ""))
            sql = "SELECT `id` FROM `recipes` WHERE `name`=%s"
            cursor.execute(sql, (recipe.name))
            result = cursor.fetchone()
            recipe_id = result["id"]
            sql = "INSERT INTO `mealplanRecipes` (`recipe_id`, `mealplan_id`) VALUES (%s, %s)"
            for mealplan in recipe.meal_plans:
                cursor.execute(sql, (int(recipe_id), int(mealplan.value)))
        
    cnx.commit()

 
# Closing file
file.close()
