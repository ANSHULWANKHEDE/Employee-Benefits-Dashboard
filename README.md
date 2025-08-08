<h3>Employee Benefits Analysis</h3>
This project analyzes employee benefits enrollment, utilization, and demographics, and then exports the results into CSV files for reporting.

📌<h3> Project Overview </h3>
The dataset contains records of employees across different departments, their ages, benefit types, enrollment dates, and usage dates.
The goal is to:

Analyze enrollment rates for different benefit types.

Analyze utilization rates to see how often benefits are used.

Extract demographic insights to understand benefit preferences across departments.

📂 <h3>Files Generated </h3>
Running the script will generate the following CSV reports:

enrollment_rates.csv

Shows the percentage of employees enrolled in each benefit type.

utilization_rates.csv

Shows the percentage of benefits that were used (by date or “No Usage”).

demographic_insights.csv

Shows a cross-tabulation of departments vs. benefit types, with counts of enrollments.

⚙️ <h3>How It Works </h3>
Create the dataset

A sample dataset is created directly in the script (data dictionary).

In a real-world scenario, this can be loaded from a CSV file or SQL database.

Data Cleaning

Missing usage_date values are filled with "No Usage" for clarity.

Dates are converted into proper datetime format.

Analysis

Enrollment rates: Calculated as the percentage of each benefit_type.

Utilization rates: Percentage of each usage_date occurrence.

Demographics: Count of benefit enrollments grouped by department and benefit_type.

Export to CSV

Each analysis result is saved to a separate CSV file in the project directory.

🚀 </h3>How to Run </h3>
Make sure you have Python 3.x installed.

Install pandas if not already installed:

bash
Copy
Edit
pip install pandas
Run the script:

bash
Copy
Edit
python main.py
Check your project folder for:

enrollment_rates.csv

utilization_rates.csv

demographic_insights.csv

📊 </h3>Example Output (Enrollment Rates) </h3>
Benefit Type	Percentage
medical	33.33%
dental	33.33%
vision	33.33%

💡<h3> Customization</h3>
Replace the sample data dictionary with your actual dataset.

Change file export names as needed.

Extend the analysis to include:

Age group insights

Time-based utilization trends

Department-wise participation rates

