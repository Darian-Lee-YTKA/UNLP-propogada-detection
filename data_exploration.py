import pandas as pd

span_detection_df = pd.read_parquet("data/span_detection_train.parquet")
classification_df = pd.read_parquet("data/technique_classification_train.parquet")

print("span detection head")
print(span_detection_df.head())

print("classification head")
print(classification_df.head())


span_lengths = span_detection_df["content"].str.len()
classification_lengths = classification_df["content"].str.len()

print("🔤 Span Detection - Max Length:", span_lengths.max(), "Min Length:", span_lengths.min(), "Total Entries:", len(span_detection_df))
print("🕵️‍ ️Technique Classification - Max Length:", classification_lengths.max(), "Min Length:", classification_lengths.min(), "Total Entries:", len(classification_df))

print("column names: ", span_detection_df.columns)

