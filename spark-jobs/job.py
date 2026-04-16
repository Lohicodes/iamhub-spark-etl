from pyspark.sql import SparkSession

def run_spark_job():
    # Create a SparkSession
    spark = SparkSession.builder.appName("SampleSparkJob").getOrCreate()

    # Read data from a CSV file
    input_path = "data/input/sample.csv"
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # Perform some transformations (e.g., filter and group by category)
    result_df = df.filter(df.price > 0.3).groupBy("category").count()

    # Show the results
    result_df.show()

    # Stop the SparkSession
    spark.stop()