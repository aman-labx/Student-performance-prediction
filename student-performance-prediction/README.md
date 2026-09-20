# Student Performance Prediction

A beginner Machine Learning project that predicts a student's final academic score using student-related factors.

## Project Status

**Learning Project — Completed**

This project was built to understand the basic Machine Learning workflow using Python and Scikit-learn.

## Objective

The goal of this project is to predict a student's final score using:

- Study hours per day
- Attendance percentage
- Previous score
- Assignment completion percentage
- Sleep hours
- Extracurricular activity

## Machine Learning Workflow

The project follows these steps:

1. Dataset creation
2. Data loading
3. Data exploration
4. Missing value checking
5. Data visualization
6. Feature and target selection
7. Train-test split
8. Model training
9. Prediction
10. Model evaluation
11. Model comparison
12. Saving the trained model
13. Making predictions using new input data

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

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
│   ├── model.py
│   └── student_score_model.pkl
│
├── .gitignore
├── README.md
└── requirements.txt
Dataset

The project uses a synthetic dataset containing 200 student records.

Features
Feature	Description
study_hours_per_day	Average study hours per day
attendance_percent	Student attendance percentage
previous_score	Previous academic score
assignment_completion_percent	Assignment completion percentage
sleep_hours	Average sleep hours
extracurricular	Extracurricular activity: 0 or 1
final_score	Target variable
Machine Learning Models
Linear Regression

Linear Regression was used to predict the student's final score.

Random Forest Regressor

Random Forest Regressor was used to compare the performance of a tree-based model with Linear Regression.

Model Results
Model	MAE	MSE	R² Score
Linear Regression	4.30	27.27	0.69
Random Forest	4.86	36.34	0.58

The results are based on the synthetic dataset used in this learning project.

Saved Model

The trained Linear Regression model is saved as:

src/student_score_model.pkl

The model.py program loads this trained model and accepts student information through the terminal to generate a predicted final score.

How to Run
1. Clone the repository
git clone https://github.com/aman-labx/student-performance-prediction.git
2. Open the project folder
cd student-performance-prediction
3. Install the required libraries
pip install -r requirements.txt
4. Run the prediction program
python src/model.py

The program will ask for:

Study hours per day
Attendance percentage
Previous score
Assignment completion percentage
Sleep hours
Extracurricular activity

It will then display the predicted final score.

Example
Student Performance Prediction
--------------------------------

Enter study hours per day: 7
Enter attendance percentage: 85
Enter previous score: 75
Enter assignment completion percentage: 90
Enter sleep hours: 7
Extracurricular activity? (1 = Yes, 0 = No): 1

Predicted Final Score: 65.06
What I Learned

Through this project, I practiced:

Working with Pandas
Working with NumPy
Data exploration
Data visualization
Feature and target selection
Train-test splitting
Linear Regression
Random Forest Regression
Model evaluation
MAE, MSE and R²
Saving models with Joblib
Loading trained models
Making predictions with new data
Organizing a Machine Learning project
Limitations

This is a beginner Machine Learning learning project and uses a synthetic dataset.

The model should not be used to make real academic decisions.

Prediction performance may differ when using real-world student data.

Future Improvements
Use a real-world student dataset
Add more relevant features
Improve data preprocessing
Try additional Machine Learning algorithms
Perform hyperparameter tuning
Build a web interface
Deploy the prediction application
Author

Aman Machhirke

1st Year College Student | Aspiring Machine Learning Engineer

Currently learning:

C Programming
Python
Data Structures & Problem Solving
Mathematics for Machine Learning
Machine Learning
Advanced Web Development

Disclaimer:

This project is created for educational and learning purposes.
