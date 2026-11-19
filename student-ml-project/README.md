# Student Support Prediction

## Project Description

This project uses machine learning to predict whether
a student passes or needs additional support.

It compares:
- Logistic Regression
- Decision Tree Classifier

A baseline model is also included.

## Dataset

Download the Student Performance Factors dataset:

https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

Put StudentPerformanceFactors.csv inside the data folder.

## Features

- Hours_Studied
- Attendance
- Sleep_Hours
- Previous_Scores
- Tutoring_Sessions

## Label

- 0 = Pass
- 1 = Needs Support

A score below 60 is labeled Needs Support.

## Running the Project

Create a virtual environment:

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

Install the requirements:

    python -m pip install -r requirements.txt

Open student_support_ml.ipynb in VS Code.

Select the .venv environment as the notebook kernel.

Run all cells.

## Outputs

The notebook creates an outputs folder containing:

- model_results.csv
- accuracy_comparison.csv
- logistic_confusion_matrix.csv
- tree_confusion_matrix.csv
- model_comparison.md

## Limitations

The 60-point cutoff is an assumption.
The models can make mistakes and may not work well
on other datasets.

They should not be used to make real decisions about students.