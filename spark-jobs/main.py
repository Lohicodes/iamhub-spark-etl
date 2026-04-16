import json
from job import run_spark_job

def load_config():
    with open('config/dev.json') as f:
        return json.load(f)

if __name__ == "__main__":
    config = load_config()
    print(f"Running Spark job with config: {config}")
    run_spark_job()

    