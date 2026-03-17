# Pandas  is used for data analysis and data handling 
import pandas as pd
forum_usesr = {
    "User ID": [1,2,3,4,5,6,7,8],
    "Username": ["Rish","Bodgan","Alex","Rogers","Mark","Jarvis","Bob","Vissy"],
    "Age": [18,20,35,40,20,15,24,29]
}

df = pd.DataFrame(forum_usesr)
df 