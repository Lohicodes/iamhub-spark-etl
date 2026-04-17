from pyspark.sql import SparkSession

def run_spark_job():
    # Create a SparkSession
    

    spark = SparkSession.builder \
        .appName("test-job") \
        .getOrCreate()

    data = [("Lohith", 25), ("Rahul", 30), ("Anil", 35)]
    columns = ["name", "age"]

    df = spark.createDataFrame(data, columns)
    df.write.mode("overwrite").option("compression", "snappy").parquet("/app/output/sample_parquet_snappy")
        # Stop the SparkSession
    spark.stop()