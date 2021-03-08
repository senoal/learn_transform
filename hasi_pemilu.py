import pandas as pd

df = pd.read_excel("election.xlsx")
print("\n___________Data Awal___________\n")
print(df)
df['suara_sah'] = df.iloc[:, 1:4].sum(axis=1)
df['suara_hilang'] = df['Jml_wrg']-df['suara_sah']
print("")

df_1=df.T

df_1['JML'] = df_1.iloc[1:, 0:15].sum(axis=1)

print(df_1.T)

df_1=df_1.T
df_1=df_1.T[1:4]

df_1.columns

for index, row in df_1.iterrows():
    print("\n___________Tampilkan Hasil Suara : "+index, row['JML'])