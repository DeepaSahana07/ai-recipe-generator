🍳 AI Recipe Generator

A beautiful, interactive web application that generates personalized recipes using AI technology. Built with Streamlit for a seamless user experience.

 ✨ Features

-🌍 Multi-Cuisine Support: Italian, Indian, Mexican, Chinese, American, Mediterranean, Thai, French
-🥗 Dietary Preferences: Vegetarian, Vegan, Gluten-Free, Keto, Low-Carb options
- ⏱️ Time-Based Filtering: Set maximum cooking time based on your schedule
- 👨‍🍳 Skill Level Matching: Recipes tailored to your cooking expertise
- 🛒 Ingredient Integration: Input available ingredients for personalized suggestions
- 📊 Nutrition Information: Detailed nutritional facts for each recipe
- 💾 Interactive Features: Save favorites, share recipes, create shopping lists
- 🎨 Beautiful UI: Modern, responsive design with gradient backgrounds and animations

 🚀 Live Demo

[View Live Application](https://your-app-name.streamlit.app) *(Deploy first to get the link)*

📸 Screenshots

![Recipe Generator Interface](screenshot.png) *(Add a screenshot after running the app)*

 🛠️ Installation & Setup

 Prerequisites
- Python 3.8 or higher
- Git

 Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/ai-recipe-generator.git
   cd ai-recipe-generator
   ```

2. Create virtual environment
   ```bash
   python -m venv recipe_env
   
   # Activate (Windows)
   recipe_env\Scripts\activate
   
   # Activate (Mac/Linux)
   source recipe_env/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application
   ```bash
   streamlit run app.py
   ```

5. Open your browser to `http://localhost:8501`

 🔧 Configuration

Environment Variables
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_api_key_here
```

 API Integration
Currently using mock data for demonstration. To integrate with real AI:
1. Get OpenAI API key from [OpenAI Platform](https://platform.openai.com)
2. Replace mock functions with actual API calls
3. Update the recipe generation logic

 📦 Project Structure

```
ai-recipe-generator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── recipe_env/        # Virtual environment (auto-generated)
```

 🎨 UI Components

- Gradient Headers: Eye-catching header with multi-color gradient
- Recipe Cards: Beautifully styled cards with shadows and borders
- Ingredient Chips: Colorful tags for ingredients
- Step Numbers: Circular numbered steps for instructions
- Nutrition Badges: Attractive badges for nutritional information
- Interactive Buttons: Hover effects and modern styling

🌟 Key Features Explained

 Recipe Generation
- Intelligent cuisine-based recipe selection
- Dietary preference filtering
- Cooking time constraints
- Skill level matching

 User Interface
- Responsive sidebar for preferences
- Two-column layout for optimal viewing
- Professional color scheme
- Smooth animations and transitions

 Interactive Elements
- Save to favorites functionality
- Share recipe capability
- Shopping list integration
- Real-time recipe generation

 🚀 Deployment

 Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click

 Heroku
1. Create `Procfile`:
   ```
   web: sh setup.sh && streamlit run app.py
   ```
2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   port = $PORT\n\
   enableCORS = false\n\
   headless = true\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

 📝 Future Enhancements

- [ ] Real OpenAI GPT integration
- [ ] User authentication system
- [ ] Recipe rating and reviews
- [ ] Advanced ingredient substitution
- [ ] Meal planning calendar
- [ ] Shopping list export to grocery apps
- [ ] Voice input for ingredients
- [ ] Recipe video integration
- [ ] Social sharing features
- [ ] Mobile app version

 🐛 Known Issues

- Mock data is currently used (easily replaceable with real AI)
- Limited recipe database (expandable)
- No user persistence (can be added with database)

 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 👨‍💻 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

🙏 Acknowledgments

- Streamlit team for the amazing framework
- OpenAI for AI capabilities
- The Python community for excellent libraries
- Food enthusiasts who inspire great recipes

📞 Support

If you have any questions or run into issues:
1. Check the [Issues](https://github.com/yourusername/ai-recipe-generator/issues) page
2. Create a new issue with detailed description
3. Contact me directly via email

---

⭐ **Star this repository if you found it helpful!** ⭐