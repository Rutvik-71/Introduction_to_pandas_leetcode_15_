import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicate rows based on the email column and keep only the first occurrence
    return customers.drop_duplicates(subset=["email"], keep="first")