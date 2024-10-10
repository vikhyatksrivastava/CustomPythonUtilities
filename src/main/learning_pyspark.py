from pyspark.sql import SparkSession
from pyspark.sql.functions import *


def read_file():
    spark = SparkSession.builder.appName("Learning PySpark").getOrCreate()
    df = spark.read.csv("../../../../postgre/Product_Source_file/tree.csv", header=True, inferSchema=True)
    print("----------Source Data-------------")
    df.show()
    transformed_df = df.alias('d1').join(df.alias('d2'), col('d1.col1') == col('d2.col2'))
    transformed_df.show()
    final_df = transformed_df.select('d1.col1')
    if df.isEmpty():
        print("No data found in the input files.")
        return
    else:
        if df.col("col2") is None:
            transformed_df = df.withColumn("col3", lit("Root"))
        elif df.col("col2") == df.col("col1"):
            transformed_df = df.withColumn("col3", lit("Branch"))
        else:
            transformed_df = df.withColumn("col3", lit("leaf"))
            transformed_df.show()


def main():
    read_file()


if __name__ == main():
    main()
