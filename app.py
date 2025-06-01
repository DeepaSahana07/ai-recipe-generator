def get_mock_recipe(cuisine, dietary_pref, ingredients, cooking_time=45, skill_level="Intermediate"):
    """Enhanced AI recipe generation with user customization"""
    
    # Expanded recipe database with multiple options per cuisine
    ENHANCED_RECIPES = {
        "italian": [
            {
                "name": "Creamy Mushroom Risotto",
                "description": "A rich and creamy Italian classic with earthy mushrooms",
                "prep_time": "15 minutes",
                "cook_time": "25 minutes",
                "servings": 4,
                "difficulty": "Medium",
                "ingredients": [
                    "2 cups Arborio rice", "4 cups vegetable broth", "1 lb mixed mushrooms",
                    "1 onion, diced", "3 cloves garlic", "1/2 cup white wine",
                    "1/2 cup parmesan cheese", "2 tbsp butter", "Fresh thyme"
                ],
                "instructions": [
                    "Heat broth in a separate pan and keep warm",
                    "Sauté mushrooms until golden, set aside",
                    "Cook onion and garlic until fragrant",
                    "Add rice and toast for 2 minutes",
                    "Add wine and stir until absorbed",
                    "Add broth one ladle at a time, stirring constantly",
                    "Fold in mushrooms, butter, and parmesan",
                    "Season and serve immediately"
                ],
                "nutrition": {"calories": 380, "protein": "12g", "carbs": "58g", "fat": "8g"},
                "tags": ["vegetarian", "comfort_food", "medium_time"]
            },
            {
                "name": "Classic Spaghetti Carbonara",
                "description": "Traditional Roman pasta with eggs, cheese, and pancetta",
                "prep_time": "10 minutes",
                "cook_time": "15 minutes",
                "servings": 4,
                "difficulty": "Easy",
                "ingredients": [
                    "400g spaghetti", "200g pancetta", "4 large eggs",
                    "100g pecorino romano", "Black pepper", "Salt"
                ],
                "instructions": [
                    "Cook spaghetti in salted boiling water",
                    "Crisp pancetta in a large pan",
                    "Whisk eggs with grated cheese and pepper",
                    "Drain pasta, reserve pasta water",
                    "Toss hot pasta with pancetta",
                    "Remove from heat, add egg mixture",
                    "Toss quickly, adding pasta water if needed",
                    "Serve immediately with extra cheese"
                ],
                "nutrition": {"calories": 520, "protein": "24g", "carbs": "62g", "fat": "18g"},
                "tags": ["quick", "classic", "low_time"]
            },
            {
                "name": "Margherita Pizza",
                "description": "Simple and fresh pizza with tomatoes, mozzarella, and basil",
                "prep_time": "20 minutes",
                "cook_time": "12 minutes",
                "servings": 2,
                "difficulty": "Medium",
                "ingredients": [
                    "Pizza dough", "400g canned tomatoes", "250g fresh mozzarella",
                    "Fresh basil leaves", "Olive oil", "Salt", "Garlic"
                ],
                "instructions": [
                    "Preheat oven to 475°F (245°C)",
                    "Roll out pizza dough",
                    "Crush tomatoes with salt and garlic",
                    "Spread sauce on dough",
                    "Tear mozzarella into pieces and distribute",
                    "Drizzle with olive oil",
                    "Bake for 10-12 minutes until crispy",
                    "Top with fresh basil before serving"
                ],
                "nutrition": {"calories": 450, "protein": "18g", "carbs": "55g", "fat": "16g"},
                "tags": ["vegetarian", "classic", "medium_time"]
            }
        ],
        "indian": [
            {
                "name": "Butter Chicken Curry",
                "description": "Creamy tomato-based curry with tender chicken pieces",
                "prep_time": "20 minutes",
                "cook_time": "30 minutes",
                "servings": 4,
                "difficulty": "Medium",
                "ingredients": [
                    "1 lb chicken breast, cubed", "1 can tomato sauce", "1/2 cup heavy cream",
                    "1 onion, sliced", "3 cloves garlic", "1 inch ginger",
                    "2 tsp garam masala", "1 tsp turmeric", "Salt to taste", "Fresh cilantro"
                ],
                "instructions": [
                    "Marinate chicken with yogurt and spices for 15 minutes",
                    "Cook chicken until golden, set aside",
                    "Sauté onions until caramelized",
                    "Add garlic, ginger, and spices",
                    "Add tomato sauce and simmer",
                    "Return chicken to pan",
                    "Stir in cream and simmer until thick",
                    "Garnish with cilantro and serve with rice"
                ],
                "nutrition": {"calories": 420, "protein": "28g", "carbs": "12g", "fat": "18g"},
                "tags": ["curry", "medium_time", "spicy"]
            },
            {
                "name": "Vegetable Biryani",
                "description": "Fragrant basmati rice with mixed vegetables and aromatic spices",
                "prep_time": "25 minutes",
                "cook_time": "35 minutes",
                "servings": 6,
                "difficulty": "Medium",
                "ingredients": [
                    "2 cups basmati rice", "Mixed vegetables", "1 large onion",
                    "Biryani masala", "Saffron", "Mint leaves", "Fried onions",
                    "Yogurt", "Ghee", "Whole spices"
                ],
                "instructions": [
                    "Soak rice for 30 minutes",
                    "Sauté vegetables with spices",
                    "Cook rice with whole spices until 70% done",
                    "Layer rice and vegetables",
                    "Sprinkle saffron milk and fried onions",
                    "Cover and cook on dum for 45 minutes",
                    "Let it rest for 10 minutes",
                    "Serve with raita and pickle"
                ],
                "nutrition": {"calories": 380, "protein": "8g", "carbs": "72g", "fat": "12g"},
                "tags": ["vegetarian", "aromatic", "high_time"]
            },
            {
                "name": "Quick Dal Tadka",
                "description": "Simple lentil curry with aromatic tempering",
                "prep_time": "10 minutes",
                "cook_time": "20 minutes",
                "servings": 4,
                "difficulty": "Easy",
                "ingredients": [
                    "1 cup yellow lentils", "1 onion", "2 tomatoes", "Ginger-garlic paste",
                    "Turmeric", "Cumin seeds", "Mustard seeds", "Curry leaves",
                    "Green chilies", "Cilantro", "Ghee"
                ],
                "instructions": [
                    "Wash and cook lentils with turmeric",
                    "Heat ghee for tempering",
                    "Add cumin and mustard seeds",
                    "Add curry leaves and green chilies",
                    "Sauté onions until golden",
                    "Add ginger-garlic paste and tomatoes",
                    "Pour tempering over cooked dal",
                    "Garnish with cilantro and serve"
                ],
                "nutrition": {"calories": 220, "protein": "12g", "carbs": "35g", "fat": "6g"},
                "tags": ["vegetarian", "healthy", "low_time", "vegan_adaptable"]
            }
        ],
        "mexican": [
            {
                "name": "Spicy Black Bean Tacos",
                "description": "Flavorful vegetarian tacos with seasoned black beans",
                "prep_time": "10 minutes",
                "cook_time": "15 minutes",
                "servings": 4,
                "difficulty": "Easy",
                "ingredients": [
                    "2 cans black beans", "8 corn tortillas", "1 avocado",
                    "1 lime", "1 red onion", "2 tomatoes", "1 jalapeño",
                    "Cumin", "Chili powder", "Fresh cilantro", "Mexican cheese"
                ],
                "instructions": [
                    "Drain and rinse black beans",
                    "Heat beans with cumin and chili powder",
                    "Warm tortillas in a dry pan",
                    "Dice tomatoes, onion, and jalapeño",
                    "Mash avocado with lime juice",
                    "Assemble tacos with beans and toppings",
                    "Sprinkle with cheese and cilantro",
                    "Serve with lime wedges"
                ],
                "nutrition": {"calories": 320, "protein": "14g", "carbs": "52g", "fat": "8g"},
                "tags": ["vegetarian", "quick", "low_time"]
            },
            {
                "name": "Chicken Fajitas",
                "description": "Sizzling chicken with peppers and onions",
                "prep_time": "15 minutes",
                "cook_time": "12 minutes",
                "servings": 4,
                "difficulty": "Easy",
                "ingredients": [
                    "1 lb chicken strips", "2 bell peppers", "1 large onion",
                    "Fajita seasoning", "Flour tortillas", "Sour cream",
                    "Guacamole", "Salsa", "Cheese", "Lime"
                ],
                "instructions": [
                    "Season chicken with fajita spices",
                    "Heat oil in a large skillet",
                    "Cook chicken until golden",
                    "Add sliced peppers and onions",
                    "Cook until vegetables are tender-crisp",
                    "Warm tortillas",
                    "Serve with toppings",
                    "Squeeze lime over everything"
                ],
                "nutrition": {"calories": 410, "protein": "32g", "carbs": "28g", "fat": "18g"},
                "tags": ["quick", "low_time", "protein_rich"]
            }
        ]
    }
    
    # Get recipes for the selected cuisine
    available_recipes = ENHANCED_RECIPES.get(cuisine.lower(), ENHANCED_RECIPES["italian"])
    
    # Filter recipes based on user preferences
    filtered_recipes = []
    
    for recipe in available_recipes:
        # Check dietary preferences
        if dietary_pref == "Vegetarian" and "vegetarian" not in recipe.get("tags", []):
            continue
        elif dietary_pref == "Vegan" and "vegan" not in recipe.get("tags", []) and "vegan_adaptable" not in recipe.get("tags", []):
            continue
        
        # Check cooking time
        total_time = int(recipe['prep_time'].split()[0]) + int(recipe['cook_time'].split()[0])
        if total_time > cooking_time:
            continue
            
        # Check skill level
        recipe_difficulty = recipe['difficulty'].lower()
        if skill_level == "Beginner" and recipe_difficulty == "advanced":
            continue
        elif skill_level == "Intermediate" and recipe_difficulty == "advanced":
            continue
            
        filtered_recipes.append(recipe)
    
    # If no recipes match criteria, relax constraints
    if not filtered_recipes:
        filtered_recipes = available_recipes
    
    # Select a recipe
    selected_recipe = random.choice(filtered_recipes)
    
    # Customize based on available ingredients
    if ingredients.strip():
        user_ingredients = [ing.strip().lower() for ing in ingredients.split(',')]
        customized_recipe = customize_recipe_with_ingredients(selected_recipe, user_ingredients, dietary_pref)
        return customized_recipe
    
    # Apply dietary modifications
    if dietary_pref == "Vegan":
        selected_recipe = make_vegan_adaptations(selected_recipe)
    elif dietary_pref == "Gluten-Free":
        selected_recipe = make_gluten_free_adaptations(selected_recipe)
    
    return selected_recipe

def customize_recipe_with_ingredients(recipe, user_ingredients, dietary_pref):
    """Customize recipe based on user's available ingredients"""
    customized = recipe.copy()
    
    # Simple ingredient matching and suggestions
    recipe_ingredients = [ing.lower() for ing in recipe['ingredients']]
    matched_ingredients = []
    
    for user_ing in user_ingredients:
        for recipe_ing in recipe_ingredients:
            if user_ing in recipe_ing or recipe_ing.split()[0] in user_ing:
                matched_ingredients.append(recipe_ing)
    
    if matched_ingredients:
        customized['description'] += f" (Using your ingredients: {', '.join(matched_ingredients[:3])})"
    
    return customized

def make_vegan_adaptations(recipe):
    """Make vegan adaptations to a recipe"""
    adapted = recipe.copy()
    adapted['name'] = f"Vegan {recipe['name']}"
    
    # Replace common non-vegan ingredients
    new_ingredients = []
    for ingredient in recipe['ingredients']:
        ingredient_lower = ingredient.lower()
        if 'butter' in ingredient_lower:
            new_ingredients.append(ingredient.replace('butter', 'vegan butter').replace('Butter', 'Vegan butter'))
        elif 'cheese' in ingredient_lower:
            new_ingredients.append(ingredient.replace('cheese', 'nutritional yeast').replace('Cheese', 'Nutritional yeast'))
        elif 'cream' in ingredient_lower:
            new_ingredients.append(ingredient.replace('cream', 'coconut cream').replace('Cream', 'Coconut cream'))
        elif 'milk' in ingredient_lower:
            new_ingredients.append(ingredient.replace('milk', 'almond milk').replace('Milk', 'Almond milk'))
        elif any(meat in ingredient_lower for meat in ['chicken', 'beef', 'pork', 'fish']):
            new_ingredients.append('Plant-based protein (tofu/tempeh)')
        else:
            new_ingredients.append(ingredient)
    
    adapted['ingredients'] = new_ingredients
    adapted['description'] += " (Vegan version)"
    return adapted

def make_gluten_free_adaptations(recipe):
    """Make gluten-free adaptations to a recipe"""
    adapted = recipe.copy()
    adapted['name'] = f"Gluten-Free {recipe['name']}"
    
    # Replace gluten-containing ingredients
    new_ingredients = []
    for ingredient in recipe['ingredients']:
        ingredient_lower = ingredient.lower()
        if 'flour' in ingredient_lower:
            new_ingredients.append(ingredient.replace('flour', 'gluten-free flour').replace('Flour', 'Gluten-free flour'))
        elif 'pasta' in ingredient_lower or 'spaghetti' in ingredient_lower:
            new_ingredients.append('Gluten-free pasta')
        elif 'bread' in ingredient_lower:
            new_ingredients.append('Gluten-free bread')
        else:
            new_ingredients.append(ingredient)
    
    adapted['ingredients'] = new_ingredients
    adapted['description'] += " (Gluten-free version)"
    return adapted
