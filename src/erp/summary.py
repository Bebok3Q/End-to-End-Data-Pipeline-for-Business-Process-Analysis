import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from utils import load_db_config
from sqlalchemy import create_engine

db_config = load_db_config()
db_url = f"{db_config['type']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}"
engine = create_engine(db_url)

df = pd.read_sql("SELECT * FROM sales", con=engine)

df['date'] = pd.to_datetime(df['date'])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Supermarket Sales Summary Dashboard",)

# Total Sales By Branch
branch_sales = df.groupby('branch')['total'].sum().reset_index()
sns.barplot(x='branch', y='total', data=branch_sales, ax=axes[0, 0], palette='Blues')
axes[0, 0].set_title("Total Sales by Branch")
axes[0, 0].set_xlabel("Branch")
axes[0, 0].set_ylabel("Total Sales")

# Sales by Product Line
sns.boxplot(x='product_line', y='total', data=df, ax=axes[0, 1], palette='coolwarm')
axes[0, 1].set_title("Sales Distribution by Product Line")
axes[0, 1].set_xlabel("Product Line")
axes[0, 1].set_ylabel("Total Sales")
axes[0, 1].tick_params(axis='x', rotation=45, labelsize=5)

# Payment Method Distribution
payment_couts = df['payment'].value_counts()
axes[1, 0].pie(payment_couts, labels=payment_couts.index, autopct='%1.1f%%', colors=["#ff9999", "#66b3ff", "#99ff99"])
axes[1, 0].set_title("Payment Method Distribution")

# Sales Trend Over Time
df_daily_sales = df.groupby('date')['total'].sum().reset_index()
sns.lineplot(x="date", y='total', data=df_daily_sales, ax=axes[1, 1], color='green')
axes[1, 1].set_title("Sales Trend Over Time")
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Total")
axes[1, 1].tick_params(axis='x', rotation=45)


plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()