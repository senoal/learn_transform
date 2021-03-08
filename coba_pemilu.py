import pandas as pd

df = pd.read_excel("election.xlsx")
print("\n___________Data Awal___________\n")
print(df)

print("\n___________Mencari suara SAH___________\n")
#mencari suara sah x = c1+c2+c3-bb
df['suara_sah'] = df.iloc[:, 1:4].sum(axis=1)
df_1=df
print(df_1)

print("\n___________Mencari suara Hilang___________\n")
#mencari suara hilang x = total_pop - suara_sah
df_1['suara_hilang'] = df_1['Jml_wrg']-df['suara_sah']
df_2 = df_1
print(df_2)

#balik kolam, baris
df_3=df_1.T
#tampilkan jumlah
print("\n___________Tampilkan Jumlah Perolehan Suara___________\n")
df_3['JML'] = df_3.iloc[1:, 0:15].sum(axis=1)

print(df_3.T)

df_3=df_3.T
df_4=df_3.T[1:4]

df_4.columns

for index, row in df_4.iterrows():
    print("\n___________Tampilkan Hasil Suara : "+index, row['JML'])
    #print(row['JML'])
    
    #JML.max()