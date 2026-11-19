# Model Card: Student Support Prediction

## Purpose
These models predict whether a student passes or needs
additional support.

This is an educational machine-learning project.

## Models
- Logistic Regression
- Decision Tree Classifier
- Baseline model

## Dataset
Student Performance Factors

Source:
https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

## Features
- Hours_Studied
- Attendance
- Sleep_Hours
- Previous_Scores
- Tutoring_Sessions

## Label
- 0 = Pass (score of 60 or higher)
- 1 = Needs Support (score below 60)

The score cutoff is an assumption for this project.
Exam_Score is used to create the label, not as a feature.

## Training and Testing
- 80% training data
- 20% testing data
- Same split for both models

## Results

Fill in these results after running the notebook.

| Metric | Logistic Regression | Decision Tree |
|---|---|---|
| Accuracy | | |
| Precision | | |
| Recall | | |
| F1 Score | | |

Best model according to F1 score:

## Limitations
- The score cutoff is an assumption.
- The dataset may not represent every school or student.
- The models can make incorrect predictions.
- Important student information may be missing.
- Training data may contain bias.
- A good accuracy score does not mean every prediction is correct.

## Responsible Use
These models should not be used to make real decisions
about students or their education.

## Conclusion
The models were compared using accuracy, precision,
recall, F1 score, and confusion matrices.