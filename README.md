# 🥗 NutriLens – AI-Powered Nutrition Chatbot

### 📸 Snap it. Track it. Eat smarter. 💚

NutriLens is an AI-powered nutrition chatbot that helps users understand their food intake and make healthier dietary choices. Using Google's Gemini API, it analyses food images and text descriptions to estimate nutritional values and provide personalised nutrition guidance.

## 🚀 Features

- 📸 **AI Food Recognition:** Upload a food image or describe a meal to analyse its nutritional content.
- 🔥 **Calorie Estimation:** Estimate the calories in your meals.
- 💪 **Macronutrient Analysis:** Get estimates of protein, carbohydrates, fats, and fibre.
- 👤 **Personalised Nutrition:** Provide your age, sex (optional), height, weight, activity level, and health goal.
- 🎯 **Goal-Based Guidance:** Receive nutrition suggestions based on your goal to lose, maintain, or gain weight.
- 📊 **Daily Nutrition Summary:** Review nutrition information and compare your intake with estimated daily requirements.
- 💬 **AI Chatbot:** Ask nutrition-related questions and receive helpful responses.
- 🌐 **Interactive Web Interface:** Use the application through a simple Streamlit interface.

## 🎯 Problem Statement

Maintaining a balanced diet can be challenging when people do not know the nutritional value of their meals. Manually tracking calories and nutrients can also be time-consuming.

NutriLens simplifies this process by allowing users to upload food images or enter meal descriptions to receive quick nutritional estimates and practical dietary suggestions.

## 💡 Our Solution

NutriLens combines AI-powered food analysis with personalised nutrition guidance in one chatbot. It uses the user's profile and dietary goals to provide relevant information about meals and help users make more informed food choices.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Google Gemini API | AI-powered food analysis and chatbot responses |
| Google Gen AI SDK | Communication with Gemini models |
| Streamlit Secrets | Secure API key configuration |
| GitHub | Source code management |

## ⚙️ How It Works

1. **Create Your Profile:** Enter your basic details, activity level, and nutrition goal.
2. **Upload or Describe Food:** Submit a meal image or type a description.
3. **Analyse Nutrition:** Gemini estimates the meal's nutritional values.
4. **Explore the Results:** Review estimated calories, protein, carbohydrates, fats, and fibre.
5. **Get Nutrition Guidance:** Ask follow-up questions and request a daily nutrition summary.

## 📦 Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version supported by your dependencies
- A Google Gemini API key
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your GitHub details.

### 2. Navigate to the Project Directory

```bash
cd YOUR_REPOSITORY
```

### 3. Install Dependencies

If your repository contains a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the main dependencies:

```bash
pip install streamlit google-genai
```

### 4. Configure Your Gemini API Key

Create a `.streamlit` directory in your project folder if it does not already exist.

Inside it, create a file named `secrets.toml`:

```toml
Gemini_API_Key = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your actual API key.

**Security reminder:** Never commit your API key or `secrets.toml` file to GitHub. Add `.streamlit/secrets.toml` to your `.gitignore` file.

### 5. Run the Application

```bash
streamlit run app.py
```

Replace `app.py` with your main Python filename if it is different.

## ☁️ Deployment

NutriLens can be deployed using Streamlit Community Cloud.

1. Push your project code to a GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select your repository and main application file.
5. Open the app's settings and add your Gemini API key under **Secrets**:

```toml
Gemini_API_Key = "YOUR_GEMINI_API_KEY"
```

6. Deploy the application.

Ensure that your repository includes the required Python files, `prompts.py`, and `requirements.txt`.

## 📁 Project Structure

A possible project structure is:

```text
NutriLens/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

Your actual structure may differ depending on how you organise the application.

**Important:** Do not upload `secrets.toml` containing your API key to GitHub.

## 🔮 Future Enhancements

- 📈 Visual dashboards for daily and weekly nutrition trends.
- 🗂️ Persistent meal history and nutrition tracking.
- 🧮 More structured calculations for daily calorie and macronutrient targets.
- 🍎 Meal recommendations based on user preferences and dietary restrictions.
- 📱 Improved mobile-friendly interface.
- 🧾 Downloadable nutrition reports.
- 🔔 Optional reminders for meal logging and hydration.

## ⚠️ Limitations and Disclaimer

- Nutritional values generated from food images are estimates and may vary depending on portion size, ingredients, and preparation methods.
- AI-generated nutrition information may contain errors and should not be treated as a substitute for verified nutritional data.
- Daily nutrition requirements are estimates, not exact medical recommendations.
- NutriLens is intended for general nutrition education and does not diagnose or treat medical conditions.
- Users with medical conditions or specialised dietary needs should consult a qualified healthcare professional.

## 👨‍💻 Developer

**Developed by:** YOUR_NAME

**Project:** NutriLens – AI-Powered Nutrition Chatbot

**Built with:** Python, Streamlit, and Google Gemini API

## 📄 License

Choose a suitable open-source license before publishing your project. For example, you can use the MIT License by adding a `LICENSE` file containing its terms.

---

### 💚 NutriLens

**Understand your food. Track your nutrition. Make smarter choices.**
