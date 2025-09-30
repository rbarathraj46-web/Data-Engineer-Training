from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, sum as spark_sum

spark = SparkSession.builder.appName("EnergyAggregation").getOrCreate()

df = spark.read.csv("spark_logs.csv", header=True, inferSchema=True)

df = df.withColumn("hour", hour(col("timestamp")))
df = df.withColumn("period", (col("hour").between(6,22)).cast("string"))

agg = df.groupBy("device_id", "period").agg(spark_sum("energy_kwh").alias("total_energy"))
agg.show()

top_devices = df.groupBy("device_id").agg(spark_sum("energy_kwh").alias("total_energy")).orderBy(col("total_energy").desc())
top_devices.show()
