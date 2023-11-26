import json
import pymysql.cursors
from enum import Enum
import requests
import time

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

def make_parameters(search):
    return {
        "type": "public",
        "q": search,
        "app_id": app_id,
        "app_key": app_key
    }

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

url = "https://api.edamam.com/api/recipes/v2"
app_key = "a4c54dab3f9f31f1eb0c8a037c8b187e"
app_id = "38724b7d"

params = [
    make_parameters("Chicken"),
    make_parameters("Steak"),
    make_parameters("Vegetarian"),
    make_parameters("Vegan"),
    make_parameters("Pescatarian"),
    make_parameters("Pork"),
    make_parameters("Cake"),
    make_parameters("Soup"),
    make_parameters("Mushroom")
    ]



# Create array of recipe data
recipes = []

count = 0

for param in params:
    print(param)
    
    while (url is not None) and (count < 100):
        res = requests.get(url, params=param)
        
        if res.status_code == 200:
            json_data = res.json()
            
            for hits in json_data["hits"]:
                data = recipe_data() # Creates recipe_data class
                data.name = hits["recipe"]["label"] # gets name
                data.ingredients = " ".join([str(item) for item in hits["recipe"]["ingredientLines"]]) # gets all ingredients
                data.instructions = hits['recipe']['url']
                data.nutrition = str( int(hits["recipe"]["calories"] / hits["recipe"]["yield"]) ) # gets calories per serving
                data.protein = hits["recipe"]["totalNutrients"]["PROCNT"]["quantity"] / hits["recipe"]["yield"]
                data.meal_plans = getMealPlans(hits, data)
                # print("{}\n\t{}\n\t\t{}".format(data.name, data.nutrition, data.ingredients)) # prints data
                recipes.append(data) # Add the data to the recipes array
                
            if 'next' in json_data['_links']:
                url = json_data['_links']['next']['href']
            else:
                url = None
            count += 1
            time.sleep(7) # To not go over api limit of 10 per minute
        else:
            url = None
            
    with cnx:
        with cnx.cursor() as cursor:
            for recipe in recipes:
                sql = "INSERT INTO `recipes` (`name`, `nutrition`, `ingredients`, `instructions`) VALUES (%s, %s, %s, %s)"
                ingredients = recipe.ingredients
                if len(ingredients) >= 4095:
                    ingredients = ingredients[0:4094]
                cursor.execute(sql, (recipe.name, recipe.nutrition, ingredients, recipe.instructions))
                sql = "SELECT `id` FROM `recipes` WHERE `name`=%s"
                cursor.execute(sql, (recipe.name))
                result = cursor.fetchone()
                recipe_id = result["id"]
                sql = "INSERT INTO `mealplanRecipes` (`recipe_id`, `mealplan_id`) VALUES (%s, %s)"
                for mealplan in recipe.meal_plans:
                    cursor.execute(sql, (int(recipe_id), int(mealplan.value)))
            
        cnx.commit()
    
    url = "https://api.edamam.com/api/recipes/v2"
    recipes.clear()
    cnx = pymysql.connect(host=config['host'],
                        user=config['user'],
                        password=config['password'],
                        database=config['database'],
                        cursorclass=pymysql.cursors.DictCursor)
    count = 0