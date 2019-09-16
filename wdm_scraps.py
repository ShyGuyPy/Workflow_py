#unused parts of wdm code


#print(data_df)

#print(data_df.index.month)

datetime_values = list(data_df.index.values) #.index.array)#
check2 = data_df.iloc[7,0]
dtr2 = datetime_values[0:5]

df_shape = data_df.shape


datetime_values_df = pd.DataFrame(datetime_values)

datetime_values_df.columns=["Date_Time"]

#print(datetime_values_df)

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

# data_df.to_csv(output_folder +"/" + title + ".csv")


#print(dtr2)
#print(df_shape)
#print(datetime_values)
#print(datetime_values_df)
#print(data_df)

# for col in data_df.columns:
#     print(col)

#print(data_df.axes)
#print(count)