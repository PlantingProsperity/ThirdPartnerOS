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