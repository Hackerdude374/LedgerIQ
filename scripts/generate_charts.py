# Create the generate_charts.py script that uses matplotlib/seaborn to create charts

import os

charts_dir = "/mnt/data/LedgerIQ/scripts"
os.makedirs(charts_dir, exist_ok=True)

generate_charts_code = """import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_category_charts(df):
    output_dir = 'outputs/charts'
    os.makedirs(output_dir, exist_ok=True)

    summary = df.groupby('Category')['Amount'].sum().reset_index()

    # Bar Chart
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Amount', y='Category', data=summary, palette='viridis')
    plt.title('Total by Category')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'bar_chart.png'))
    plt.close()

    # Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(summary['Amount'], labels=summary['Category'], autopct='%1.1f%%', startangle=140)
    plt.title('Spending/Income Distribution')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'pie_chart.png'))
    plt.close()
"""

# Save the script
generate_charts_path = os.path.join(charts_dir, "generate_charts.py")
with open(generate_charts_path, "w") as f:
    f.write(generate_charts_code)

generate_charts_path
