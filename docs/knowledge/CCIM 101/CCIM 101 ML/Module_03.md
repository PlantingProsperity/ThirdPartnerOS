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