

--- FILE START: Module_01.md ---

```yaml
---
module_id: Module 1
module_title: Overview of the Real Estate Universe
content_type: Concept
key_concepts: ["Capital Markets", "Space Markets", "Four Quadrants", "Debt vs. Equity", "Cap Rate", "Market Rent"]
equations_present: true
case_study_reference: None
---
```

# Module 1: Overview of the Real Estate Universe

## Space Market vs. Capital Market

The real estate universe is defined by the interplay between two distinct but interrelated markets that determine the value and usage of property.

### The Capital Market
The **Capital Market** is the arena where real estate competes for investor dollars against other asset classes like stocks and bonds. 
*   **Definition:** It is characterized by the interaction between the demand for real estate as an investment and the existing supply of space available for investment. 
*   **Pricing Mechanism:** The "price" of space in this market is often expressed as the **Capitalization Rate (Cap Rate)**, which represents what an investor is willing to pay for every dollar of Net Operating Income (NOI).
*   **Function:** Investors use the capital market to determine property values and required yields based on the perceived risk relative to other investment alternatives.

### The Space Market
The **Space Market** (also referred to as the User or Tenant Market) involves the physical use of real property.
*   **Definition:** It is defined by the interaction of current and potential users of space (demand) with the owners of existing space (supply).
*   **Pricing Mechanism:** The "price" resulting from this interaction is the **market rent** and specific lease terms.
*   **Dynamics:** Demand is driven by economic growth, employment, and business needs, while supply is often inelastic in the short run because new construction requires significant time to reach the market.

### Interaction and Valuation
The market rents determined in the space market provide the NOI that investors then analyze in the capital market to determine value.

**The Fundamental Value Formula:**
$$Value = \frac{NOI}{Cap\ Rate}$$

## The Four Quadrants of Real Estate Investment

Commercial real estate investment is categorized into four quadrants based on two dimensions: **Private vs. Public** markets and **Equity vs. Debt** capital.

| | Equity (Ownership) | Debt (Lending) |
| :--- | :--- | :--- |
| **Private Markets** | **Private Equity:** Individuals, Pension Funds, and Life Insurance Companies. | **Private Debt:** Commercial Banks and Life Insurance Companies. |
| **Public Markets** | **Public Equity:** Equity Real Estate Investment Trusts (REITs). | **Public Debt:** Commercial Mortgage-Backed Securities (CMBS) and Debt REITs. |

### Quadrant Definitions
*   **Private Market:** Involves investing directly in a physical asset, such as purchasing a specific building.
*   **Public Market:** Involves investing in securities, such as purchasing shares of stock in a REIT or a mortgage-backed bond.
*   **Equity:** Represents an ownership position in the property.
*   **Debt:** Represents an investment from the perspective of a lender, such as a mortgage loan.

***

**Analogy:**
The relationship between the Space Market and the Capital Market is like a **hydroelectric dam**. The **Space Market** is the river flow (tenants and rents) providing the raw energy, while the **Capital Market** is the turbine system (investors and cap rates) that converts that flow into measurable power (property value). If the river dries up or the turbines become inefficient, the resulting output changes.

--- FILE END ---


--- FILE START: Module_02.md ---

```yaml
---
module_id: Module 2
module_title: The Why and What of Real Estate Market Analysis
content_type: Theory/Framework
key_concepts: ["CCIM Strategic Analysis Model", "Geospatial Data", "Psychographics", "GIS", "Market Analysis", "STDBonline"]
equations_present: false
case_study_reference: None
---
```

# Module 2: The Why and What of Real Estate Market Analysis

## Overview
Market analysis is the foundation upon which financial analysis is built. For real estate decision-makers, the **outputs** of a market analysis serve as the essential **inputs** for the financial analysis.

## The CCIM Strategic Analysis Model
The **CCIM Strategic Analysis Model** is an iterative process used to evaluate the viability of a real estate project until a "Go/No Go" decision is reached. It consists of four interdependent components, each addressing a central question:

1.  **Market and Competitive Analysis:** Does the forecasted relationship between supply and demand for a specific property type in a specific location indicate success?
2.  **Location and Site Analysis:** Will the existing or proposed design of the improvements and the physical attributes of the site command the maximum market income?
3.  **Political and Legal Analysis:** Is the political climate and legal landscape conducive to a successful project over the foreseeable future?
4.  **Financial Analysis:** Does the projected financial performance indicate a return commensurate with the risk to satisfy the wealth expectations of the owner or user?

## Geospatial Data and Technology
In commercial real estate, the analysis of "location" is facilitated by geospatial data and **Geographic Information Systems (GIS)**.

### Geospatial Data
**Geospatial data** (also known as geographic information) is data that identifies the geographic location of features and boundaries on Earth.
*   It includes information regarding natural or constructed features and oceans.
*   Spatial data is typically stored as **coordinates and topology**, allowing it to be mapped.
*   GIS software allows analysts to organize, manipulate, and visualize this data.

### Data Factors and References
To be utilized within a GIS, data must have a reference to a location. Common factors and references include:
*   **Location References:** Latitude and longitude coordinates, ZIP codes, street addresses, and telephone numbers.
*   **Traditional Demographic Factors:** Household income, race, and age (typically collected by the U.S. Census).
*   **Descriptive Attributes:** Income levels and propensity to consume.

## Psychographics
**Psychographics**, also referred to as the **Lifestyle Segmentation Profile (LSP)**, represents a more advanced form of data that leverages the location component of GIS.

*   **Definition:** Psychographic segmentations are based on **consumption patterns** rather than just traditional demographic data like age or race.
*   **Predictive Power:** LSP is considered more accurate at predicting consumer behavior than standard demographic measurements.
*   **Application:** The CCIM Institute utilizes the **TAPESTRY** database (maintained by ESRI), which categorizes the U.S. market into 65 segments and 11 "LifeModes" based on attributes like affluence, education, and housing preferences.

## Four Levels of Geospatial Assistance
Geospatial technology (via platforms like STDBonline) assists CCIMs through four levels of analysis:
1.  **Record Keeping:** Organizing building and market records by geographic location.
2.  **Visualization:** Overlaying "layers" of information such as zoning, environmental constraints, and transportation infrastructure to determine highest and best use.
3.  **Tactical Analysis:** Identifying and segmenting specific factors that drive price appreciation in a neighborhood.
4.  **Strategic Decision Support:** Using historical information and spatial regression to forecast future development and pricing patterns for "go/no-go" decisions.

***

**Analogy:**
The CCIM Strategic Analysis Model is like a **four-legged stool**. The legs represent Market, Site, Political, and Financial analyses. If one leg is weak—such as failing to account for a political shift or a gap in market demand—the entire stool becomes unstable, and the investment decision is likely to fail. **Geospatial data** acts as the **level** used to ensure all four legs are resting on solid, accurately mapped ground.

--- FILE END ---


--- FILE START: Module_03.md ---

```yaml
---
module_id: Module 3
module_title: Investment Analysis Tools
content_type: Mixed
key_concepts: ["Time Value of Money", "Cash Flow Model", "IRR", "NPV", "Compounding", "Discounting"]
equations_present: true
case_study_reference: None
---
```

# Module 3: Investment Analysis Tools

## The Cash Flow Model
The cash flow model is a key tool for identifying a property's profit potential by picturing the amounts and timing of cash flows. It consists of four components:
1.  **Initial investment**
2.  **Cash flows from operations** during the holding period
3.  **Cash flow from disposition** (sale proceeds)
4.  **Holding period**

## Investor Preferences
Rational investors are guided by two basic preferences when risk is equal:
*   **More is better than less.**
*   **Sooner is better than later.**

### Comparison of Investment Cash Flows (Investor Preference Examples)

**Larger Periodic Cash Flows**
| Period (n) | Investment A ($) | Investment B ($) | Description |
| :--- | :--- | :--- | :--- |
| 0 | (1,000) | (1,000) | Initial Investment |
| 1 | 100 | 90 | Periodic PMT |
| 2 | 100 | 90 | Periodic PMT |
| 3 | 100 | 90 | Periodic PMT |
| 4 | 100 | 90 | Periodic PMT |
| 5 | 1,100 | 1,090 | PMT + Reversion |

**Earlier Periodic Cash Flows**
| Period (n) | Investment A ($) | Investment B ($) | Description |
| :--- | :--- | :--- | :--- |
| 0 | (1,000) | (1,000) | Initial Investment |
| 1 | 500 | 0 | Periodic PMT |
| 2 | 0 | 0 | Periodic PMT |
| 3 | 0 | 0 | Periodic PMT |
| 4 | 0 | 0 | Periodic PMT |
| 5 | 1,000 | 1,500 | PMT + Reversion |

## Time Value of Money (TVM)
TVM is the principle that a dollar received today is worth more than a dollar received in the future due to **No risk**, **Higher purchasing power (inflation)**, and **Opportunity cost**.

### Consistency of Components
To ensure accuracy, the number of periods ($n$) and the interest rate ($i$) must be consistent with the frequency of payments:

$$n = Years \times Periods\ Per\ Year$$
$$i = \frac{Annual\ Interest\ Rate}{Periods\ Per\ Year}$$

---

## Six Functions of the Dollar: Sample Problems

> ### Sample Problem 3-1: Compounding a Single Amount to a Future Value
> **Question:** An investor pays $100,000 today for land. It increases by 9% annually. What is it worth at the end of Year 10?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (100,000) | Present Value (PV) |
> | 1-10 | 0 | Periodic Payment (PMT) |
> | 10 | 236,736.37 | Future Value (FV) at 9% |

> ### Sample Problem 3-2: Compounding an Annuity to a Future Value
> **Question:** If $10,000 is invested at the end of each year for 10 years at 10% interest, what is the value at the end of Year 10?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | 0 | Present Value (PV) |
> | 1-10 | (10,000) | Periodic Payment (PMT) |
> | 10 | 159,374.25 | Future Value (FV) at 10% |

> ### Sample Problem 3-3: Determining a Sinking Fund Payment
> **Question:** A parking lot needs $50,000 for resurfacing in 3 years. How much must be invested monthly at 10% annual interest?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | 0 | Present Value (PV) |
> | 1-36 | (1,196.69) | Required Monthly PMT |
> | 36 | 50,000 | Future Value (FV) Target |

> ### Sample Problem 3-4: Discounting a Single Future Amount to a Present Value
> **Question:** You anticipate selling land for $1,300,000 in 3 years. What would you pay today to achieve a 10% annual yield?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (976,709.24) | Calculated Present Value (PV) |
> | 1-3 | 0 | Periodic Payment (PMT) |
> | 3 | 1,300,000 | Future Value (FV) at 10% |

> ### Sample Problem 3-5: Discounting an Annuity to a Present Value
> **Question:** What is the value today of $1,000 monthly payments for 3 years, discounted at 10% annually?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (30,991.24) | Calculated Present Value (PV) |
> | 1-36 | 1,000 | Periodic Payment (PMT) |
> | 36 | 0 | Future Value (FV) |

> ### Sample Problem 3-6: Determining a Series of Equal Payments Necessary to Amortize a Present Value
> **Question:** What is the monthly payment on a $250,000 loan for 25 years at 10% interest?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (250,000) | Loan Amount (PV) |
> | 1-300 | 2,271.75 | Calculated Monthly PMT |
> | 300 | 0 | Future Value (FV) |

---

## Discounted Cash Flow (DCF): Internal Rate of Return (IRR)

> ### Sample Problem 3-7: Calculating the IRR of a Single Amount Received
> **Question:** Investor pays $10,000 for an investment today; receives $28,300 at the end of Year 10. What is the IRR?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (10,000) | Initial Investment (PV) |
> | 1-10 | 0 | Periodic Payment (PMT) |
> | 10 | 28,300 | Sale Proceeds (FV) |
> | **Result** | **10.96%** | **Calculated IRR** |

> ### Sample Problem 3-8a: Calculating the IRR of an Annuity Plus Single Amount Received
> **Question:** Initial investment of $20,000; income of $3,000/year for 5 years; sold for $20,000.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (20,000) | Initial Investment |
> | 1-5 | 3,000 | Periodic PMT |
> | 5 | 20,000 | Sale Proceeds (Reversion) |
> | **Result** | **15.00%** | **Calculated IRR** |

> ### Sample Problem 3-8b: Calculating the IRR of an Annuity Plus Single Amount Received
> **Question:** Initial investment of $20,000; income of $3,000/year for 5 years; sold for $16,000.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (20,000) | Initial Investment |
> | 1-5 | 3,000 | Periodic PMT |
> | 5 | 16,000 | Sale Proceeds (Loss in value) |
> | **Result** | **11.84%** | **Calculated IRR** |

> ### Sample Problem 3-8c: Calculating the IRR of an Annuity Plus Single Amount Received
> **Question:** Initial investment of $20,000; income of $3,000/year for 5 years; sold for $24,000.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (20,000) | Initial Investment |
> | 1-5 | 3,000 | Periodic PMT |
> | 5 | 24,000 | Sale Proceeds (Appreciation) |
> | **Result** | **17.81%** | **Calculated IRR** |

> ### Sample Problem 3-9a: Calculating the IRR with Variable Cash Flows
> **Question:** Initial investment of $60,000; variable cash flows over 10 years; sold for $45,000.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (60,000) | Initial Investment |
> | 1 | 10,000 | Cash Flow |
> | 2 | 9,000 | Cash Flow |
> | 3 | 8,000 | Cash Flow |
> | 4 | 7,000 | Cash Flow |
> | 5 | 6,000 | Cash Flow |
> | 6 | 5,000 | Cash Flow |
> | 7 | 4,000 | Cash Flow |
> | 8 | 3,000 | Cash Flow |
> | 9 | 2,000 | Cash Flow |
> | 10 | 46,000 | $1,000 CF + $45,000 Proceeds |
> | **Result** | **8.61%** | **Calculated IRR** |

> ### Sample Problem 3-9b: Recalculating IRR Changing the Sale Proceeds
> **Question:** Same as 3-9a, but sale proceeds increase from $45,000 to $70,000.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 10 | 71,000 | $1,000 CF + $70,000 Proceeds |
> | **Result** | **11.62%** | **New Calculated IRR** |

> ### Sample Problem 3-10a: Proof of IRR for Investment A
> **Question:** Initial investment $10,000; $0 years 1-3; $14,641 year 4.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (10,000) | Initial Investment |
> | 1-3 | 0 | PMT |
> | 4 | 14,641 | Reversion |
> | **Result** | **10.00%** | **Calculated IRR** |

---

## Net Present Value (NPV)

> ### Sample Problem 3-11a: Measuring Investment Performance Using NPV with a Target Yield of 7 Percent
> **Question:** Investment $10,000; CFs: Yr1 $0, Yr2 $1,000, Yr3 $5,000, Yr4 $7,931. Target Yield = 7%.
> 
> | Period (n) | Cash Flow ($) | PV at 7% ($) |
> | :--- | :--- | :--- |
> | 0 | (10,000) | (10,000) |
> | 1 | 0 | 0 |
> | 2 | 1,000 | 873 |
> | 3 | 5,000 | 4,081 |
> | 4 | 7,931 | 6,051 |
> | **NPV** | **$1,005.45** | **Positive NPV** |

> ### Sample Problem 3-11b: Measuring Investment Performance Using NPV with a Target Yield of 13 Percent
> **Question:** Same cash flows as 3-11a. Target Yield = 13%.
> 
> | Period (n) | Cash Flow ($) | PV at 13% ($) |
> | :--- | :--- | :--- |
> | 0 | (10,000) | (10,000) |
> | 1 | 0 | 0 |
> | 2 | 1,000 | 783 |
> | 3 | 5,000 | 3,465 |
> | 4 | 7,931 | 4,864 |
> | **NPV** | **($887.37)** | **Negative NPV** |

> ### Sample Problem 3-11c: Measuring Investment Performance Using NPV with a Target Yield of 10 Percent
> **Question:** Same cash flows as 3-11a. Target Yield = 10%.
> 
> | Period (n) | Cash Flow ($) | PV at 10% ($) |
> | :--- | :--- | :--- |
> | 0 | (10,000) | (10,000) |
> | 1 | 0 | 0 |
> | 2 | 1,000 | 826 |
> | 3 | 5,000 | 3,757 |
> | 4 | 7,931 | 5,417 |
> | **NPV** | **$0.00** | **Yield Equals Target** |

> ### Sample Problem 3-12: Using the NPV Function to Calculate Investment Value
> **Question:** Calculate price to pay for Year 1-4 cash flows ($0, $1k, $5k, $7.9k) to earn 10%.
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | 0 | Solve for NPV |
> | 1 | 0 | Cash Flow |
> | 2 | 1,000 | Cash Flow |
> | 3 | 5,000 | Cash Flow |
> | 4 | 7,931 | Cash Flow |
> | **NPV** | **$10,000.00** | **Investment Value** |

***

**Analogy:**
Using **IRR and NPV** to compare investments is like **checking the speed and the fuel efficiency** of different cars. The **IRR** tells you the "speed" (percentage return) at which your capital is working for you. The **NPV** tells you the "fuel efficiency" (total value in today's dollars) relative to your minimum requirements. If the NPV is positive, you are getting more than enough "fuel" (wealth) to reach your destination at the speed you require.

--- FILE END ---


--- FILE START: Module_04.md ---

```yaml
---
module_id: Module 4
module_title: Introduction to the Real Estate Cash Flow Model
content_type: Mixed
key_concepts: ["Net Operating Income", "NOI", "APOD", "Gross Rent Multiplier", "Direct Capitalization", "Cap Rate", "Cash Flow Before Tax"]
equations_present: true
case_study_reference: Plaza Suites
---
```

# Module 4: Introduction to the Real Estate Cash Flow Model

## Plaza Suites Financial Assumptions
*   **Type of Property:** Office Building
*   **Size of Property:** Small office building (Specific square footage not provided)
*   **Purchase Price:** $1,000,000
*   **Acquisition Costs:** $50,000
*   **Initial Investment:** $1,050,000
*   **Year One PRI:** $145,000
*   **PRI Annual Growth Rate:** 3 percent
*   **Annual Vacancy and Credit Loss Projection:** 8 percent
*   **Year One Operating Expenses:** $45,000
*   **Operating Expenses Annual Growth Rate:** 3 percent
*   **Holding Period:** Five years
*   **Projected End of Year Five Sale Price:** Capitalize year six NOI at 8.5 percent
*   **End of Year Five Cost of Sale:** 4 percent of sale price

## Financial Formulas

### Net Operating Income (NOI)
$$NOI = (Potential\ Rental\ Income - Vacancy\ and\ credit\ losses) + Other\ Income - Operating\ Expenses$$

### Direct Capitalization (IRV)
$$Income\ (I) = Rate\ (R) \times Value\ (V)$$
$$Rate\ (R) = \frac{Income\ (NOI)}{Value\ (Investment\ Value)}$$
$$Value\ (V) = \frac{Income\ (NOI)}{Rate\ (Cap\ Rate)}$$

### Gross Rent Multiplier (GRM)
$$Investment\ Value = Forecast\ of\ first-year\ PRI \times GRM$$
$$GRM = \frac{Investment\ Value}{Year\ one\ PRI}$$

## Annual Property Operating Data (APOD): Plaza Suites

| Line | Item | % of PRI/GOI | Annual Figures ($) |
| :--- | :--- | :--- | :--- |
| 1 | **POTENTIAL RENTAL INCOME** | | **145,000** |
| 2 | Less: Vacancy & Cr. Losses | 8% of PRI | 11,600 |
| 3 | **EFFECTIVE RENTAL INCOME** | | **133,400** |
| 4 | Plus: Other Income (collectable) | | 0 |
| 5 | **GROSS OPERATING INCOME** | | **133,400** |
| 6-28 | Operating Expenses (Subtotaled) | | |
| 29 | **TOTAL OPERATING EXPENSES** | | **45,000** |
| 30 | **NET OPERATING INCOME** | | **88,400** |
| 31 | Less: Annual Debt Service | | 0 |
| 35 | **CASH FLOW BEFORE TAXES** | | **88,400** |

## Without Financing / Before Tax Cash Flow Models

### Plaza Suites Holding Period
| Period (n) | Cash Flow ($) | Description |
| :--- | :--- | :--- |
| 0 | (1,050,000) | Initial investment (Price + Acq. Costs) |
| 1 | 88,400 | Cash flow before tax |
| 2 | 91,052 | Cash flow before tax |
| 3 | 93,784 | Cash flow before tax |
| 4 | 96,597 | Cash flow before tax |
| 5 | 1,257,255 | Year 5 NOI ($99,495) + Sale proceeds before tax ($1,157,760) |

> ### Sample Problem 4-1a: Determining Investment Value Using GRM
> **Question:** If a property is forecasted to have $100,000 first-year PRI and the potential buyer's GRM requirement is seven, what is the investment value of the property?
>
> **Solution:**
> $$\$100,000 \times 7 = \$700,000$$

> ### Sample Problem 4-1b: Measuring Investment Performance Using GRM
> **Question:** If a property is offered for sale at $700,000 and the PRI forecast for year one is $100,000, what is the GRM investment performance measure?
>
> **Solution:**
> $$\$700,000 \div \$100,000 = 7\ GRM$$

> ### Sample Problem 4-2a: Determining Investment Value Using Direct Capitalization
> **Question:** An investor is considering purchasing a property with a forecasted first-year NOI of $50,000. The investor has established a cap rate requirement of 9.75 percent. What would this investor consider paying for the property?
>
> **Solution:**
> $$\$50,000 \div 0.0975 = \$512,821$$

> ### Sample Problem 4-2b: Measuring Investment Performance Using Direct Capitalization
> **Question:** Assume the investor is considering purchasing a property that is priced at $512,821 with a forecasted first-year NOI of $50,000. What is the cap rate?
>
> **Solution:**
> $$\$50,000 \div \$512,821 = 0.0975\ (9.75\%)$$

> ### Sample Problem 4-2c: The Relationship Between Cap Rate and Return on Investment
> **Property A (Value $100,000, Yr 1 NOI $10,000, Sale $100,000)**
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (100,000) | Purchase Price |
> | 1 | 110,000 | NOI ($10,000) + Sale ($100,000) |
> | **Result** | **10%** | **Yield (i)** |
> | **Cap Rate**| **10%** | **$10,000 / $100,000** |
>
> **Property B (Value $100,000, Yr 1 NOI $5,000, Sale $105,000)**
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (100,000) | Purchase Price |
> | 1 | 110,000 | NOI ($5,000) + Sale ($105,000) |
> | **Result** | **10%** | **Yield (i)** |
> | **Cap Rate**| **5%** | **$5,000 / $100,000** |
>
> **Property C (Value $100,000, Yr 1 NOI $15,000, Sale $95,000)**
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (100,000) | Purchase Price |
> | 1 | 110,000 | NOI ($15,000) + Sale ($95,000) |
> | **Result** | **10%** | **Yield (i)** |
> | **Cap Rate**| **15%** | **$15,000 / $100,000** |

--- FILE END ---


--- FILE START: Module_05.md ---

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

--- FILE END ---


--- FILE START: Module_06.md ---

```yaml
---
module_id: Module 6
module_title: Financing Real Estate Investments
content_type: Mixed
key_concepts: ["Financial Leverage", "Loan-to-Value (LTV)", "Debt Service Coverage Ratio (DSCR)", "Mortgage Constant", "Amortization", "Effective Cost of Funds"]
equations_present: true
case_study_reference: Plaza Suites
---
```

# Module 6: Financing Real Estate Investments

## Financial Leverage Definitions

Financial leverage measures the degree to which debt is used to finance an investment, typically to increase the expected return on equity.

*   **Positive (Favorable) Leverage:** Occurs when an investor expects a higher return on equity than if the investment were purchased on an all-cash basis. This happens when the unleveraged internal rate of return (IRR) on the property is greater than the cost of debt.
*   **Negative (Unfavorable) Leverage:** Occurs when the investor expects to receive a lower return on equity than if they had paid all cash. This happens when the projected unleveraged IRR on the property is less than the cost of debt.
*   **Neutral Leverage:** Exists when the expected unleveraged IRR on the property is equal to the cost of debt.

## Financial Formulas

### Loan-to-Value (LTV) Ratio
$$LTV\ Ratio = \frac{Loan\ Amount}{Property\ Value}$$

### Debt Service Coverage Ratio (DSCR)
$$DSCR = \frac{Net\ Operating\ Income (NOI)}{Annual\ Debt\ Service (ADS)}$$

### Mortgage Constant
The mortgage constant represents the "payment rate" of the loan, covering both return on and return of capital.
$$Mortgage\ Constant = \frac{Annual\ Debt\ Service (ADS)}{Initial\ Loan\ Amount}$$

### Borrower's Effective Cost of Funds (After-Tax)
$$After-Tax\ Cost\ of\ Funds = Before-Tax\ Cost\ of\ Funds \times (1 - Ordinary\ Tax\ Rate)$$

## Amortization Schedules

> ### Sample Problem 6-9: Amortization Schedule
> **Scenario:** A \$100,000 loan with a 25-year amortization period, 8% annual interest, and monthly payments.
>
> | Year | BOY Balance ($) | Interest ($) | Principal ($) | EOY Balance ($) |
> | :--- | :--- | :--- | :--- | :--- |
> | 1 | 100,000.00 | 7,952.69 | 1,309.15 | 98,690.85 |
> | 2 | 98,690.85 | 7,844.04 | 1,417.80 | 97,273.05 |
> | 3 | 97,273.05 | (Calculated) | (Calculated) | (Calculated) |
>

## Sample Problems and Cash Flow Models

> ### Sample Problem 6-1a: Calculating Leverage (Unleveraged)
> **Question:** A property purchased for \$100,000 has an NOI of \$8,000 for five years. No change in value. What is the IRR?.
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (100,000) | Initial Investment |
> | 1 | 8,000 | NOI |
> | 2 | 8,000 | NOI |
> | 3 | 8,000 | NOI |
> | 4 | 8,000 | NOI |
> | 5 | 108,000 | NOI + Sale Proceeds |
> | **Result** | **8.00%** | **Unleveraged IRR** |
>

> ### Sample Problem 6-4: Solving for a Periodic Payment
> **Question:** What is the monthly payment on a fully amortized \$10,000 loan at 7% interest over 10 years?.
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | 10,000 | Loan Amount (PV) |
> | 1-120 | (116.11) | Periodic Payment (PMT) |
> | 120 | 0 | Future Value (FV) |
>

> ### Sample Problem 6-12a: Borrower's Effective Cost of Funds
> **Question:** Calculate the effective cost for a \$100,000 loan at 8% interest, 25-year term, with 2 points and \$2,054 in third-party costs.
>
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | 95,946 | Net Loan Proceeds (\$100k - \$2k points - \$2,054 costs) |
> | 1-300 | (771.82) | Monthly Payment |
> | 300 | 0 | Future Value |
> | **Result** | **8.49%** | **Effective Cost of Funds** |
>

***

**Analogy:**
Financial leverage is like a **lever and a fulcrum** used to lift a heavy object. The **equity** is your physical strength, the **debt** is the length of the lever, and the **property's return** is the weight you are trying to lift. If the lever is positioned correctly (**positive leverage**), you can lift much more weight (generate higher returns) than with your strength alone. However, if the weight is too heavy for the lever's strength (**negative leverage**), the lever can snap back and cause injury (loss of equity).

--- FILE END ---


--- FILE START: Module_07.md ---

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

--- FILE END ---


--- FILE START: Module_08.md ---

```yaml
---
module_id: Module 8
module_title: Comparing Real Estate Investments
content_type: Mixed
key_concepts: ["NPV", "IRR", "Capital Accumulation", "Discount Rates", "Risk Premium", "Reinvestment Rate", "Size Disparity"]
equations_present: true
case_study_reference: Summit Apartments
---
```

# Module 8: Comparing Real Estate Investments

## Comparison: NPV vs. IRR

Both Net Present Value (NPV) and Internal Rate of Return (IRR) are fundamental tools for economic decision-making, yet they serve different purposes in evaluating real estate performance.

### Net Present Value (NPV)
*   **Definition:** The sum of the discounted values of all cash flows (including the initial investment at period zero) using a specified target yield or discount rate.
*   **Decision Rule:** 
    *   **Positive NPV:** The investment exceeds the target yield.
    *   **Zero NPV:** The investment achieves exactly the target yield.
    *   **Negative NPV:** The investment fails to achieve the target yield.
*   **Application:** Used to determine **Investment Value** (what a specific investor should pay to achieve a required return).

### Internal Rate of Return (IRR)
*   **Definition:** The annualized percentage rate earned on each dollar while it remains in an investment.
*   **Function:** It is the discount rate that makes the NPV of all cash flows equal to zero.
*   **Application:** Used to compare the yield of different investment alternatives.

## Pros and Cons of Using Internal Rate of Return (IRR)

| Feature | Description |
| :--- | :--- |
| **Pro: Comprehensive** | Answers the four basic questions: How many dollars go in/out, and when? |
| **Pro: Comparison Tool** | Provides a single percentage rate (yield) to compare mutually exclusive alternatives. |
| **Con: Reinvestment Assumption** | Fails to account for the reinvestment of positive cash flows at rates external to the IRR. |
| **Con: Cash Flow Configuration** | Limitations arise when discounting negative cash flows or handling multiple sign changes. |
| **Con: Disparity Issues** | Does not account for **Size Disparity** (different initial investments) or **Time Disparity** (different holding periods). |

## The Capital Accumulation Process

Capital accumulation is used to mitigate the limitations of IRR by adjusting all investments to a common denominator of two cash flows: one initial investment and one terminal sum.

### Mathematical Formulas

**1. Reinvestment of Periodic Cash Flows (Compounding to Future Value):**
$$FV = CF \times (1 + r)^n$$
*Where $r$ is the reinvestment rate and $n$ is the years remaining in the holding period.*

**2. Annual Compound Growth Rate of Capital:**
$$i = \left( \frac{Terminal\ Capital\ Accumulation}{Initial\ Investment} \right)^{1/n} - 1$$
*Where $i$ is the compound growth rate and $n$ is the holding period.*

---

## Sample Problems: Module 8

> ### Sample Problem 8-1c: Calculating NPV and IRR
> **Question:** An investor can purchase land for \$500,000. It produces \$25,000/year for 5 years and sells for \$750,000. What is the NPV at a 10% discount rate and what is the IRR?
> 
> | Period (n) | Cash Flow ($) | Description |
> | :--- | :--- | :--- |
> | 0 | (500,000) | Initial Investment |
> | 1 | 25,000 | Annual Rent |
> | 2 | 25,000 | Annual Rent |
> | 3 | 25,000 | Annual Rent |
> | 4 | 25,000 | Annual Rent |
> | 5 | 775,000 | Rent (\$25k) + Sale (\$750k) |
> 
> **Results:**
> *   **NPV @ 10%:** \$60,461 (Investment is worth \$560,461 at 10% target).
> *   **IRR:** 12.75%.

> ### Sample Problem 8-4: Reinvestment of Positive Cash Flows
> **Question:** Compare Investment A (no interim cash flow) and Investment B (interim cash flow) if both have a 10% IRR.
> 
> **Investment A:** \$10,000 grows to \$14,641 in 4 years.
> **Investment B:** \$10,000 initial; \$1,000/year for 4 years; \$10,000 reversion at Year 4.
> 
> **Scenario (8% Reinvestment Rate):**
> *   Investment A Accumulation: **\$14,641**
> *   Investment B Accumulation: **\$14,506** (Interim \$1k payments earned only 8% vs. A's internal 10%).

> ### Sample Problem 8-5: Adjusting for Size Disparity
> **Question:** If Investment A requires \$10,000 and Investment B requires \$15,000, how are they compared for capital accumulation?
> 
> **Solution:** Combine Investment A with an **External Investment** of \$5,000 (the difference in size).
> *   If the reinvestment rate is **12%** (higher than the 10% IRR), Investment A (Combined) will produce a higher capital accumulation than Investment B.

---

## Risk Considerations in Selection
Investors select a discount rate based on various risk factors:
*   **Liquidity Risk:** Ease of converting the asset to cash without price discount.
*   **Business Risk:** Uncertainty regarding economic conditions and demand for space.
*   **Leverage Risk:** Impact of debt; small changes in NOI causing large changes in equity cash flow.
*   **Environmental/Political Risk:** Contaminants or lack of transparency/data.

**Analogy:**
Choosing between IRR and Capital Accumulation is like **choosing between a car's top speed and the total distance it can travel.** The **IRR** is the top speed—it tells you how fast your money is growing. **Capital Accumulation** is the total distance—it factors in where you stop to refuel (reinvestment) and how much fuel you started with (initial investment) to tell you exactly where you end up at the end of the trip.

--- FILE END ---


--- FILE START: Module_09.md ---

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

--- FILE END ---
