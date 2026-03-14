```yaml
---
module_id: Module 5
module_title: Introduction to Tax
content_type: Mixed
key_concepts: ["Taxable Income", "Cash Flow After Tax", "Basis", "Cost Recovery", "Adjusted Basis", "Capital Gain", "Recapture", "Real World vs Tax World"]
equations_present: true
case_study_reference: Plaza Suites
---
```

# Module 5: Introduction to Tax

## Tax World Versus Real World
Taxation is defined by legislative bodies and tax codes, often differing from "Real World" economic logic. The primary differences involve the transfer of money and the timing of cash flows.

### Logical Distinctions
*   **Real World (Cash Flow):** Focuses on actual dollars going in and out of an investment. It represents the literal liquidity of the investor.
*   **Tax World (Taxable Income):** Focuses on how many of those dollars are subject to tax, how much is owed, and when it is paid.
*   **Non-Cash Expenses:** In the "Tax World," an investor can claim a **Cost-Recovery (Depreciation)** deduction for an asset wearing out, even though no money actually changed hands. This reduces taxable income without reducing "Real World" cash flow.
*   **Timing:** "Real World" payments like loan costs occur at time zero, but the "Tax World" requires them to be capitalized and deducted over the term of the loan.

## Mathematical Models

### Annual Taxable Income (Without Financing)
$$Taxable\ Income = Net\ Operating\ Income - Cost\ Recovery$$

### Cash Flow After Tax (CFAT)
$$Cash\ Flow\ After\ Tax = Cash\ Flow\ Before\ Tax - Tax\ Liability\ (Savings)$$

### Original Basis
$$Original\ Basis = Purchase\ Price + Acquisition\ Costs$$

## Cost Recovery (Depreciation) Schedules

### Class Life of Improvements
| Property Type | Class Life | Annual Percentage (Unadjusted) |
| :--- | :--- | :--- |
| Residential real estate | 27.5 years | 3.636% |
| Non-residential real estate | 39.0 years | 2.564% |



### IRS Cost-Recovery Percentages (Residential Property)
*Assumes acquisition on the first day of the tax year and uses the Mid-month Convention.*

| Period | Month 1 (%) | Month 2-12 (%) | Notes |
| :--- | :--- | :--- | :--- |
| Year Acquired | 3.485 | (Varies) | |
| Full Years Held | 3.636 | 3.636 | |
| Year of Sale | 0.152 | (Varies) | |

### IRS Cost-Recovery Percentages (Non-Residential Property)
| Period | Month 1 (%) | Month 2-12 (%) | Notes |
| :--- | :--- | :--- | :--- |
| Year Acquired | 2.461 | (Varies) | |
| Full Years Held | 2.564 | 2.564 | |
| Year of Sale | 0.107 | (Varies) | |

## Sample Problems

> ### Sample Problem 5-1a: Calculating Original Basis
> **Question:** A medical building is purchased for \$1,000,000 with \$50,000 in acquisition costs. What is the original basis?
> 
> **Solution:**
> $$\$1,000,000 + \$50,000 = \$1,050,000$$

> ### Sample Problem 5-1b: Allocating Basis
> **Question:** Using the basis from 5-1a (\$1,050,000) and a tax assessment showing \$160,000 land / \$640,000 improvements, allocate the basis.
> 
> **Solution:**
> *   Land Allocation: $(\$160,000 \div \$800,000) = 20\%$
> *   Improvement Allocation: $(\$640,000 \div \$800,000) = 80\%$
> *   **Land Basis:** $0.20 \times \$1,050,000 = \$210,000$
> *   **Improvement Basis:** $0.80 \times \$1,050,000 = \$840,000$

> ### Sample Problem 5-1d: Calculating Adjusted Basis
> **Question:** Calculate the adjusted basis at the end of Year 3 for a non-residential property with an original basis of \$1,050,000 and the following cost recovery: Yr 1: \$20,672; Yr 2: \$21,538; Yr 3: \$20,672.
> 
> **Solution:**
> | Year | Beginning Basis | Cost Recovery | End Adjusted Basis |
| :--- | :--- | :--- | :--- |
| 1 | \$1,050,000 | \$20,672 | \$1,029,328 |
| 2 | \$1,029,328 | \$21,538 | \$1,007,790 |
| 3 | \$1,007,790 | \$20,672 | **\$987,118** |

## Plaza Suites: "Without Financing/After Tax" Analysis
**Case Study Data:**
*   **Initial Investment:** \$1,050,000
*   **Improvement Value:** \$840,000
*   **Ordinary Income Tax Rate:** 39.6%
*   **Capital Gains Tax Rate:** 20%
*   **Cost-Recovery Recapture Rate:** 25%

### Five-Year Forecast of CFAT (Partial)
| Item | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Net Operating Income | \$88,400 | \$91,052 | \$93,784 | \$96,598 | \$99,496 |
| Less: Cost Recovery | (\$20,672) | (\$21,538) | (\$21,538) | (\$21,538) | (\$20,672) |
| **Real Estate Taxable Income** | **\$67,728** | **\$69,514** | **\$72,246** | **\$75,060** | **\$78,823** |
| Tax Liability (39.6%) | \$26,820 | \$27,528 | \$28,609 | \$29,724 | \$31,214 |
| **Cash Flow After Tax** | **\$61,580** | **\$63,524** | **\$65,175** | **\$66,874** | **\$68,282** |

### Plaza Suites Sale Proceeds After Tax (EOY 5)
| Component | Value | Notes |
| :--- | :--- | :--- |
| Projected Sale Price | \$1,206,000 | |
| Costs of Sale | (\$48,240) | |
| Adjusted Basis | (\$944,042) | |
| **Total Gain** | **\$213,718** | |
| Tax on Recapture (25%) | (\$26,490) | On \$105,958 recovery |
| Tax on Cap Gain (20%) | (\$21,552) | On \$107,760 appreciation |
| **Sale Proceeds After Tax**| **\$1,109,719** | |

**Resulting After-Tax IRR:** 7.16%

***

**Analogy:**
The difference between the Real World and Tax World is like **the difference between a pilot's actual view of the terrain and their radar screen.** The **Real World** (actual view) shows the literal cash changing hands—the physical landscape. The **Tax World** (radar) uses a different set of sensors (the tax code) to identify obstacles and opportunities (deductions like cost recovery) that may not be visible to the naked eye but drastically change how the "flight" (investment) is navigated.