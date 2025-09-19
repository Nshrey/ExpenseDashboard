import pandas as pd
import os
def load_xlsx(Filepath):
    df = pd.read_excel(Filepath)
    df = df.drop("Value Dt", axis=1)
    df = df.rename(columns={"Narration":"Description","Chq./Ref.No.":"RefId","Withdrawal Amt.":"Debit","Deposit Amt.":"Credit","Closing Balance":"Balance"})
    df["Date"] = pd.to_datetime(df["Date"])
    return df