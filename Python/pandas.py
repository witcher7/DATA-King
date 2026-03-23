# Pandas  is used for data analysis and data handling 
import pandas as pd
forum_usesr = {
    "User ID": [1,2,3,4,5,6,7,8],
    "Username": ["Rish","Bodgan","Alex","Rogers","Mark","Jarvis","Bob","Vissy"],
    "Age": [18,20,35,40,20,15,24,29]
}

df = pd.DataFrame(forum_usesr)
df.shape  # gives shape 
df.columns  # gives columns 
df.dtypes # to check data types 
df.values 
df.head(N) # first 5 rows
df.tail(N) # last N rows
df.columns.tolist() # to convert into list
df.describe()
df.isna() # where values not available or None gives true
df.isna().sum() # to sum NA values 
df.select_dtypes(include='object') #this will include only those columns which has column object
df.select_dtypes(include='int64') #this will include only those columns which has column object
df.select_dtypes(exclude='int64') #this will include only those columns which has column object
df['username'].value_counts() # count total columns times 
df['reputation'].unique() 
df.sort_values(by="username", ascending=True)

# LOCATION 
df.loc[2] # label
df.loc[1:3] # from row 1 to row 3 
df.loc[2:3,['Age',"Total Posts"]]
df.iloc[3] # index of row 
df.iloc[4:5]


# Filtering 
df[df['reputation']== 500]
df[df['Total Posts']>=200]
df[df['Total Posts']>=200 & (df['Age']>= 30)]
df[df['Total Posts']>=200 | (df['Age']>= 30)]
df['reputation'].isin([200,500])
df[df['Total Posts'].isin(range(200,350))]

## Date and Time range filteration 
date_range = pd.date_range(start="2032-03-01",end = "2032-08-01")
df[df['Joined Date'].isin(date_range)]


# ADDING new Rows and COlumns 
df['language'] = 'English' # su
df['Active'] = [True,False,False] 
# concatenate 
# pd.concat([df,df2],axis=1) # will add horizontaly
df.drop(['language'])