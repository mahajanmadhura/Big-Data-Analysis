# Big-Data-Analysis

COMPANY: CODTECH IT SOLUTIONS

NAME: MADHURA MAHAJAN

INTERN ID: CT06DZ81

DOMAIN: DATA ANALYTICS

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION OF THE PROJECT :

📈 Scalable Sales Data Analysis using Dask

This project demonstrates how to perform scalable analysis on a large dataset using Dask, a parallel computing library in Python. It showcases big data processing capabilities and produces statistical insights and visualizations.

🔧 Technologies Used

* Dask (for scalable dataframe operations)
* Dask Distributed (for local cluster execution)
* Matplotlib (for plotting insights)
* Pandas & NumPy (for data creation)
* Parquet with Snappy compression (for optimized storage)

📊 Features / Analysis Performed

* Generates or loads a large synthetic sales dataset (100,000 rows)
* Calculates basic statistics (mean, std, min, max, etc.)
* Identifies top 5 product categories by revenue
* Saves results as a bar chart (`top_categories.png`)
* Stores the processed dataset in Parquet format for future use

🧠 Insights

This script illustrates how Dask can efficiently:

* Handle large datasets using chunked processing (`blocksize='25MB'`)
* Leverage multi-threading or multi-processing for performance
* Perform lazy computations that are only evaluated when needed
* Save data in highly compressed formats for downstream tasks

🚀 Scalability & Performance

This project is a great starting point to understand how distributed computing works in Python. By using Dask’s cluster-based execution model, the script can scale from a single machine to a full cluster without code changes.

Key benefits:

* Memory efficiency: Only chunks of the data are loaded into memory at a time.
* Parallelism: Multiple CPU cores are utilized for faster processing.
* Future-ready: Easily upgradable to cloud-based Dask clusters or integration with Hadoop-like systems.

*OUTPUT*:
-Top Catagories-
<img width="1792" height="892" alt="Image" src="https://github.com/user-attachments/assets/61f42299-2b7b-4bf3-b02f-4775c1862091" />
