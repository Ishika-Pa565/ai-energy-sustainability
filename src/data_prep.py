import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/energy_usage_raw.csv")
PROCESSED_PATH = Path("data/processed/energy_usage_clean.csv")

def main():
    df = pd.read_csv(RAW_PATH)
    print("Original data:")
    print(df.head())
    
    # Simple cleaning
    df = df.dropna()
    for col in ['month', 'num_occupants']:
        df[col] = df[col].astype(int)
    
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"\nCleaned data saved to {PROCESSED_PATH}")
    print("Cleaned data shape:", df.shape)

if __name__ == "__main__":
    main()
