import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv("customer_shopping_behavior.csv")

# ----------------------------
# Data Cleaning
# ----------------------------

# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

# Rename column
df.rename(columns={'Purchase_Amount_USD': 'Purchase_Amount'}, inplace=True)

# Handle missing values (Review Rating)
df['Review_Rating'] = df.groupby('Category')['Review_Rating'] \
                       .transform(lambda x: x.fillna(x.median()))

# Create Age Group
bins = [0, 25, 40, 60, 100]
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Convert purchase frequency to days
frequency_mapping = {
    'Weekly': 7,
    'Bi-Weekly': 14,
    'Fortnightly': 14,
    'Monthly': 30,
    'Quarterly': 90,
    'Every 3 Months': 90,
    'Annually': 365
}
df['purchase_frequency_days'] = df['Frequency_of_Purchases'].map(frequency_mapping)

# Drop unnecessary column
df.drop(columns=['Promo_Code_Used'], inplace=True)

# ----------------------------
# Push to SQL
# ----------------------------

engine = create_engine("mysql+pymysql://username:password@localhost:3306/ecommerce_db")

df.to_sql('customer_data', con=engine, if_exists='replace', index=False)

print("Data cleaning and upload completed successfully.")
