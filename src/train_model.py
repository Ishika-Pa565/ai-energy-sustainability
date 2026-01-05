import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

DATA_PATH = Path("data/processed/energy_usage_clean.csv")
MODEL_PATH = Path("models/energy_model.pkl")

def main():
    df = pd.read_csv(DATA_PATH)
    print("Data loaded:", df.shape)
    print(df.head())
    
    # Features and target
    feature_cols = ["month", "avg_temp", "num_occupants", "ac_hours"]
    X = df[feature_cols]
    y = df["kwh_consumption"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"\nModel trained!")
    print(f"MAE: {mae:.2f} kWh")
    print(f"R² Score: {r2:.3f}")
    
    # Save model
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
