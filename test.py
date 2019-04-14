import pandas as pd

df = pd.read_csv('/Users/saching12/Desktop/python codes/Google_landmark_recognition/train.csv')
df.head(5)

var = df[df['id'] == '000a00df314b41c1'].url
var = str(var)
f = open("demofile2.txt", "a")
f.write(var)
f.close()