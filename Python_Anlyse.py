# import pandas as pd

# # Load the data (from a CSV or SQL database)
# # For CSV: df = pd.read_csv('employee_benefits.csv')
# # For SQL, you would typically use SQLAlchemy or a similar library to connect to your database.
# # Example: 
# # from sqlalchemy import create_engine
# # engine = create_engine('mysql+pymysql://user:password@host/database')
# # df = pd.read_sql('SELECT * FROM employee_benefits', engine)

# # Sample DataFrame creation (for demonstration)
# data = {
#     'employee_id': [1, 2, 3, 1, 2, 3],
#     'department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
#     'age': [25, 35, 30, 26, 36, 31],
#     'benefit_type': ['medical', 'dental', 'vision', 'medical', 'vision', 'dental'],
#     'enrollment_date': pd.to_datetime(['2022-01-15', '2022-01-16', '2022-02-01', '2022-01-15', '2022-01-16', '2022-02-01']),
#     'usage_date': pd.to_datetime(['2022-02-10', '2022-02-15', None, '2022-03-12', '2022-03-15', None]),
# }

# df = pd.DataFrame(data)

# # Data Cleaning
# # Fill missing usage dates with 'No Usage'
# df['usage_date'].fillna('No Usage', inplace=True)

# # Convert enrollment and usage to appropriate formats (if needed)
# df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])
# df['usage_date'] = pd.to_datetime(df['usage_date'], errors='coerce')

# # Analyze Enrollment Rates
# enrollment_rates = df['benefit_type'].value_counts(normalize=True) * 100

# # Analyze Utilization Rates
# utilization_rates = df['usage_date'].value_counts(normalize=True) * 100

# # Demographic Insights
# demographic_insights = df.groupby(['department', 'benefit_type']).size().unstack(fill_value=0)

# # Display Results
# print("Enrollment Rates:\n", enrollment_rates)
# print("\nUtilization Rates:\n", utilization_rates)
# print("\nDemographic Insights:\n", demographic_insights)
import pandas as pd

# Sample DataFrame creation (for demonstration)
data = {
    'employee_id': [1, 2, 3, 1, 2, 3],
    'department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'age': [25, 35, 30, 26, 36, 31],
    'benefit_type': ['medical', 'dental', 'vision', 'medical', 'vision', 'dental'],
    'enrollment_date': pd.to_datetime(['2022-01-15', '2022-01-16', '2022-02-01', '2022-01-15', '2022-01-16', '2022-02-01']),
    'usage_date': pd.to_datetime(['2022-02-10', '2022-02-15', None, '2022-03-12', '2022-03-15', None]),
}

df = pd.DataFrame(data)

# Data Cleaning
df['usage_date'].fillna('No Usage', inplace=True)

# Export DataFrames to CSV
enrollment_rates = df['benefit_type'].value_counts(normalize=True) * 100
enrollment_rates.to_csv('enrollment_rates.csv', header=True)

utilization_rates = df['usage_date'].value_counts(normalize=True) * 100
utilization_rates.to_csv('utilization_rates.csv', header=True)

demographic_insights = df.groupby(['department', 'benefit_type']).size().unstack(fill_value=0)
demographic_insights.to_csv('demographic_insights.csv', header=True)

print("Data exported successfully!")
