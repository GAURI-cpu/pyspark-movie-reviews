from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

spark = SparkSession.builder.appName("MovieReviews").getOrCreate()

df = spark.read.csv(
    "IMDB Dataset.csv",
    header=True,
    inferSchema=True,
    multiLine=True,
    escape='"'
)

print("Schema of the dataset:")
df.printSchema()

print("First 5 rows:")
df.show(5, truncate=80)

clean_df = df.filter(
    col("review").isNotNull()
    & (trim(col("review")) != "")
    & col("sentiment").isin("positive", "negative")
)

total = clean_df.count()
print("Total number of reviews:", total)

print("Positive and negative review counts:")
clean_df.groupBy("sentiment").count().show()

final_df = clean_df.withColumn("review_length", length(col("review")))

long_reviews = final_df.filter(col("review_length") > 500)
print("Reviews longer than 500 characters:", long_reviews.count())
long_reviews.select("review", "sentiment", "review_length").show(5, truncate=80)

final_df.coalesce(1).write.mode("overwrite").csv("output/cleaned_reviews", header=True)
print("Saved cleaned data to output/cleaned_reviews")

spark.stop()
