import pandas as pd 
# import a csv or json file according to you
df = pd.read_csv("data.csv")
print(df.to_string())

#for json 
import pandas as pd 

df = pd.read_json("data.json")
print(df.to_string())
