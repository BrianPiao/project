import pandas as p
df = p.read_csv("morepain.csv")
df.drop(["Star_name.1","Distance.1","Mass.1","Radius.1","Luminosity"],axis = 1,inplace = True)
f = df.dropna()
f.reset_index(drop = True,inplace = True)
f.to_csv("cleanest.csv")