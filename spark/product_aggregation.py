# Spark version of the product aggregation (run with spark-submit in a cluster).
# Kept as a reference implementation alongside the pure-Python transform.
def aggregate(spark, input_path, output_path):
    df = spark.read.option('header', True).csv(input_path)
    df.groupBy('product_id').sum('quantity', 'amount').write.mode('overwrite').parquet(output_path)
