# analysis.py
# Author: Data Scientist
# Email: 24ds3000004@ds.study.iitm.ac.in

import marimo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cell 1: Generate synthetic data and create an interactive slider
# This cell creates the dataset and exposes a slider for user interaction.
df = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
})
df["y"] = 2 * df["x"] + np.random.normal(0, 2, size=100)

slider = marimo.ui.slider(1, 10, value=2, label="Slope (m)")

# Cell 2: Plot and dynamic markdown output based on slider value
# This cell depends on the slider value from Cell 1.
m = slider.value  # Dependency: uses slider value from Cell 1

fig, ax = plt.subplots()
ax.scatter(df["x"], df["y"], alpha=0.6, label="Data")
ax.plot(df["x"], m * df["x"], color="red", label=f"y = {m}x")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

marimo.display(fig)

marimo.display(
    marimo.md(f"""
### Interactive Linear Fit

- **Current slope (m):** `{m}`
- **Equation:** $y = {m}x$
- Adjust the slider to see how the fit changes.

_Email: 24ds3000004@ds.study.iitm.ac.in_
""")
)