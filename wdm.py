from wdmtoolbox import wdmtoolbox
import glob
import pandas as pd

#this is the directory where the raw wdm files are placed
source_dir_met = r"C:\Users\icprbadmin\Documents\Python_Scripts\Workflow_py\input\met"
source_dir_prad = r"C:\Users\icprbadmin\Documents\Python_Scripts\Workflow_py\input\prad"

#create object containing all files in for met and prad
allFiles1 = glob.glob(source_dir_met + "/*met*.wdm*")
allFiles2 = glob.glob(source_dir_prad+ "/*prad*.wdm*")

#our file destintion
output_folder = r"C:\Users\icprbadmin\Documents\Python_Scripts\Workflow_py\output"

#iterate through the met files
for file in allFiles1:
    #takes specific indexes from the right to include only the unique identification code
    title = file[-10:-4]
    #use wdmtoolbox function to assign data to a pandas dataframe
    data_df = wdmtoolbox.extract(file, 1000)

    #output extracted pandas df to csv
    #data_df.to_csv(output_folder +"/" + title + ".csv")

datetime_values = list(data_df.index.array)#.index.values)
check2 = data_df.iloc[7,0]
dtr2 = datetime_values[0:5]

df_shape = data_df.shape


datetime_values_df = pd.DataFrame(datetime_values)
datetime_values_df.columns=["Date_Time"]

#add rows to dataframe
# data_df =pd.concat([data_df, datetime_values_df, pd.DataFrame(columns=("year", "month", "day", "hour")
#                                          )], sort=False)




#-------------formatting data

#disable warning
pd.options.mode.chained_assignment = None  # default='warn'




#data_df['Datetime'] = []
#
# data_df['year'] = df[]


# count = 0
# for i in datetime_values:#dtr2:
#     #datetime object to string
#     dt = str(i)
#     # grabbing select parts of the datetime object for each entry in the data
#     year = dt[-29:-25]
#     month = dt[-24:-22]
#     day = dt[-21:-19]
#     hour = dt[-18:-16]
#
#     #then assign each to respective column
#     data_df.iloc[count, data_df.columns.get_loc('year')] = year
#     data_df.iloc[count, data_df.columns.get_loc('month')] = month
#     data_df.iloc[count, data_df.columns.get_loc('day')] = day
#     data_df.iloc[count, data_df.columns.get_loc('hour')] = hour
#     #print(count)
#
#     # data_df.iloc[count,3] = month
#     # data_df.iloc[count,4] = day
#     # data_df.iloc[count,5] = hour
#     count +=1

data_df.to_csv(output_folder +"/" + title + ".csv")


#print(dtr2)
#print(df_shape)
#print(datetime_values)
#print(datetime_values_df)

# for col in data_df.columns:
#     print(col)

print(data_df.keys())
#print(count)