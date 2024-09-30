import requests

# Step 1: Set up API key and URL
api_key = “YourAPIkey”

# Step 2: Get ingredients from the User
ingredients = input("Enter the ingredients you have (separated by commas): ")

# Step 3: fetch recipe suggestions based on ingredients
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}"
response = requests.get(url)

# Step 4: Check the request was successful
if response.status_code == 200:
  recipes = response.json()

  # Step 5: Display recipe titles and ids
  if recipes:
    for recipe in recipes:
      print(f"Recipe Title: {recipe['title']}")
      print(f"Recipe ID: {recipe['id']}")
      print("--------------------")

  else:
    print("No recipes found.")

   # Ask for the user to choose a recipe
  recipe_id = input("Enter the ID of the recipe you want to get more details: ")

   # Step 6: fetch recipe information using recipe id
  detail_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
  detail_response = requests.get(url)

  if  detail_response.status_code == 200:
    # parse the JSON response
     recipe_details = detail_response.json()


    # Display recipe information
     amount = recipe_details.get("amount", "No amount available.")
     cooking_time = recipe_details.get("readyInMinutes", "No cooking time available.")
     servings = recipe_details.get("servings", "No servings available.")

   #   Display the recipe details
     print(recipe_details)
     print("cooking time: {cooking_time} minutes")
     print("servings: {servings}")
     print("instructions: {instructions}")
else: 
    print("failed to get details for recipe id {recipe_id}. status code: {detail_response.status_code}")
