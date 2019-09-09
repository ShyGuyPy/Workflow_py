import pandas as pd

test_data = {'t1': ['test1test','test2test'],
             't2': ['testone','testtwo']
             }
data_df = pd.DataFrame(data=test_data)
print(data_df)
data_df['t3']= [data_df.iloc[0,0][-5:-4],data_df.iloc[1,0][-5:-4]]
# test = data_df.iloc[0,1]
# print(test)
print(data_df)