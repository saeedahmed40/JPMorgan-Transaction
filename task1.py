import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    """Reads a CSV file into a DataFrame and returns it."""

    if not os.path.exists(file):
        raise FileNotFoundError(f"File not found: {file}")

    if not file.endswith('.csv'):
        raise ValueError("Invalid file type. Only CSV files are supported.")

    return pd.read_csv(file)
# Visualization Functions
def visual_1(df):
    """Creates two bar plots: one for overall transaction counts and another split by fraud status."""

    def transaction_counts(df):
        """Calculates the count of transactions per 'amount' (fill in the relevant column)."""
        return df['amount'].value_counts()

    def transaction_counts_split_by_fraud(df):
        """Calculates transaction counts per 'amount', split by 'isFraud' status."""
        return df.groupby(['amount', 'isFraud']).size().unstack()

    fig, axs = plt.subplots(2, figsize=(10, 12))  # Increased figure size for better readability

    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction Counts by amount') 
    axs[0].set_xlabel('amount') 
    axs[0].set_ylabel('Count')

    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction Counts by amount, Split by Fraud')
    axs[1].set_xlabel('amount')
    axs[1].set_ylabel('Count')
    axs[1].legend(title='isFraud')  # Add a legend to distinguish fraud vs. non-fraud

    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Annotate bars with their values
    for ax in axs:
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', xytext=(0, 5), textcoords='offset points')

    plt.show()  # Display the plot

def visual_2(df):
    """Creates a scatter plot between two numerical columns, highlighting potential outliers."""

    def query(df):
        """Filters the DataFrame based on some condition (you'll need to define this)."""
        return df[df['amount'] > 0]

    plot = query(df).plot.scatter(x='amount', y='oldbalanceOrg')
    plot.set_title('Scatter Plot of amount vs. oldbalanceOrg')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)

    plt.show()
# Main execution
df = exercise_0('transactions.csv')

visual_1(df)
visual_2(df)