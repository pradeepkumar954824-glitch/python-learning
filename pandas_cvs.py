import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Neha"],
    "Marks": [85, 92, 78, 95]
}

df = pd.DataFrame(data)

print(df)

print("औसत अंक:", df["Marks"].mean())
print("सबसे अधिक अंक:", df["Marks"].max())
print("सबसे कम अंक:", df["Marks"].min())