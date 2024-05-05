from libraries import *

def preprocess_data(df):
    df = pd.get_dummies(df, columns=['genre'])
    X = df.drop(columns=['popularity', 'artist', 'song'])
    y = df['popularity']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_models(X_train, y_train):
    linear_reg = LinearRegression()
    rf_reg = RandomForestRegressor()
    gb_reg = GradientBoostingRegressor()
    linear_reg.fit(X_train, y_train)
    rf_reg.fit(X_train, y_train)
    gb_reg.fit(X_train, y_train)
    return {'Linear Regression': linear_reg, 'Random Forest': rf_reg, 'Gradient Boosting': gb_reg}

def evaluate_models(models, X_train, X_test, y_train, y_test,confidance):
    results = {}
    for name, model in models.items():
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        y_pred = model.predict(X_test)
        prediction_score = model.score(X_test, y_pred)
        original_score = model.score(X_test, y_test)         
        n = len(y_test)
        std_err = np.std(y_test - y_pred)
        margin_err = std_err * stats.t.ppf((1 + (confidance/100)) / 2, n - 1)
        lower_bound = y_pred - margin_err
        upper_bound = y_pred + margin_err
        
        results[name] = {'Train Score': train_score, 'Test Score': test_score, 
                         'Prediction Score': prediction_score, 'Original Score': original_score,
                         'Lower Bound': lower_bound, 'Upper Bound': upper_bound}
    return results

def train_predict_regression_model(df,confidance):
    X_train, X_test, y_train, y_test = preprocess_data(df)
    models = train_models(X_train, y_train)
    evaluation_results = evaluate_models(models, X_train, X_test, y_train, y_test,confidance)
    return models, evaluation_results
