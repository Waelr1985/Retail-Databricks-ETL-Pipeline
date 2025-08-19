silver = spark.table("silver_superstore")

gold = (silver.groupBy("Category", "Region")
              .agg({"Sales": "sum", "Profit": "sum"}))

gold.write.format("delta").mode("overwrite").saveAsTable("gold_sales_summary")
