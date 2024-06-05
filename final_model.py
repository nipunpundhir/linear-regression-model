def separate_data_and_target_new(df):
    X,y = np.ndarray([]),np.ndarray([])
    # Code starts here
    X=df.drop(['ln_selling_price','selling_price'], axis=1)
    y=df['ln_selling_price']
    # Code ends here
    return X,y