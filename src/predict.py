import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("models/energy_model.pkl")

def get_sustainability_tips(pred_kwh, ac_hours, avg_temp):
    tips = []
    if ac_hours > 8:
        tips.append("🔥 AC hours zyada! Temp 24-26°C rakho + fan use karo.")
    if pred_kwh > 40:
        tips.append("⚡ High usage! Peak hours (6-10 PM) me appliances avoid karo.")
    if avg_temp > 30:
        tips.append("🌡️ Hot weather me blinds band rakho, ventilation use karo.")
    if not tips:
        tips.append("✅ Good job! Efficient usage continue karo.")
    return tips

def get_valid_input(prompt, type_func):
    while True:
        try:
            value = type_func(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Number daalo.")

def main():
    model = joblib.load(MODEL_PATH)
    
    print("Household Energy Predictor")
    print("=" * 40)
    
    month = get_valid_input("Month (1-12): ", int)
    avg_temp = get_valid_input("Avg temperature (°C): ", float)
    num_occupants = get_valid_input("Number of occupants: ", int)
    ac_hours = get_valid_input("AC usage hours/day: ", float)
    
    X_new = np.array([[month, avg_temp, num_occupants, ac_hours]])
    pred_kwh = model.predict(X_new)[0]
    
    print(f"\n📊 Predicted daily energy: {pred_kwh:.2f} kWh")
    print("\n💡 Sustainability Tips:")
    for tip in get_sustainability_tips(pred_kwh, ac_hours, avg_temp):
        print(f"  {tip}")
    
    print("\n🌍 This helps reduce CO₂ emissions + electricity bills!")

if __name__ == "__main__":
    main()
