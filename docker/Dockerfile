from bitnami/spark:latest


user root


# Install pyspark
RUN pip install pyspark

# Set the working directory
WORKDIR /app

# Copy the Spark job script into the container
COPY . .

# Command to run the Spark job
CMD ["python", "spark-jobs/main.py"]