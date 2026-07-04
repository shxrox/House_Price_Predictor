import pandas as pd
import joblib

# 1. Load the unseen test dataset and your trained model
test_df = pd.read_csv('test.csv')
model = joblib.load('house_model.pkl') # Loads your AI's brain

# 2. Extract the Id column before preprocessing (you need this for the final file)
house_ids = test_df['Id']

# 3. Preprocess the test data EXACTLY like you did the training data
# (Ensure you select the exact same features used during model training)
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
X_test = test_df[features]

# Handle any missing values in the test set using the median (just like before)
X_test = X_test.fillna(X_test.median())

# 4. Use your trained AI to predict the house prices
predictions = model.predict(X_test)

# 5. Create the final submission DataFrame requested by Kaggle
submission = pd.DataFrame({
    'Id': house_ids,
    'SalePrice': predictions
})

# 6. Export to a CSV file (index=False ensures no extra row-number column is added)
submission.to_csv('submission.csv', index=False)
print("Your Kaggle submission file 'submission.csv' has been successfully created!")