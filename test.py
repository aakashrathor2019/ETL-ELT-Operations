import pandas as pd


#Example1: Convert Dict into DF and Merge them
data1 = {
    'name' : ['Ram', 'Shyam', 'Mohan'],
    'department' : ['IT', 'Management',  'Accounts']
}

data2 ={
    'address': ['Indore', 'Bhopal', 'Barwaha'],
    'experience': [9,3,2]
}

df1= pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("First Dataframe:")
print(df1)
print("Second Dataframe:")
print(df2)

data = pd.merge(df1, df2, left_index= True, right_index=True)
print("Final Data:")
print(data)

#Example2: Implement various operations like groupby, sum, etc.
grouped_sum = data.groupby('name')['experience'].sum()
print(grouped_sum)
grouped_agg = data.groupby('address')['experience'].agg(['sum', 'mean', 'count'])
print(grouped_agg)
grouped_diff_agg = data.groupby('department').agg({'experience': ['sum', 'mean']})
print(grouped_diff_agg)