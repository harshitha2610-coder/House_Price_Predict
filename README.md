# 🏠 House Price Prediction System

## 📌 Project Overview

The House Price Prediction System is a Machine Learning application that predicts residential house prices based on various property features such as square footage, number of bedrooms, bathrooms, year built, lot size, garage size, and neighborhood quality.

The project performs data preprocessing, exploratory data analysis (EDA), feature engineering, model training, model evaluation, and provides a user-friendly prediction interface using Streamlit.

---

## 🎯 Objective

To build a regression-based machine learning model that accurately predicts house prices using property attributes and provides an interactive web application for users to estimate house prices.

---

## 📂 Dataset

**Dataset Name:** House Price Regression Dataset

### Features

- Area
- Num_Bedrooms
- Num_Bathrooms
- Floors
- Year_Built
- Location Code (0=Downtown, 1=Suburban, 2=Urban)
- Condition Code (0=Poor, 1=Average, 2=Good)
- Garage Code (0=No, 1=Yes)


**Target Variable**

- House_Price

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Save Trained Model
9. Streamlit Deployment

---

## 🤖 Machine Learning Models

- Linear Regression
- Decision Tree Regressor

The Decision Tree Regressor was selected as the final model and saved using Joblib.

---

## 📈 Evaluation Metrics

The model performance was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🚀 Streamlit Application

The application allows users to enter:

- Area
- Number of Bedrooms
- Number of Bathrooms
- Floors
- Year Built
- Location Code
- Garage Code
- Condition Code

The trained model predicts the estimated house price instantly.

---

## 📁 Project Structure

```
House_Price_Prediction/
│
├── app.py
├── regressionmodel.ipynb
├── house_price_tree_model.pkl
├── house_price_regression_dataset.csv
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone <https://github.com/harshitha2610-coder/House_Price_Predict.git>
```

Move into the project folder

```bash
cd House_Price_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

### Home Page
![Home_page](screenshots/Home_page.jpeg)

### Prediction Result
![Prediction](screenshots/Prediction.jpeg)
---

## 🌐 Deployment

The project is deployed using **Streamlit Community Cloud**.
- https://housepricepredictionbyharshhi.streamlit.app/
---

## 🔮 Future Enhancements

- Random Forest Regression
- XGBoost Regression
- Live Real Estate Data Integration
- Map-based Location Analysis
- Cloud Database Integration
- Mobile Application

---

## 👨‍💻 Author

**Harshitha L**

AI & Machine Learning Internship Project

---

## 📜 License

This project is developed for educational and internship purposes.
