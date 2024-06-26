import pandas as pd
import numpy as np

df = pd.read_csv('calorie_info.csv', encoding = 'unicode_escape')

df.shape

df.head(10)

df.info()

pd.isnull(df)

pd.isnull(df).sum()

df.describe()

df["per_100_ml_or_gm"].replace("ml","",regex=True, inplace=True)

df["per_100_ml_or_gm"].replace("g","",regex=True, inplace=True)

pd.to_numeric(df["per_100_ml_or_gm"])

df["cal_per_100_ml_or_gms"].replace("cal","",regex=True, inplace=True)
pd.to_numeric(df["cal_per_100_ml_or_gms"])

df["kj_per_100_ml_or_gms"].replace("kJ","",regex=True, inplace=True)
pd.to_numeric(df["kj_per_100_ml_or_gms"])

df["cal_per_serving"].replace("cal","",regex=True, inplace=True)
pd.to_numeric(df["cal_per_serving"])

df["kj_per_serving"].replace("kJ","",regex=True, inplace=True)
pd.to_numeric(df["kj_per_serving"])

if df["per_ounces"].dtype == 'object':
  df["per_ounces"].str.replace("fl. oz. (30 ml)","1",regex=True)
df["per_ounces"] = pd.to_numeric(df["per_ounces"])
pd.to_numeric(df["per_ounces"], errors='coerce')

df.drop("per_ounces", axis=1, inplace=True)

df["cal_per_ounces"].replace("cal","",regex=True, inplace=True)
pd.to_numeric(df["cal_per_ounces"])

df["cal_per_ounces"].astype(np.int64)

df.dropna(inplace=True)

df["kj_per_ounces"].replace("kJ","",regex=True, inplace=True)
pd.to_numeric(df["kj_per_ounces"])

df.head()

df.dropna(inplace=True)
