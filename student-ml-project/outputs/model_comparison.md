
# Model Comparison

The model with the highest F1 score was Logistic Regression.

## Logistic Regression
Accuracy: 0.992
Precision: 0.750
Recall: 0.429
F1 Score: 0.545

False positives: 2
False negatives: 8

## Decision Tree
Accuracy: 0.991
Precision: 0.750
Recall: 0.214
F1 Score: 0.333

False positives: 1
False negatives: 11

## Conclusion

The models were trained and tested using the same data split.

The best model was selected using the F1 score.

Accuracy shows the percentage of correct predictions.
Precision measures how reliable support predictions are.
Recall measures how many support cases were identified.

A false negative means the model missed a case needing support.
A false positive means it incorrectly flagged a case.

The difference between training and test accuracy can help
identify possible overfitting.

The dataset and score cutoff have limitations. These models
should not be used to make real decisions about students.
