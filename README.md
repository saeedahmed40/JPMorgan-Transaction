# JPMorgan-Transaction
This project analyses a recently acquired dataset of mobile money transactions from a financial services provider. The goal is to gain insights into customer behaviour, identify patterns of fraud, and potentially develop predictive models for fraud detection.

Dataset Overview
-----------------
The dataset contains records of mobile money transactions with the following key features:

Transaction Types:
------------------
CASH-IN: Deposits into a user's account.
CASH-OUT: Withdrawals from a user's account.
DEBIT: Withdrawals sent directly to a user's bank account.
PAYMENT: Purchases of goods or services.
TRANSFER: Movement of funds between user accounts.

Fraud Indicators:
-----------------
IsFlaggedFraud: Indicates potential fraud detected by the provider's automated system.
IsFraud: Confirms actual fraudulent activity.

# Project Objectives

Exploratory Data Analysis (EDA):
--------------------------------
Understand the distribution of transaction types and amounts.
Analyse user behaviour patterns (e.g., transaction frequency, preferred transaction types).
Identify any correlations between transaction features and fraud.

Fraud Detection:
----------------
Evaluate the performance of the existing fraud detection system (IsFlaggedFraud).
Develop and compare machine learning models for fraud prediction.
Explore techniques for anomaly detection and unsupervised learning to identify unusual transaction patterns.

Insights and Recommendations:
-----------------------------
Provide actionable insights to the financial services provider regarding fraud prevention and customer engagement strategies.
Develop recommendations for improving the existing fraud detection system.
