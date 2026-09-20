import pandas as pd
import joblib
import os

# Load trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "student_score_model.pkl"
)

model = joblib.load(model_path)


def predict_score(
    study_hours_per_day,
    attendance_percent,
    previous_score,
    assignment_completion_percent,
    sleep_hours,
    extracurricular
):
    input_data = pd.DataFrame([{
        "study_hours_per_day": study_hours_per_day,
        "attendance_percent": attendance_percent,
        "previous_score": previous_score,
        "assignment_completion_percent": assignment_completion_percent,
        "sleep_hours": sleep_hours,
        "extracurricular": extracurricular
    }])

    prediction = model.predict(input_data)

    return prediction[0]


if __name__ == "__main__":

    print("Student Performance Prediction")
    print("--------------------------------")

    study_hours = float(input("Enter study hours per day: "))
    attendance = float(input("Enter attendance percentage: "))
    previous_score = float(input("Enter previous score: "))
    assignment_completion = float(
        input("Enter assignment completion percentage: ")
    )
    sleep_hours = float(input("Enter sleep hours: "))

    extracurricular = int(
        input("Extracurricular activity? (1 = Yes, 0 = No): ")
    )

    predicted_score = predict_score(
        study_hours,
        attendance,
        previous_score,
        assignment_completion,
        sleep_hours,
        extracurricular
    )

    print("\nPredicted Final Score:", round(predicted_score, 2))