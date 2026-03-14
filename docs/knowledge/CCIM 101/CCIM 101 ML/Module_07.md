```yaml
---
module_id: Module 7
module_title: Investment Analysis with Financing
content_type: Mixed
key_concepts: ["Cash-on-Cash", "Leveraged IRR", "Equity Yield", "Before-Tax Cash Flow", "After-Tax Cash Flow", "Effective Tax Rate"]
equations_present: true
case_study_reference: Plaza Suites
---
```

# Module 7: Investment Analysis with Financing

## Overview
This module completes the real estate cash flow model by incorporating debt financing into both before-tax and after-tax analyses. The primary focus is on the impact of financial leverage on the investor's equity yield (IRR) and liquidity.

## Cash-on-Cash Return
Before-tax cash-on-cash is a measure of investment performance that shows the ratio between the first-year cash flow and the initial equity investment.

### Formula: Before-Tax Cash-on-Cash
$$Before-Tax\ Cash-on-Cash = \frac{First-year\ Cash\ Flow\ Before\ Tax}{Initial\ Investment}$$

## Plaza Suites Case Study: "With Financing" Assumptions
To conduct the leveraged analysis, the following debt and tax parameters are added to the Plaza Suites dataset:

| Data Point | Value |
| :--- | :--- |
| **Maximum Loan-to-Value (LTV)** | 75% |
| **Minimum Debt Service Coverage Ratio (DSCR)** | 1.2 |
| **Interest Rate** | 8.5% |
| **Amortization Period** | 20 years |
| **Loan Term** | 10 years |
| **Loan Costs** | 2% of loan amount |
| **Acquisition Costs** | $50,000 |
| **Purchase Price** | $1,000,000 |

### Calculated Financing Values (Plaza Suites)
Based on the underwriting criteria, the maximum loan amount is determined by the lesser of the LTV or DSCR limits.
*   **Loan Amount via LTV:** $750,000
*   **Loan Amount via DSCR:** $707,393
*   **Selected Loan Amount (Rounded):** $707,000
*   **Loan Costs:** $14,140
*   **Initial Equity Investment:** $357,140
*   **Annual Debt Service (ADS):** $73,626

## Plaza Suites: "With Financing/Before Tax" Analysis

### Cash-on-Cash Calculation
Using the first-year Cash Flow Before Tax (CFBT) of $14,774:
$$\frac{\$14,774}{\$357,140} = 4.14\%$$

### Before-Tax Equity Yield T-Bar (Table)
| Period (n) | Cash Flow ($) | Description |
| :--- | :--- | :--- |
| 0 | (357,140) | Initial Investment (Price + Acq + Costs - Loan) |
| 1 | 14,774 | Cash Flow Before Tax |
| 2 | 17,426 | Cash Flow Before Tax |
| 3 | 20,157 | Cash Flow Before Tax |
| 4 | 22,971 | Cash Flow Before Tax |
| 5 | 560,571 | Yr 5 CFBT ($25,870) + Sale Proceeds BT ($534,701) |
| **Result** | **13.13%** | **Before-Tax IRR** |

## Plaza Suites: "With Financing/After Tax" Analysis

### Tax Component Model (With Financing)
In the after-tax model with debt, interest and loan cost amortization are deducted to determine taxable income.
*   **Interest:** Deductible for tax purposes.
*   **Loan Costs Amortization:** Deductible straight-line over the term of the loan.
*   **Unamortized Loan Costs:** Deductible in the year the loan is paid off (at sale).

### After-Tax Equity Yield T-Bar (Table)
| Period (n) | Cash Flow ($) | Description |
| :--- | :--- | :--- |
| 0 | (357,140) | Initial Investment |
| 1 | 12,098 | Cash Flow After Tax |
| 2 | 13,550 | Cash Flow After Tax |
| 3 | 14,663 | Cash Flow After Tax |
| 4 | 15,779 | Cash Flow After Tax |
| 5 | 506,011 | Yr 5 CFAT ($16,552) + Sale Proceeds After Tax ($489,459) |
| **Result** | **10.07%** | **After-Tax IRR** |

## Effective Tax Rate with Financing
The effective tax rate measures how much taxes reduce the leveraged IRR.

| Metric | Value |
| :--- | :--- |
| Before-Tax Yield | 13.13% |
| After-Tax Yield | 10.07% |
| **Effective Tax Rate** | **23.31%** |

> ### Sample Problem: Calculating Tax Liability from Annual Operations with Debt
> **Scenario:** Net Operating Income is $88,400. Interest paid is $59,555. Cost Recovery is $20,672. Amortization of Loan costs is $1,414. Tax rate is 39.6%.
>
> **Calculation:**
> $$Taxable\ Income = \$88,400 - \$59,555 - \$20,672 - \$1,414 = \$6,759$$
> $$Tax\ Liability = \$6,759 \times 0.396 = \$2,676$$

***

**Analogy:**
Adding financing to your real estate analysis is like **turbocharging an engine.** The **Before-Tax IRR** is the increased speed you get from the turbo (leverage). However, the turbo also produces more heat (risk and tax complexity). The **After-Tax IRR** tells you exactly how much of that extra speed you actually keep after the engine's cooling system (the tax code) takes its share of the energy.