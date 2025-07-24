import dask.dataframe as dd
from dask.distributed import Client
import matplotlib.pyplot as plt
import os
from multiprocessing import freeze_support

def main():
    # Initialize Dask client with Windows-friendly config
    client = Client(
        n_workers=2,
        threads_per_worker=1,
        memory_limit='4GB',
        processes=False
    )

    try:
        print("\n🚀 Starting Dask Analysis")

        # Step 1: Load or generate sample data
        try:
            if not os.path.exists('sales_data.csv'):
                print("Creating sample data...")
                import numpy as np
                import pandas as pd
                dates = pd.date_range('2023-01-01', periods=100000, freq='H')
                pd.DataFrame({
                    'transaction_id': range(100000),
                    'customer_id': np.random.randint(1000, 9999, size=100000),
                    'amount': np.random.uniform(1, 1000, size=100000),
                    'product_category': np.random.choice(
                        ['Electronics', 'Clothing', 'Home', 'Food'],
                        size=100000
                    ),
                    'region': np.random.choice(
                        ['North', 'South', 'East', 'West'],
                        size=100000
                    ),
                    'date': dates
                }).to_csv('sales_data.csv', index=False)

            df = dd.read_csv(
                'sales_data.csv',
                dtype={
                    'transaction_id': 'int64',
                    'customer_id': 'int32',
                    'amount': 'float64',
                    'product_category': 'category',
                    'region': 'category'
                },
                parse_dates=['date'],
                blocksize='25MB'
            )
            print(f"✅ Loaded {len(df):,} records")
        except Exception as e:
            print(f"❌ Data loading failed: {str(e)}")
            return

        # Step 2: Perform analysis
        try:
            print("\n📊 Calculating basic statistics...")
            stats = df.describe().compute()
            print(stats)

            print("\n🏆 Top categories by revenue:")
            # ✅ Fix applied: added observed=True to silence FutureWarning
            top_cats = df.groupby('product_category', observed=True)['amount'].sum().nlargest(5).compute()
            print(top_cats)

            # Plot the results
            plt.figure(figsize=(10, 5))
            top_cats.plot(kind='bar', color='skyblue')
            plt.title('Top Revenue Categories')
            plt.ylabel('Total Revenue ($)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('top_categories.png')
            print("\n💾 Saved visualization: top_categories.png")

            # Save processed data
            output_dir = 'processed_data'
            os.makedirs(output_dir, exist_ok=True)
            df.to_parquet(
                output_dir,
                engine='pyarrow',
                compression='snappy'
            )
            print(f"💾 Saved processed data to: {output_dir}")

        except Exception as e:
            print(f"❌ Analysis failed: {str(e)}")

    finally:
        client.close()
        print("\n🎉 Analysis completed!")

if __name__ == '__main__':
    freeze_support()  # Required for Windows multiprocessing
    main()
