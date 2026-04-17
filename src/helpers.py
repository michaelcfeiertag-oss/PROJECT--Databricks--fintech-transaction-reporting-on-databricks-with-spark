from pyspark.sql import functions as F

def add_amount_band(df, amount_col="amount"):
    return (
        df.withColumn(
            "amount_band",
            F.when(F.col(amount_col) < 100, "LOW")
             .when(F.col(amount_col) < 1000, "MEDIUM")
             .otherwise("HIGH")
        )
    )

def add_high_value_flag(df, amount_col="amount", threshold=1000):
    return df.withColumn("is_high_value", F.when(F.col(amount_col) >= threshold, F.lit(1)).otherwise(F.lit(0)))

def standardize_upper(df, cols):
    current = df
    for col_name in cols:
        current = current.withColumn(col_name, F.upper(F.trim(F.col(col_name))))
    return current
