import pandas as pd

# Series - method of pandas (any method name of pandas starts with uppercase)

#s=pd.Series([10,20,30,40]) # passing list into series method of pandas
#print(s) # it gives index to each element of the list by default starting from 0 to n-1

#v=pd.Series([10,20,30,40], index=['rajeev','om','devid','ram']) # passing list into series method of pandas with index
#print(v)
#print(v['om'])
#print(v[0]) 




# dataframe means 2-d array in pandas, it is a collection of series
# all vals must be equal in dataframe, if not then it will give NaN for missing values
# df is used to convert dict data into dataframe, it is a method of pandas


#stu={
 #   'name':['rajeev','om','devid','ram'],
  #  'marks':[10,20,30,40],
   # 'age':[20,30,40,50],
    #'city':['pune','mumbai','delhi','banglore']
#}

#df=pd.DataFrame(stu)
#print(df)

#df=pd.DataFrame({
 #   'name':['rajeev','om','devid','ram'],
  #  'marks':[10,20,30,40],
   # 'age':[20,30,40,50],
    #'city':['pune','mumbai','delhi','banglore']
#})
#print(df)

#print(df.shape)
#print(df.dtypes)

#----------------------------readinf from csv file-----------------------------

data=pd.read_csv(r'F:\Downloads\Downloads\students_raw.csv')
#print(data)
#print(data.head())
#print(data.tail())
#print(data.shape)
#print(data.info())
#print(data.describe()) # apply only on numeric columns, it gives count, mean, std, min, 25%, 50%, 75%, max
#print(data[['student_name','passed']]) # it gives all the values of student_name column


#----------------loc and iloc-----------------------------
#loc is used to access rows and columns by label, it is inclusive of last value
# loc is used to access rows and columns by label, it is inclusive of last value
#iloc is used to access rows and columns by index, it is exclusive of last value

print(data.loc[0]) # it gives all the values of 0th row(1st row) of the dataframe
print('____________________________')
print(data.iloc[0]) # it gives all the values of 0th row(1st row) of the dataframe