# Author: Vikhyat Srivastava
# Date: 23/09/2023
from pyspark.python.pyspark.shell import spark  #
import pyspark.sql.functions as F
from pyspark.sql import SparkSession


# This program reads file written in text format and counts number of lines and number of words in each line.

def readFile():
    spark = SparkSession.builder.appName("WriteDataFrameToHive").getOrCreate()
    path = "C:\Projects\postgre\PostGre_Projects\scripts\EmployeeDataAnalysis\employee_data.csv"
    df = spark.read.csv(path, header=True, inferSchema=True)
    # df.printSchema()
    # df.show()
    # print(f"Source file have {df.count()} records")
    # managers = df.filter(F.col("is_manager").cast("boolean") == True).select(F.col("employee_name"))
    # managers.show()
    average_salary = df.groupby(F.col("designation")).agg(F.round(F.avg("salary"), 2).alias("Average_Salary"))
    average_salary.show()

    average_salary.write.partitionBy("department").mode("overwrite").saveAsTable("employee_data_partitioned")
    average_salary.write.bucketBy(2, "employee_id").sortBy("employee_id").mode("overwrite").saveAsTable("employee_data_bucketed")

    average_salary.write.parquet("employee_data.parquet")
    average_salary.write.partitionBy("department").bucketBy(2, "employee_id").sortBy("employee_id").parquet(
        "employee_data_partitioned_bucketed.parquet")

    average_salary.write.csv("path/to/csv/file.csv")
    average_salary.write.option("header", "true").option("sep", ";").option("nullValue", "NA").csv("employee_data_custom.csv")


def main():
    readFile()


if __name__ == '__main__':
    main()
