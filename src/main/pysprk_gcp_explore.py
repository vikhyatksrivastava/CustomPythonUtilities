# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col  

# spark = SparkSession.builder.master("local[*]").appName("Tutorial").getOrCreate()
# csv_df = spark.read.csv("data\\employees.csv", header=True, inferSchema=True)

# csv_df.show(truncate=False)

# csv_to_parquet_path = "data\\employees_parquet"
# csv_df.write.mode("overwrite").parquet(csv_to_parquet_path)


import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run_batch():
    options = PipelineOptions()

    with beam.Pipeline(options=options) as p:
        (p
         | 'Read CSV' >> beam.io.ReadFromText('data\\employees.csv', skip_header_lines=1)
         | 'Split Columns' >> beam.Map(lambda line: line.split(','))
        #  | 'Print Rows' >> beam.Map(print)
         | 'Save locally' >> beam.io.WriteToText('output\\employees_output.txt')
        )

if __name__ == "__main__":
    run_batch()