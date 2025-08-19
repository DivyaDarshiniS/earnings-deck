# chart.py
# Author: Data Scientist
# Email: 24ds3000004@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate realistic synthetic data for customer engagement patterns
np.random.seed(42)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = [f"{h}:00" for h in range(8, 18)]  # 8 AM to 5 PM

# Simulate engagement scores (0-100) with business-like patterns
data = []
for day in days:
    base = np.random.randint(40, 70)
    pattern = base + np.random.normal(0, 10, len(hours))
    # Simulate higher engagement mid-day
    pattern[3:7] += np.random.randint(10, 20)
    data.append(np.clip(pattern, 0, 100))

df = pd.DataFrame(data, index=days, columns=hours)

# Create the heatmap
plt.figure(figsize=(8, 8))  # 512x512 pixels at dpi=64
ax = sns.heatmap(
    df,
    annot=True,
    fmt=".0f",
    cmap="RdYlGn",
    linewidths=0.5,
    cbar_kws={'label': 'Engagement Score'}
)

plt.title("Customer Engagement Heatmap", fontsize=18, pad=16)
plt.xlabel("Hour of Day", fontsize=14)
plt.ylabel("Day of Week", fontsize=14)
plt.tight_layout()

# Save the chart as PNG with exactly 512x512 pixels
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()