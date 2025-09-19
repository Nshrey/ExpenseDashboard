import loaders.xls_loader
import pandas as pd
import os
def build_ledger(Path):
    xlsList = os.listdir(Path)
    print(xlsList)
build_ledger("C:/Users/nrao/Desktop/expense-dashboard/data/raw")