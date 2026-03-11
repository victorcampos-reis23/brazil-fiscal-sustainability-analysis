# Brazil: Fiscal Sustainability & Debt Dynamics Analysis
"How much would the country need to grow to reduce the fiscal effort required for public account adjustment?"

## 📌 Project Overview

This project provides a quantitative simulation of the Primary Surplus required to stabilize the Brazilian Debt-to-GDP ratio (DBGG). Using a dynamic macroeconomic framework, it explores the trade-offs between real interest rates ($r$), GDP growth ($g$), and the current fiscal position.

The goal is to visualize the "Fiscal Policy Space" through a sensitivity matrix (Heatmap), identifying the boundaries where debt dynamics transition from sustainable to explosive (Fiscal Dominance risk).

## 🧮 Theoretical Framework

The stabilization of the debt-to-GDP ratio is governed by the following fundamental equation:

$$
b = \left( \frac{r - g}{1 + g} \right) \times d
$$

Where:
- **$b$**: Primary balance required to stabilize the debt-to-GDP ratio.
- **$r$**: Real interest rate (Ex-ante).
- **$g$**: Real GDP growth rate.
- **$d$**: Gross General Government Debt (DBGG) as a % of GDP.

**Fiscal Effort Calculation:**

$$
\text{Fiscal Effort} = b - \text{Current Primary Balance}
$$

#📊 Key Parameters (2024-2026 Outlook):

Current Debt ($d$): 78.7% (Current market/BCB data).
Target Debt (2026 Projection): ~84% (Scenario stress test).
Current Primary Balance (Estimated 2026): [Insert Value, e.g., -0.5% or 0.0%] of GDP.

## 🚀 Features
Automated Data Ingestion: Connects directly to the Central Bank of Brazil (SGS API) to fetch the latest DBGG and Selic figures.

Sensitivity Matrix: Generates a 2D grid exploring scenarios of real interest rates (from 6% to 11%) and GDP growth (from -1% to 4%).

Visualization: Professional Heatmap generated via Seaborn, highlighting "Danger Zones" (Red) and "Sustainability Zones" (Green).

## 🛠 Tech Stack
Python 3.13

Pandas & NumPy: Data manipulation and matrix calculus.

Matplotlib & Seaborn: Financial-grade data visualization.

python-bcb: Interface with the Central Bank of Brazil's API.

##📈 Results

The output heatmap (see below) demonstrates that under current high real interest rate conditions (approx. 9.74%), the required primary surplus to stabilize the debt significantly exceeds the current fiscal targets unless a substantial acceleration in GDP growth ($g$) occurs.



       
