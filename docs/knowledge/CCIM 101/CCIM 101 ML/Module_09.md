```yaml
---
module_id: Module 9
module_title: Case Study: Summit Apartments
content_type: Case Study
key_concepts: ["Multifamily Analysis", "Unit Mix", "Market Rent", "Expense Ratio", "Exit Cap Rate", "Loan-to-Value", "DSCR"]
equations_present: true
case_study_reference: Summit Apartments
---
```

# Module 9: Case Study: Summit Apartments

## Case Study Overview
The Summit Apartments is a **25-unit** apartment complex located in Gainesville, FL. The property consists entirely of **two-bedroom, two-bath** units recently renovated.

## Data Dictionary: Financial Assumptions & Parameters

| Category | Key Parameter | Value | Notes / Description |
| :--- | :--- | :--- | :--- |
| **Property Info** | Total Units | 25 | All 2BR/2BA renovated units. |
| **Property Info** | Location | Gainesville, FL | 799 SW 2nd Ave. |
| **Acquisition** | Purchase Price | \$1,400,000 | \$56,000 per unit. |
| **Acquisition** | Acquisition Costs | \$20,000 | Capitalized at time zero. |
| **Operations** | Year 1 Market Rent | \$725 | Per unit, per month. |
| **Operations** | Rent Growth Rate | 3.00% | Annual increase projection. |
| **Operations** | Vacancy & Credit Loss | 6.00% | Stabilized market rate. |
| **Operations** | Other Income (Year 0) | \$1,200 | Estimated laundry income base. |
| **Operations** | Other Income Growth | 2.00% | Annual increase projection. |
| **Operations** | Operating Expense Ratio | 40.00% | Percentage of collected income (GOI). |
| **Taxation** | Ordinary Tax Rate | 39.60% | Marginal rate for individual investor. |
| **Taxation** | Capital Gains Rate | 20.00% | On appreciation over 12 months. |
| **Taxation** | Depreciation Recapture | 25.00% | Unrecaptured Section 1250 rate. |
| **Taxation** | Assessed Land Value | \$300,000 | Non-depreciable portion of basis. |
| **Taxation** | Assessed Improvements | \$700,000 | Depreciable portion of basis. |
| **Taxation** | Cost Recovery Period | 27.5 Years | Straight-line (Residential property). |
| **Financing** | Maximum LTV Ratio | 75.00% | Lending constraint 1. |
| **Financing** | Minimum DSCR | 1.20 | Lending constraint 2. |
| **Financing** | Loan Interest Rate | 8.00% | Nominal annual rate. |
| **Financing** | Amortization Period | 25 Years | Used to calculate debt service. |
| **Financing** | Loan Term | 5 Years | Results in balloon payment at EOY 5. |
| **Financing** | Loan Costs | 2.00% | Percent of total loan amount. |
| **Disposition** | Holding Period | 5 Years | Standard projection timeframe. |
| **Disposition** | Disposition Cap Rate | 9.00% | Applied to Year 6 NOI. |
| **Disposition** | Cost of Sale | 5.00% | Selling commissions and closing costs. |
| **Investment** | Target Yield (BT) | 15.00% | Investor's required before-tax return. |

## Initial Operational Projections (Year 1)

### Potential Rental Income (PRI) Calculation
$$PRI = 25\ units \times \$725/month \times 12\ months = \$217,500$$

### Net Operating Income (NOI) Calculation
| Component | Calculation | Amount ($) |
| :--- | :--- | :--- |
| Potential Rental Income | (Base Rent) | 217,500 |
| Less: Vacancy & Credit | (6% of PRI) | (13,050) |
| Plus: Other Income | (\$1,200 + 2%) | 1,224 |
| **Gross Operating Income** | | **205,674** |
| Less: Operating Expenses | (40% of GOI) | (82,270) |
| **Net Operating Income** | | **123,404** |

## Exit Strategy Calculation (End of Year 5)
The projected sale price is determined by capitalizing the Year 6 Net Operating Income:

$$Projected\ Sale\ Price = \frac{Year\ 6\ NOI}{Disposition\ Cap\ Rate}$$

$$Projected\ Sale\ Price = \frac{\$143,018}{0.09} = \$1,589,000\ (rounded)$$

## Investment Performance T-Bar: Without Financing / Before-Tax
| Period (n) | Cash Flow ($) | Description |
| :--- | :--- | :--- |
| 0 | (1,420,000) | Initial Investment (Price + Acq. Costs) |
| 1 | 123,404 | NOI |
| 2 | 127,099 | NOI |
| 3 | 130,904 | NOI |
| 4 | 134,824 | NOI |
| 5 | 1,648,411 | Yr 5 NOI (\$138,861) + Sale Proceeds BT (\$1,509,550) |
| **Result** | **10.20%** | **Before-Tax IRR (Unleveraged)** |

***

**Analogy:**
Initializing the Summit Apartments case study is like **programming a GPS for a long road trip.** The **Data Dictionary** provides the fixed coordinates (purchase price and location) and the performance constraints (speed limits/interest rates and fuel efficiency/expense ratios). Once these variables are entered, the analyst can map out the entire 5-year journey to determine if the destination (target yield) is reachable.