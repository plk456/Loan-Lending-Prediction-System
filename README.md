# Loan-Lending-System

Protecting lenders with predictive analytics

# Lending Loan Status Prediction

## Introduction

Lending Club is a peer-to-peer lending platform that connects borrowers with investors, enabling individuals to obtain personal loans without going through traditional banks. Predicting the loan status—whether a loan will be fully paid or charged off—is critical for managing risk, improving lending decisions, and protecting investors.

This project leverages advanced machine learning techniques to build a predictive model that forecasts the loan status based on various borrower and loan attributes. By analyzing historical loan data, the model helps identify risky loans and improve lending outcomes.

## Features

- **Comprehensive Data Preprocessing**: Cleans and prepares raw loan data, including handling missing values and encoding categorical features.
- **Imbalanced Dataset Handling**: Utilizes SMOTE (Synthetic Minority Over-sampling Technique) to balance the classes for more reliable predictions.
- **Feature Selection**: Drops irrelevant or redundant features to improve model performance.
- **Machine Learning Model**: Implements a Random Forest Classifier with hyperparameter tuning via GridSearchCV for optimal performance.
- **Evaluation Metrics**: Assesses model using accuracy, classification report, confusion matrix, and ROC AUC score.
- **Data Standardization**: Applies feature scaling with StandardScaler to normalize input features.
- **Model Persistence**: Saves the trained model using pickle for future deployment or inference use.
  
## Technologies Used

- **Python**: Primary programming language for data processing and modeling.
- **Pandas & NumPy**: Data manipulation and numerical operations.
- **scikit-learn**: Machine learning algorithms, preprocessing, model selection, and evaluation tools.
- **imblearn (SMOTE)**: Handling imbalanced data problems by synthesizing new samples.
- **Pickle**: Serializing and saving trained machine learning models.

## Summary

This project delivers a robust loan status prediction model that assists lenders in making better-informed decisions. By combining data preprocessing, class balancing, and machine learning, the model can accurately classify loans as likely to be paid or defaulted. Such predictive insights enhance risk management and financial planning in peer-to-peer lending platforms.

## Contact

For questions, suggestions, or collaboration, please reach out:

- **Name**: Prodduturu Likith Kumar
- **Email**: kumarlikith178@gmail.com
- **LinkedIn**: (https://www.linkedin.com/in/likithkumar456/)

---

Feel free to open issues or submit pull requests if you want to contribute or report bugs.
