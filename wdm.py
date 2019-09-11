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

datetime_row = list(data_df.index.values)
check2 = data_df.iloc[7,0]
dtr2 = datetime_row[0:5]
print(dtr2)

#add rows to dataframe
data_df =pd.concat([data_df,pd.DataFrame(columns=("year", "month", "day", "hour") #(columns=list('ABCD')
                                         )], sort=False)

#-------------formatting data

#disable warning
pd.options.mode.chained_assignment = None  # default='warn'

count = 0
for i in dtr2:#datetime_row:
    #datetime object to string
    dt = str(i)
    # grabbing select parts of the datetime object for each entry in the data
    year = dt[-29:-25]
    month = dt[-24:-22]
    day = dt[-21:-19]
    hour = dt[-18:-16]

    #then assign each to respective column
    data_df.iloc[count, data_df.columns.get_loc('year')] = year
    #print(count)

    # data_df.iloc[count,3] = month
    # data_df.iloc[count,4] = day
    # data_df.iloc[count,5] = hour
    count +=1

#data_df.to_csv(output_folder +"/" + title + ".csv")


# print(dt)
# print(year)
# print(month)
# print(day)
# print(hour)



# check3 = list(test_df.columns)

print(data_df)