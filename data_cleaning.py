import pandas as pd

df = pd.read_csv("appointments.csv")

# just 500 fist appointments
df_small = df.head(500)

# save in a new file
df_small.to_csv("appointments_small.csv", index=False)

print(df.head())
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values (simple example)
df["age"] = df["age"].fillna(df["age"].median())

# Create new feature
df["waiting_days"] = (pd.to_datetime(df["appointment_date"]) - 
                      pd.to_datetime(df["scheduling_date"])).dt.days

# Convert categorical columns
df["sex"] = df["sex"].astype("category")

# Remove impossible values
df = df[df["age"] >= 0]

# Output cleaned file
df.to_csv("cleaned_appointments.csv", index=False)

df.head()
print(df.head())
print(df.isnull().sum())

# Drop duplicates
df = df.drop_duplicates()

# Handle missing values (simple example)
df["age"] = df["age"].fillna(df["age"].median())

# Create new feature
df["waiting_days"] = (pd.to_datetime(df["appointment_date"]) - 
                      pd.to_datetime(df["scheduling_date"])).dt.days

# Convert categorical columns
df["sex"] = df["sex"].astype("category")

# Remove impossible values
df = df[df["age"] >= 0]

# Output cleaned file
df.to_csv("cleaned_appointments.csv", index=False)

df.head()