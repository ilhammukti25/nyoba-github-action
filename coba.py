import pandas as pd

today = pd.to_datetime('today')
my_dict = {"nama_depan": f"ilham {today}", "nama_belakang": "mukti"}
df = pd.DataFrame([my_dict])
df.to_csv("yuhu.csv", index=False)
