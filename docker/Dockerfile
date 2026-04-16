from python:3.10


# Install Java (required for Spark)
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install pyspark
RUN pip install pyspark

# Set the working directory
WORKDIR /app

# Copy the Spark job script into the container
COPY . .

# Command to run the Spark job
CMD ["python", "spark-jobs/main.py"]