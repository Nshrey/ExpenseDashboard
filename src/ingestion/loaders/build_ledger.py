from xls_loader import load_xlsx
import pandas as pd
from pathlib import Path
import os

def build_ledger(raw_path):
    raw_dir = Path(raw_path)                       # .../data/raw
    processed_dir = raw_dir.parent / "processed"   # .../data/processed
    processed_dir.mkdir(parents=True, exist_ok=True)

    xls_list = sorted([n for n in os.listdir(raw_dir) if n.lower().endswith(".xls")])
    dflist = []

    for name in xls_list:
        df = load_xlsx(str(raw_dir / name))
        df["SourceFile"] = name
        df["Account"] = "Savings"
        dflist.append(df)

    concatdf = pd.concat(dflist, ignore_index=True)
    concatdf["Debit"]  = pd.to_numeric(concatdf["Debit"],  errors="coerce").fillna(0.0)
    concatdf["Credit"] = pd.to_numeric(concatdf["Credit"], errors="coerce").fillna(0.0)
    concatdf["Amount"] = (concatdf["Credit"] - concatdf["Debit"]).round(2)
    concatdf.loc[concatdf["Amount"].abs() < 1e-9, "Amount"] = 0.0

    concatdf = concatdf.sort_values("Date", ascending=True).reset_index(drop=True)
    concatdf = concatdf[["Date","Description","RefId","Debit","Credit","Balance","Amount","Account","SourceFile"]]

    ledger_path = processed_dir / "ledger.csv"
    concatdf.to_csv(ledger_path, index=False, encoding="utf-8")


build_ledger("C:/Users/nrao/Desktop/expense-dashboard/data/raw")