import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
import joblib 

data = pd.read_csv('full_combined_quarterly_reports.csv') 

grouped_data = data.groupby('market_cap_category')


svm_models = {}




for group_name, group_data in grouped_data:
    print("Training SVM model for market cap category:", group_name)
    group_data = group_data[['company_name', 'ticker', 'book_value', 'book_to_share_value', 
                             'earnings_per_share', 'debt_ratio', 'current_ratio', 
                             'dividend_yield_ratio', 'price_movement_percent', 
                             'indicator']]
    group_data.dropna(inplace=True)
    scaler = MinMaxScaler()

    numerical_columns = ['book_value', 'book_to_share_value', 'earnings_per_share', 
                         'debt_ratio', 'current_ratio', 'dividend_yield_ratio', 
                         'price_movement_percent']

    group_data[numerical_columns] = scaler.fit_transform(group_data[numerical_columns])
    
    X = group_data[['book_value', 'book_to_share_value', 'earnings_per_share', 
                    'debt_ratio', 'current_ratio', 'dividend_yield_ratio', 
                    'price_movement_percent']]
    y = group_data['indicator']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    

    param_grid = {
    'C': [0.1, 1, 10, 100],  # Regularization parameter
    'kernel': ['linear', 'rbf', 'poly'],  # Kernel type
    'gamma': ['scale', 'auto'],  # Kernel coefficient (for 'rbf' and 'poly' kernels)
    }

  
    grid_search = GridSearchCV(estimator=SVC(), param_grid=param_grid, cv=5, n_jobs=-1)


    grid_search.fit(X_train, y_train)

    print("Grid Search completed.")

  
    best_params = grid_search.best_params_
    print("Best parameters:", best_params)


    best_model = grid_search.best_estimator_

  
    best_model_filename = f'models/{group_name}-best_svm_model.pkl'
    joblib.dump(best_model, best_model_filename)
    print("Best model saved as", best_model_filename)


    y_pred = best_model.predict(X_test)


    print("Classification Report:")
    classification_rep = classification_report(y_test, y_pred)
    print(classification_rep)

    print("Confusion Matrix:")
    confusion_mat = confusion_matrix(y_test, y_pred)
    print(confusion_mat)

    report_filename = f'models/{group_name}_classification_report.txt'
    with open(report_filename, 'w') as f:
        f.write(classification_rep)

    cm_filename = f'models/{group_name}_confusion_matrix.txt'
    with open(cm_filename, 'w') as f:
        f.write(str(confusion_mat))

    print("Classification Report saved as", report_filename)
    print("Confusion Matrix saved as", cm_filename)