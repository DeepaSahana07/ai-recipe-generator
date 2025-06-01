import streamlit as st
import json
import random
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🍳 AI Recipe Generator",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for attractive UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #ff6b6b, #ffd93d, #6bcf7f);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .recipe-card {
        background: linear-gradient(145deg, #f0f8ff, #e6f3ff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #4CAF50;
    }
    
    .ingredient-chip {
        background: linear-gradient(45deg, #ff6b6b, #ffa726);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        display: inline-block;
        font-weight: bold;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .step-number {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border-radius: 50%;
        width: 30px;
        height: 30px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 10px;
    }
    
    .nutrition-badge {
        background: linear-gradient(45deg, #9c27b0, #e91e63);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.9rem;
        margin: 0.2rem;
        display: inline-block;
    }
    
    .sidebar-header {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Mock recipe database (simulating AI responses)
MOCK_RECIPES = {
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
            "nutrition": {"calories": 380, "protein": "12g", "carbs": "58g", "fat": "8g"}
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
            "nutrition": {"calories": 420, "protein": "28g", "carbs": "12g", "fat": "18g"}
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
            "nutrition": {"calories": 320, "protein": "14g", "carbs": "52g", "fat": "8g"}
        }
    ]
}

def get_mock_recipe(cuisine, dietary_pref, ingredients):
    """Simulate AI recipe generation"""
    available_recipes = MOCK_RECIPES.get(cuisine.lower(), MOCK_RECIPES["italian"])
    base_recipe = random.choice(available_recipes)
    
    # Modify recipe based on preferences
    if dietary_pref == "Vegetarian" and "chicken" in base_recipe["name"].lower():
        base_recipe["name"] = base_recipe["name"].replace("Chicken", "Vegetable")
        base_recipe["ingredients"] = [ing for ing in base_recipe["ingredients"] if "chicken" not in ing.lower()]
    
    return base_recipe

def main():
    # Header
    st.markdown('<div class="main-header">🍳 AI Recipe Generator</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-header"><h2>🎯 Recipe Preferences</h2></div>', unsafe_allow_html=True)
        
        # User inputs
        cuisine = st.selectbox(
            "🌍 Choose Cuisine:",
            ["Italian", "Indian", "Mexican", "Chinese", "American", "Mediterranean", "Thai", "French"]
        )
        
        dietary_pref = st.selectbox(
            "🥗 Dietary Preference:",
            ["No Preference", "Vegetarian", "Vegan", "Gluten-Free", "Keto", "Low-Carb"]
        )
        
        cooking_time = st.slider("⏱️ Max Cooking Time (minutes):", 15, 120, 45)
        
        skill_level = st.selectbox(
            "👨‍🍳 Skill Level:",
            ["Beginner", "Intermediate", "Advanced"]
        )
        
        ingredients = st.text_area(
            "🥕 Available Ingredients (optional):",
            placeholder="tomatoes, onions, garlic, chicken..."
        )
        
        generate_btn = st.button("✨ Generate Recipe", type="primary", use_container_width=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if generate_btn or 'current_recipe' not in st.session_state:
            with st.spinner("🤖 AI is crafting your perfect recipe..."):
                # Simulate API call delay
                import time
                time.sleep(2)
                
                # Generate recipe
                recipe = get_mock_recipe(cuisine, dietary_pref, ingredients)
                st.session_state.current_recipe = recipe
        
        if 'current_recipe' in st.session_state:
            recipe = st.session_state.current_recipe
            
            # Recipe display
            st.markdown('<div class="recipe-card">', unsafe_allow_html=True)
            
            # Recipe header
            col_name, col_time = st.columns([3, 1])
            with col_name:
                st.markdown(f"## 🍽️ {recipe['name']}")
                st.markdown(f"*{recipe['description']}*")
            
            with col_time:
                st.metric("⏱️ Total Time", f"{int(recipe['prep_time'].split()[0]) + int(recipe['cook_time'].split()[0])} min")
                st.metric("👥 Servings", recipe['servings'])
            
            # Recipe details
            detail_col1, detail_col2, detail_col3 = st.columns(3)
            with detail_col1:
                st.info(f"📝 **Prep:** {recipe['prep_time']}")
            with detail_col2:
                st.info(f"🔥 **Cook:** {recipe['cook_time']}")
            with detail_col3:
                st.info(f"📊 **Level:** {recipe['difficulty']}")
            
            st.markdown("---")
            
            # Ingredients section
            st.markdown("### 🛒 Ingredients")
            ingredients_html = ""
            for ingredient in recipe['ingredients']:
                ingredients_html += f'<span class="ingredient-chip">{ingredient}</span> '
            st.markdown(ingredients_html, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Instructions section
            st.markdown("### 👨‍🍳 Instructions")
            for i, instruction in enumerate(recipe['instructions'], 1):
                st.markdown(
                    f'<div style="display: flex; align-items: center; margin: 1rem 0;">'
                    f'<span class="step-number">{i}</span>'
                    f'<span style="flex: 1;">{instruction}</span></div>',
                    unsafe_allow_html=True
                )
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Nutrition information
        if 'current_recipe' in st.session_state:
            recipe = st.session_state.current_recipe
            
            st.markdown("### 📊 Nutrition Facts")
            nutrition = recipe['nutrition']
            
            # Create nutrition badges
            nutrition_html = f"""
            <div style="text-align: center;">
                <span class="nutrition-badge">🔥 {nutrition['calories']} cal</span><br>
                <span class="nutrition-badge">🥩 {nutrition['protein']}</span><br>
                <span class="nutrition-badge">🍞 {nutrition['carbs']}</span><br>
                <span class="nutrition-badge">🥑 {nutrition['fat']}</span>
            </div>
            """
            st.markdown(nutrition_html, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Action buttons
            st.markdown("### 💾 Save & Share")
            
            if st.button("❤️ Save to Favorites", use_container_width=True):
                st.success("Recipe saved to favorites!")
            
            if st.button("📱 Share Recipe", use_container_width=True):
                st.info("Share link copied to clipboard!")
            
            if st.button("🛒 Add to Shopping List", use_container_width=True):
                st.success("Ingredients added to shopping list!")
        
        # Tips section
        st.markdown("---")
        st.markdown("### 💡 Pro Tips")
        tips = [
            "🧂 Always taste and adjust seasoning",
            "🔥 Preheat your pan before cooking",
            "🥘 Use fresh herbs when possible",
            "⏰ Read the entire recipe first",
            "🧊 Keep ingredients at room temperature"
        ]
        
        for tip in tips:
            st.markdown(f"• {tip}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: gray; padding: 1rem;">'
        '🤖 Powered by AI • Made with ❤️ using Streamlit<br>'
        f'Generated on {datetime.now().strftime("%B %d, %Y at %I:%M %p")}'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()