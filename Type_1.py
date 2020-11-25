import numpy as np 
import pandas as pd 
import random random.seed(12345)


df = pd.read_csv('bio_data.csv') df['Z'] = df['old - placebo'] df['Y'] = df['new - old']
# Plug-in
theta_hat = np.mean(df['Y'])/np.mean(df['Z']) theta_hat
# Bootstrap
bootstrap_theta = []
for i in range(1,1000):
df_sample = np.random.choice(df['subject'], size= 8, replace=True) y_sample = []
z_sample = []
for i in df_sample:
y_sample.append(list(df[df['subject'] == i]['Y'])[0])
z_sample.append(list(df[df['subject'] == i]['Z'])[0])
# append all the thetas all_theta.append(np.mean(y_sample)/np.mean(z_sample))
# Get the values
print("Mean: " , np.mean(all_theta)) print(np.percentile(all_theta,2.5) , np.percentile(all_theta,97.5))