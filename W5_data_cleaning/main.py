import pandas as pd
 

df = pd.read_csv('messy_students.csv')
 

df.info()
 

print(df.isna().sum())
print(df.duplicated().sum())
clean_df = df.drop_duplicates()

df = df.drop_duplicates()

df['name'] = df['name'].str.strip()

df['math'] = pd.to_numeric(df['math'], errors='coerce')
df['english'] = pd.to_numeric(df['english'], errors='coerce')
df['english'] = df['english'].replace('缺考', pd.NA)


print("原始筆數:", df.shape)
print("清理後筆數:", clean_df.shape)

df[['math', 'english']].describe()
clean_df[['math', 'english']].describe()



# 驗證缺失值與重複值
clean_df.isna().sum()

clean_df.duplicated().sum()

clean_df.to_csv(
    "cleaned_students.csv",
    index=False
)
