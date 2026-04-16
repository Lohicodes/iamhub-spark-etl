FROM  python:3.10


# Install Java (required for Spark)
RUN apt-get update && apt-get install -y default-jdk && apt-get clean

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$JAVA_HOME/bin:$PATH

# Install pyspark
RUN pip install pyspark

# Set the working directory
WORKDIR /app

# Copy the Spark job script into the container
COPY . .

# Command to run the Spark job
CMD ["python", "spark-jobs/main.py"]