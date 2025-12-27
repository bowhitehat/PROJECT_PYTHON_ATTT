import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

age = pd.read_csv("data/age_statistics.csv")
plt.bar(age['age_range'], age['count'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/age_chart.png")
plt.close()

privacy = pd.read_csv("data/privacy_statistics.csv")
plt.pie(privacy['count'], labels=privacy['privacy_concern'], autopct="%1.1f%%")
plt.savefig("images/privacy_chart.png")
plt.close()

device = pd.read_csv("data/device_statistics.csv")
plt.bar(device['device'], device['count'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/device_chart.png")
plt.close()

print("✅ Charts created")
