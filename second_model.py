from sklearn.linear_model import LinearRegression
def fit_the_model_on_the_training_data(data,X_train:np.ndarray,y_train:np.ndarray):
    regression = None
    # Code starts here
    regression=LinearRegression()
    
    regression.fit(X_train,y_train)
    # Code ends here 
    return regression