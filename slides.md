---
marp: true
theme: custom
paginate: true
footer: 'Contact: 24ds3000004@ds.study.iitm.ac.in'
style: |
  section {
    font-family: 'Segoe UI', Arial, sans-serif;
  }
  h1, h2 {
    color: #2d7ff9;
  }
  .byline {
    font-size: 1em;
    color: #555;
    margin-top: 1em;
  }
  .math {
    font-size: 1.2em;
    color: #1a1a1a;
    background: #eaf6ff;
    padding: 0.5em 1em;
    border-radius: 0.3em;
    display: inline-block;
  }
---

<!-- _class: lead -->

# Quarterly Earnings Report

**Interactive Stakeholder Briefing**

<div class="byline">Prepared by: Technical Consultant<br>
Contact: <a href="mailto:24ds3000004@ds.study.iitm.ac.in">24ds3000004@ds.study.iitm.ac.in</a>
</div>

---

### Headline Results (Markdown slide)

- **Revenue:** $12.4B *(+6.2% YoY)*
- **EPS (diluted):** $2.31 *(+9.5% YoY)*
- **Operating Margin:** 28.1%
- **Cash & Equivalents:** $7.9B

> _Note:_ This slide is authored in **Markdown** and rendered via Marp.

---

# Drivers of Performance

- <span class="fragment">Net interest income expansion on stable deposit costs</span>
- <span class="fragment">Fee income growth from wealth & payments</span>
- <span class="fragment">Lower credit costs vs. prior quarter</span>
- <span class="fragment">Operating leverage from tech efficiencies</span>

---

# Reproducible Metric (Code Sample)

```python
import pandas as pd
import numpy as np

# Example: rolling NIM (Net Interest Margin) estimator
# nim = (interest_income - interest_expense) / average_earning_assets

def rolling_nim(df, window=4):
    nim = (df["interest_income"] - df["interest_expense"]) / df["avg_earning_assets"]
    return nim.rolling(window=window, min_periods=1).mean()

q = pd.DataFrame({
    "interest_income": [1200, 1250, 1300, 1325],
    "interest_expense": [400, 420, 430, 450],
    "avg_earning_assets": [20000, 20500, 21000, 21500],
})
print(rolling_nim(q, window=2))
```

---

<!-- _backgroundImage: url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=800&q=80') -->
<!-- _color: white -->

# Architecture Overview

- Modular design  
- API-first approach  
- Scalable microservices  

---

# Financial Math

Net Present Value (NPV):

$$
\mathrm{NPV} = \sum_{t=0}^{T} \frac{CF_t}{(1+r)^t}
$$

Internal Rate of Return (IRR) is the rate $r$ such that $\mathrm{NPV}(r) = 0$.

---

# Algorithmic Complexity

<div class="math">
$$
T(n) = O(n \log n)
$$
</div>

- Efficient sorting algorithm  
- Handles large datasets  

---

# Outlook & Guidance

- <span class="fragment">Mid-single-digit revenue growth expected</span>
- <span class="fragment">Stable NIM with moderate rate sensitivity</span>
- <span class="fragment">Credit quality within historical ranges</span>

<small>Questions? Contact: 24ds3000004@ds.study.iitm.ac.in</small>

---

# Contact

- **Prepared by:** Technical Consultant  
- **Email:** [24ds3000004@ds.study.iitm.ac.in](mailto:24ds3000004@ds.study.iitm.ac.in)

---

<!-- _footer: '© 2025 Your Company' -->

# Thank You!

---

<style>
:root {
  --background: #f8fafc;
  --color: #22223b;
  --accent: #2d7ff9;
}
section {
  background: var(--background);
  color: var(--color);
}
h1, h2 {
  color: var(--accent);
}<!-- _backgroundImage: url('https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=800&q=80') -->
<!-- _color: white -->

# Architecture Overview

- Modular design  
- API-first approach  
- Scalable microservices  