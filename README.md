# Student Performance Prediction

A beginner-friendly Machine Learning project that predicts a student's final academic score using study habits, attendance, previous performance, assignment completion, sleep hours, and extracurricular activity.

## Project Status

**Learning Project — Completed**

This project was built as part of my journey toward becoming a Machine Learning Engineer.

> **Dataset Note:** The dataset used in this project is synthetically generated for learning and experimentation. It should not be treated as real-world student data.

---

## Objective

The goal of this project is to understand the basic Machine Learning workflow:

1. Load and explore a dataset
2. Perform basic data analysis
3. Check missing values
4. Analyze feature correlations
5. Prepare features and target
6. Split data into training and testing sets
7. Train regression models
8. Make predictions
9. Evaluate model performance
10. Compare different models
11. Analyze model coefficients
12. Save the trained model

---

## Dataset

The dataset contains **200 student records** with the following features:

| Feature | Description |
|---|---|
| `student_id` | Unique student identifier |
| `study_hours_per_day` | Average daily study hours |
| `attendance_percent` | Attendance percentage |
| `previous_score` | Previous academic score |
| `assignment_completion_percent` | Assignment completion percentage |
| `sleep_hours` | Average daily sleep hours |
| `extracurricular` | Whether the student participates in extracurricular activities |
| `final_score` | Final academic score — target variable |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Joblib

---

## Project Structure

```text
student-performance-prediction/
│
├── data/
│   └── student_data.csv
│
├── notebooks/
│   └── student_prediction.ipynb
│
├── src/
│   └── student_score_model.pkl
│
├── README.md
├── requirements.txt
└── .gitignore
Machine Learning Workflow
1. Data Loading

The dataset was loaded using Pandas.

import pandas as pd

df = pd.read_csv("../data/student_data.csv")
2. Data Exploration

Basic dataset information and statistics were explored using:

df.info()
df.describe()
df.isnull().sum()

A correlation heatmap was also created to understand relationships between numerical features.

3. Feature and Target Selection

The student_id column was removed because it is only an identifier.

X = df.drop(columns=["student_id", "final_score"])
y = df["final_score"]

Here:

X contains the input features.
y contains the target variable, final_score.
4. Train-Test Split

The dataset was divided into training and testing sets.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Dataset split:

Training samples: 160
Testing samples: 40
Models

Two regression models were experimented with.

Linear Regression

Linear Regression was used as the primary baseline model.

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
Random Forest Regression

Random Forest Regression was also tested for comparison.

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
Model Evaluation

The models were evaluated using:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
R² Score
Results
Model	MAE	MSE	R² Score
Linear Regression	4.30	27.27	0.69
Random Forest	4.86	36.34	0.58

On the current synthetic dataset and test split, Linear Regression produced lower MAE and MSE and a higher R² score than Random Forest.

Understanding the Metrics
Mean Absolute Error (MAE)

MAE represents the average absolute difference between the actual and predicted values.

For this project:

MAE = 4.30

The model's predictions differed from the actual final scores by about 4.3 points on average on the test set.

Mean Squared Error (MSE)

MSE calculates the average squared prediction error.

MSE = 27.27

Lower MSE indicates smaller squared prediction errors.

R² Score

R² measures how much of the variation in the target variable is explained by the model.

R² = 0.69

For this test split, the Linear Regression model explains approximately 69% of the variation in final scores.

Actual vs Predicted Scores

An Actual vs Predicted plot was created to visually compare the model's predictions with the actual final scores.

The plot helps understand how closely the predicted values follow the actual values.

Feature Coefficients

The Linear Regression model produced the following coefficients:

Feature	Coefficient
study_hours_per_day	1.811669
sleep_hours	1.220054
extracurricular	1.043916
previous_score	0.322308
attendance_percent	0.070735
assignment_completion_percent	0.069448

The coefficients describe the fitted linear relationship learned by the model from this dataset.

For example, the coefficient for study_hours_per_day is approximately 1.81. Within the fitted model, holding the other features constant, a one-unit increase in study hours is associated with an approximately 1.81-point increase in the predicted final score.

Important: These coefficients describe relationships learned from this synthetic dataset. They should not be interpreted as causal effects or as proof that one factor universally determines student performance.

Saved Model

The trained Linear Regression model was saved using Joblib.

src/student_score_model.pkl

The saved model can later be loaded for making predictions on new data.

Example:

import joblib

model = joblib.load("../src/student_score_model.pkl")
How to Run the Project
1. Clone the Repository
git clone <YOUR-GITHUB-REPOSITORY-URL>
2. Open the Project
cd student-performance-prediction
3. Install Dependencies
pip install -r requirements.txt

If pip does not work directly in your environment, you can install packages through Jupyter Notebook using:

%pip install -r ../requirements.txt
4. Open the Jupyter Notebook

Open:

notebooks/student_prediction.ipynb

Run the notebook cells from top to bottom.

Requirements

The project uses the following Python libraries:

numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter

Joblib is used to save the trained model.

Limitations

This is a beginner Machine Learning learning project and has several limitations:

The dataset is synthetically generated.
The dataset contains 200 records.
The model has been evaluated on the current train/test split.
The results should not be considered evidence of real-world student performance prediction.
The project does not use real student records.
The model is intended for learning Machine Learning concepts rather than real academic decision-making.
What I Learned

Through this project, I practiced:

Data loading with Pandas
Data exploration
Data visualization
Correlation analysis
Feature and target selection
Train-test splitting
Linear Regression
Random Forest Regression
Model prediction
Model evaluation
MAE, MSE and R²
Feature coefficient analysis
Saving a trained ML model with Joblib
Comparing Machine Learning models
Future Improvements

Possible future improvements include:

Experimenting with additional datasets
Adding more relevant features
Trying additional regression algorithms
Using cross-validation
Hyperparameter tuning
Building a prediction interface
Creating a simple web application around the trained model
Deploying the application
Author

Aman Machhirke

1st Year College Student | Aspiring Machine Learning Engineer

This project is part of my journey of learning Python, Machine Learning, Data Structures, Mathematics for Machine Learning, and practical AI/ML development.

Disclaimer

This project is created for educational and learning purposes.

The dataset is synthetic and does not represent real student records or real-world academic outcomes.
