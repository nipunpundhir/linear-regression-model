import statsmodels.formula.api as smf
def fit_the_model_ols(data):    
    ols_model = None
    train, test = np.ndarray([]),np.ndarray([])
    # Code starts here
    train, test = train_test_split(data, test_size=0.2, random_state=1234)
    
    # Building the OLS model using statsmodels formula API
    formula = 'selling_price ~ ' + ' + '.join(data.drop(columns=['selling_price']).columns)
    ols_model = smf.ols(formula, data=train).fit()
        
    # Return the model and the test data    
    return ols_model,test