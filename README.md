# 🧬 PCOS Diagnosis Web App

A machine learning-powered web application that predicts whether a person is likely to have PCOS (Polycystic Ovary Syndrome) based on key health inputs like age, BMI, menstrual irregularity, testosterone levels, and antral follicle count.


---

## 🚀 Features

- Accepts input from users via a clean HTML form.
- Predicts PCOS diagnosis based on trained logistic regression model.
- Communicates with a Flask backend via HTTP POST.
- Uses `StandardScaler` to normalize inputs before prediction.

---

## 🧠 Model Details

- Dataset: [Kaggle - PCOS Diagnosis Dataset](https://www.kaggle.com/datasets/samikshadalvi/pcos-diagnosis-dataset)
- Model: Logistic Regression
- Features Used:
  - Age
  - BMI
  - Menstrual Irregularity (0 = No, 1 = Yes)
  - Testosterone Level (ng/dL)
  - Antral Follicle Count
  ---
