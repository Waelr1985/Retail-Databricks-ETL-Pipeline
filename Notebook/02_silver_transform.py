from pyspark.sql.functions import col, to_date

bronze = spark.table("bronze_superstore")

silver = (bronze
          .withColumnRenamed("Order ID", "order_id")
          .withColumn("Order Date", to_date(col("Order Date"), "MM/dd/yyyy"))
          .withColumn("Ship Date", to_date(col("Ship Date"), "MM/dd/yyyy"))
          .dropna())

silver.write.format("delta").mode("overwrite").saveAsTable("silver_superstore")
