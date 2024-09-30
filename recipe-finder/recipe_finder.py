import requests

# Step 1: Set up my API key
api_key = "your_api_key_here"

# Step 2: Get recipe details by entering ingredients
ingredients = input("Enter ingredients (comma-separated): ")
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}"

# Step 3: Fetch recipes
response = requests.get(url)

if response.status_code == 200:
    recipes = response.json()

    if recipes:
        print("Recipes found:")
        print("____________")
        for recipe in recipes:
            print(f"Title: {recipe['title']}, ID: {recipe['id']}")
            print("-" * 40)

        # Step 4: Get recipe ID from the user
        recipe_id = input("Enter the ID of the recipe you want to get more details: ")

        # Step 5: Fetch detailed recipe information using the recipe ID
        detail_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
        detail_response = requests.get(detail_url)

        if detail_response.status_code == 200:
            recipe_details = detail_response.json()

            # Fetch available data
            title = recipe_details.get("title", "No title available.")
            image = recipe_details.get("image", "No image available.")
            servings = recipe_details.get("servings", "No servings information available.")
            instructions = recipe_details.get("instructions", "No instructions available.")

            # Print available details
            print(f"\nTitle: {title}")
            print(f"Image URL: {image}")
            print(f"Servings: {servings}")
            print(f"Instructions: {instructions if instructions else 'No instructions available.'}")
        else:
            print(f"Failed to get details for Recipe id {recipe_id}. Status code: {detail_response.status_code}")
    else:
        print("No recipes found for the given ingredients.")
else:
    print(f"Failed to reach the URL. Status code: {response.status_code}")