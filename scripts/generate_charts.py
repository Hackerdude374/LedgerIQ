import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_category_charts(df):
    output_dir = 'outputs/charts'
    os.makedirs(output_dir, exist_ok=True)

    summary = df.groupby('Category')['Amount'].sum().reset_index()

    # Bar Chart (works with positive and negative)
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Amount', y='Category', data=summary)
    plt.title('Total by Category')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'bar_chart.png'))
    plt.close()

    # Pie chart only for expenses (Amount < 0)
    expense_data = summary[summary['Amount'] < 0].copy()
    if not expense_data.empty:
        plt.figure(figsize=(6, 6))
        plt.pie(
            expense_data['Amount'].abs(),  # Convert negatives to positives for the pie
            labels=expense_data['Category'],
            autopct='%1.1f%%',
            startangle=140
        )
        plt.title('Expense Distribution')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'pie_chart.png'))
        plt.close()
