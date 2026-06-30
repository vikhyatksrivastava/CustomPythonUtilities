from pathlib import Path
from pyspark.sql import SparkSession
import sys

# Create a local Spark session and reduce noisy logging
spark = SparkSession.builder.master("local[*]").appName("ReadCSV").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Resolve data path relative to the repository root
# data_file = Path(__file__).resolve().parents[2] / "data" / "employees.csv"

# if not data_file.exists():
# 	data_file = Path("data") / "employees.csv"
# 	if not data_file.exists():
# 		print(f"employees.csv not found (tried {data_file}).", file=sys.stderr)
# 		spark.stop()
# 		sys.exit(1)

# df = spark.read.csv(str(data_file), header=True, inferSchema=True)

df =spark.read.csv("..\\..\\data\\employees.csv", header=True, inferSchema=True)
df.show(truncate=False)

spark.stop()