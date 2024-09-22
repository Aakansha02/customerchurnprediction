# Customer Churn Prediction Model

## Introduction
This project aims to predict customer churn using machine learning techniques. By identifying customers who are likely to leave, businesses can implement proactive strategies to enhance customer retention.

The model is built on the **Churn_Modelling.csv** dataset, which includes various customer features such as demographics, account details, and previous churn behavior.

## Dataset Features
- **CustomerId**: Unique identifier for each customer
- **Surname**: Customer's surname
- **CreditScore**: Credit score of the customer
- **Geography**: Country of the customer
- **Gender**: Gender of the customer
- **Age**: Age of the customer
- **Tenure**: Number of years the customer has been with the company
- **Balance**: Account balance
- **NumOfProducts**: Number of products the customer is using
- **HasCrCard**: Whether the customer has a credit card
- **IsActiveMember**: Whether the customer is an active member
- **EstimatedSalary**: Estimated salary of the customer
- **Exited**: Target variable (1 = churned, 0 = retained)

## Evaluation
The model provides an accuracy of **87%** on the test set. This indicates that 87% of the predictions made by the model are correct, demonstrating its effectiveness in identifying customers at risk of churning.

### Evaluation Metrics
In addition to accuracy, the model's performance is evaluated using several key metrics:
- **Precision**: Measures the correctness of positive predictions.
- **Recall**: Assesses the model's ability to identify all relevant cases (churned customers).
- **F1 Score**: The harmonic mean of precision and recall, offering a balance between the two.
- **ROC-AUC**: Evaluates the model's ability to distinguish between classes.

These metrics can be explored in the `model.ipynb` notebook to gain deeper insights into the model's performance.
