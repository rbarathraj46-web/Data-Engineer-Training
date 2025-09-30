# Week 4 Databricks ETL
from pyspark.sql import functions as F

df = spark.read.csv("/FileStore/spark_logs.csv", header=True, inferSchema=True)
df = df.withColumn("timestamp", F.to_timestamp("timestamp"))

daily_summary = df.groupBy(F.to_date("timestamp").alias("date")).agg(F.sum("energy_kwh").alias("total_energy"))
daily_summary.display()

weekly_summary = df.groupBy(F.weekofyear("timestamp").alias("week")).agg(F.sum("energy_kwh").alias("weekly_energy"))
weekly_summary.display()

daily_summary.write.format("delta").mode("overwrite").save("/mnt/energy/daily_summary")
weekly_summary.write.csv("/mnt/energy/weekly_summary", header=True, mode="overwrite")
