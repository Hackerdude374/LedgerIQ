import os

def prepare_bi_output(df):
    df.to_csv(os.path.join("outputs", "bi_output.csv"), index=False)
