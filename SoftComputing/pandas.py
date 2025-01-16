import pandas as pd

data = {
    'Name' : ['Alice', 'Bob','Charlie','David'],
    'Age' : [25,30,35,40],
    'City' : ['New York', 'Los Angeles','Chicago','Houston']
}

df = pd.DataFrame(data)
print("Orginal DataFrame:")
print(df)

print("Age column:")
print(df['Age'])

filtered_df = df[df['Age']>30]
print("Filtered Dataframe (Age > 30):")
print(filtered_df)

mean_age = df['Age'].mean()
print("Mean Age:", mean_age)

