# PySpark Movie Reviews

Homework 1.2: a simple PySpark program that works on the IMDb dataset of 50,000 movie reviews.

## What the code does

1. Loads the CSV file into a PySpark DataFrame.
2. Prints the schema and shows the first 5 rows.
3. Removes rows where the review is empty or missing.
4. Counts the total reviews, then counts how many are positive and how many are negative.
5. Adds a new column `review_length` with the number of characters in each review.
6. Shows the reviews that are longer than 500 characters.
7. Saves the cleaned data, with the new column, as a new CSV in `output/cleaned_reviews`.

## Dataset

IMDb Dataset of 50K Movie Reviews from Kaggle:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

The dataset is in the `Dataset` folder of this repo (`Dataset/IMDB Dataset.csv`, about 63 MB). Before running the code, copy `IMDB Dataset.csv` into the same folder as `movie_reviews.py`.

## How to run

**On Google Colab (easiest):**

```
!pip install pyspark
```

Upload `IMDB Dataset.csv` and `movie_reviews.py`, then run:

```
!python movie_reviews.py
```

**On your own laptop:** you need Python and Java 17 installed. Then run:

```
pip install pyspark
python movie_reviews.py
```

## Files

- `movie_reviews.py`: the PySpark code
- `Dataset/IMDB Dataset.csv`: the movie review dataset
- `README.md`: this file
