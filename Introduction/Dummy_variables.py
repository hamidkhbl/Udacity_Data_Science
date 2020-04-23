import pandas as pd 
import numpy as np 

def create_dummy_df(df, cat_cols, dummy_na):
    for col in cat_cols:
        try:
            df = pd.concat([df.drop(col,axis=1), pd.get_dummies(df[col], dummy_na=dummy_na)], axis=1)
        except:
            continue
    return df

# test
# dummy_var_df = pd.DataFrame({'col1': ['a', 'a', 'b', 'b', 'a', np.nan, 'b', np.nan],
#                              'col2': [1, np.nan, 3, np.nan, 5, 6, 7, 8] 
# })
                            
# print(create_dummy_df(dummy_var_df,['col1'],False))