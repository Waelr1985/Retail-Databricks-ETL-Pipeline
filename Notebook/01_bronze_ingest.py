raw_df = spark.read.csv("/FileStore/tables/superstore.csv", header=True, inferSchema=True)
raw_df.write.format("delta").mode("overwrite").saveAsTable("bronze_superstore")
