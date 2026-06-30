import os
import sys

import pyspark.sql.functions as F
from pyspark.sql import SparkSession

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable


def run_query(df, category):
    category_map = F.create_map([F.lit(item) for pair in category.items() for item in pair])

    rated_df = df.withColumn(
        "member_rating",
        F.when(F.col("edu").isNull(), F.lit(0.0)).otherwise(
            F.aggregate(
                F.split(F.col("edu"), ":"),
                F.lit(0.0),
                lambda acc, code: acc + F.coalesce(F.element_at(category_map, code), F.lit(0.0)),
            )
        ),
    )

    club_ratings_df = (
        rated_df.groupBy("club_id")
        .agg(F.sum("member_rating").alias("total_rating"))
        .orderBy("club_id")
    )

    rated_df.show(truncate=False)
    club_ratings_df.show()


def main():
    spark = SparkSession.builder.master("local[*]").appName("Tutorial").getOrCreate()
    category = {"MM": 0.5, "CI": 0.5, "CO": 0.5, "CD": 1, "CL": 1, "CM": 1}
    data = [(1001, 211, 'MM:CI'), (1002, 215, 'CD:CI:CM'), (1002, 216, 'CL:CM'), (1002, 217, 'MM:CM'), (1003, 255, None), (1001, 216, 'CO:CD:CL:MM'), (1002, 210, None)]
    df = spark.sparkContext.parallelize(data).toDF(["club_id", "member_id", "edu"])
    run_query(df, category)
    spark.stop()

if __name__ == '__main__':
    main()

