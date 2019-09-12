import pandas as pd

test_data = {'t1': ['test1test','test2test'],
             't2': ['testone','testtwo']
             }


data_df = pd.DataFrame(data=test_data)
#print(data_df)
data_df['t3']= [data_df.iloc[0,0][-5:-4],data_df.iloc[1,0][-5:-4]]
# test = data_df.iloc[0,1]
# print(test)

data_df =pd.concat([data_df,pd.DataFrame(columns=("coltest1", "coltest2") ##(columns=list('ABCD')
                                         )], sort=False)

butter = 333

data_df.iloc[0, data_df.columns.get_loc('t2')] = butter

data_df['coltest1'] = data_df['t1']

print(data_df)