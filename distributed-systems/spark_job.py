from pyspark.sql import SparkSession

def process_data():
    spark = SparkSession.builder.appName("RFMLProcessing").getOrCreate()
    df = spark.read.csv("radio_frequencies.csv", header=True, inferSchema=True)
    df = df.filter(df['signal_strength'] > 0)
    df.write.csv("processed_radio_frequencies.csv", header=True)
    spark.stop()

if __name__ == "__main__":
    process_data()
