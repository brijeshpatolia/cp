# BFRE Whitepaper — Transcription of PDF pages 37–45

Source images: `/tmp/claude-0/-home-user-cp/79206b60-659d-5f16-a034-7d8ab14cc34a/scratchpad/img/p037.jpg` … `p045.jpg`
Every page carries the running head banner **"BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)"** and the **aladdin by BlackRock** logo in the footer.
PDF page index = printed page number throughout this chunk (p037 → "Page 37", p038 → "Page 38", …, p045 → "Page 45"). On p040 and p041 the printed footer is cropped out of the photograph, but the sequence is unbroken.

---

## PDF page 37 (printed p. 37)

### Headings
- Running head: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- (Ghost/bleed-through from the reverse side of the sheet shows the words "Model Surveillance" faintly at the top — that heading actually belongs to p. 38.)
- Figure caption: **Figure 1.19. BFRE Model Production Process**
- Figure caption: **Figure 1.20. BFRE Coverage Criteria and Proxy**

### Equations
None on this page.

### Tables
None (two figures only).

### Figures

**Figure 1.19. BFRE Model Production Process** — a left-to-right chevron/arrow process banner with seven stages, each stage heading a column of boxes below it.

Stage banner (in order):
1. `Derived Data and Universe Construction`
2. `Data QC`
3. `Substyles Standardization`
4. `Styles Aggregation`
5. `Risk Estimation and Output`
6. `Model QC`
7. `Summary Report and Model Release`

Column contents:

| Stage | Boxes listed underneath (top → bottom) |
|---|---|
| Derived Data and Universe Construction | "Industry enrichment"; "Universe Construction"; "Returns (weekly/ monthly aggregated, excess returns, cleaning process)"; "Weekly/ monthly risk free rate aggregation"; "Index returns"; "Monthly volumes"; "Number of observations and frequency of trade"; "Region Model Country" |
| Data QC | one tall box: "QC process on the data" |
| Substyles Standardization | one tall box: "To construct substyles" |
| Styles Aggregation | one tall box: "To aggregate the substyles into final style exposures" |
| Risk Estimation and Output | "Factor Return Estimation"; "Factor Covariance"; "Specific Return and Specific Risk"; "Specific Return Correlation" |
| Model QC | "Asset risk changes"; "Styles/ Substyles day on day correlation"; "Coverage changes"; "Country and industry Changes"; "Standardised factor returns"; "Asset returns cleaning" |
| Summary Report and Model Release | "Summary Report job analyses the QC reports and produces a summary, highlighting the exceptions"; "If no exception, model is signed off. Touch files are created to indicate models available"; "If there are exceptions, model is manually signed off using GP Workflow monitor" |

**Figure 1.20. BFRE Coverage Criteria and Proxy** — a top-to-bottom decision flowchart of five diamond decision nodes, with three terminal grey boxes at the bottom.

Decision nodes (top → bottom), each with a "NO" branch drawn to the right/left:
1. `Data exists?` — NO branch runs left and down to the terminal box **Sedol Proxy**; YES continues down.
2. `Eligible exchange?` — NO branch runs right, joining a common line that drops to the terminal box **Unit Proxy**. Annotation to the right: *"Eligible exchanges in BFRE coverage were defined by BFRE research"*.
3. `Eligible status?` — NO branch to the same Unit-Proxy line. Annotation: *"Bloomberg: Active, halted, Suspended, Order Imbalance. Data Stream: Active, Suspended"*.
4. `Eligible security type?` — NO branch to the Unit-Proxy line. Annotation: *"Eligible security types: ADR, DF, EQ, GDR, INVT, NVDR, PREF and GNSH"*.
5. `Market & Industry data?` — NO branch to the Unit-Proxy line. Annotation: *"Minimum requirements: price, shares outstanding, total returns and industry classification"*.

Terminal boxes: **Sedol Proxy** (left), **BFRE Coverage** (centre, reached by passing all five tests), **Unit Proxy** (right).

### Numbers
- "Figure 1.19", "Figure 1.20" (figure numbers). Seven production-process stages; five coverage decision nodes; three terminal outcomes. No other numeric values on the page.

### Terms / named entities
- Production stages: Derived Data and Universe Construction; Data QC; Substyles Standardization; Styles Aggregation; Risk Estimation and Output; Model QC; Summary Report and Model Release.
- Risk-estimation outputs named: Factor Return Estimation; Factor Covariance; Specific Return and Specific Risk; Specific Return Correlation.
- QC checks named: Asset risk changes; Styles/Substyles day-on-day correlation; Coverage changes; Country and industry Changes; Standardised factor returns; Asset returns cleaning.
- Coverage: Sedol Proxy; BFRE Coverage; Unit Proxy.
- Eligible security types: **ADR, DF, EQ, GDR, INVT, NVDR, PREF, GNSH**.
- Eligible status values: Bloomberg — Active, halted, Suspended, Order Imbalance; Data Stream — Active, Suspended.
- Data vendors named: Bloomberg, Data Stream (Datastream).
- "GP Workflow monitor" (sign-off tool); "Touch files" (release artefacts).

### Claims / methodological choices
- Model release is automated conditional on QC: if the Summary Report job finds no exception the model is auto-signed-off and touch files are created to indicate models are available; if there are exceptions the model is manually signed off using the GP Workflow monitor.
- Coverage is hierarchical: an asset failing the *data exists* test gets a **Sedol Proxy**; an asset with data but failing exchange / status / security-type / market-and-industry-data eligibility gets a **Unit Proxy**; only assets passing all five tests enter BFRE Coverage.
- Justification for the eligible-exchange list is given only as "defined by BFRE research" — no criteria are stated.

### Unreadable
- Faint bleed-through text from the reverse of the page overlays the middle of Figure 1.19; it does not belong to this page and was not transcribed.

---

## PDF page 38 (printed p. 38)

### Headings
- **Model Surveillance** (section heading)

### Equations
None.

### Tables
None.

### Body text (verbatim)
"The BFRE risk models are reviewed on an on-going basis as follows:"

- "**Accuracy of volatility forecasts**: this is assessed through the use of bias statistics which compare the level of forecast volatility against realised volatility for different portfolios. Bias statistics are based on a rolling window standard deviation of 12 monthly standardised returns, and exceptions are flagged using a 95% confidence interval"
- "**Accuracy of tail risk forecasts**: this is assessed based on the proportion of violations of 99% 1-day VaR over the previous 252 days¹⁸. VaR is calculated using BRS' various VaR methodologies: Analytical, Historical and Monte Carlo VaR"
- "**Benchmarking**: BFRE risk forecasts for the metrics above are assessed against Aladdin's other equity risk models, namely STORM."

"Exceptions are reviewed and logged on a monthly basis in line with current BRS model risk surveillance practices. Signs of persistently poor model performance over many periods would lead to further investigation by the model research team, and may lead to future model development."

"The results of the model back-testing reviews are also presented to Aladdin clients in the Quarterly Aladdin Risk Model back-testing calls."

Footnote 18: "This test is consistent with current UCITS guidelines for model evaluation, and follows the approach in Kupiec (1995)"

### Numbers
- **12** monthly standardised returns — length of the rolling window used for bias statistics.
- **95%** confidence interval — threshold for flagging bias-statistic exceptions.
- **99%** 1-day VaR — confidence level of the tail-risk test.
- **252 days** — look-back window over which VaR violations are counted.
- **1995** — Kupiec (1995), the reference for the VaR back-test.
- Monthly — frequency of exception review/logging; Quarterly — frequency of the client back-testing calls.

### Terms
- Bias statistics; realised vs forecast volatility; VaR violations.
- VaR methodologies: **Analytical, Historical, Monte Carlo**.
- **STORM** — Aladdin's other equity risk model, used as the benchmark.
- **BRS** (BlackRock Solutions); **Aladdin**; **UCITS** guidelines; **Kupiec (1995)**.

### Claims / methodological choices
- Three surveillance dimensions only: volatility-forecast accuracy (bias stats), tail-risk accuracy (VaR violations), and benchmarking against STORM.
- The bias statistic uses a rolling 12-month window of standardised returns; the choice of 12 months and of the 95% interval is asserted, not justified.
- The 99%/252-day VaR test is justified by consistency with UCITS guidelines and Kupiec (1995).
- Escalation path: persistently poor performance over many periods → investigation by the model research team → possibly future model development. "Persistently" and "many periods" are not quantified.

### Figures
None.

### Unreadable
- Nothing material; the lower half of the page is blank apart from bleed-through text from the reverse side.

---

## PDF page 39 (printed p. 39)

### Headings
- **Appendices** (part heading)
- **STYLE FACTOR EXPOSURE CONSTRUCTION** (section heading)
- Numbered sub-headings: **1. Cloning**, **2. Fill-Miss**, **3. Huberisation**, **4. Substyle Aggregation**, **5. Style Factor Exposure Cloning**

### Equations
None (the page refers out to Appendix C for the substyle equations and Appendix B for the aggregation definitions).

### Tables
None.

### Body text (verbatim / near-verbatim)
"Raw substyle values are built from input data according to a set of pre-specified equations set out in Appendix C. As part of this process, theoretical bounds may be placed on intermediate forms or set to missing (where a data error is suspected). Up to five transformations are applied to the raw substyles. Some of these consume model universe information, and hence these transformed substyles are model-specific. The transformations (in order of application) are:"

1. **Cloning** — "Cloning seeks to fill missing values by harvesting the value from a cross-listing, or from a root asset to a depositary receipt (and vice versa). This procedure is typically used to handle new listings or securities of existing companies."
2. **Fill-Miss** — "This procedure seeks to cross-sectionally interpolate the substyle value by regressing it on a size factor (log market capitalisation), the market, country and industry factors. For any asset that is missing a substyle value, its value is inferred using similar-sized assets in the same industry and the same country. This procedure is typically employed to handle listings of new companies."
3. **Huberisation** — "Huberisation is a refined version of the standard Winsorisation procedure for transforming substyle values to a common standardised scale, i.e. z-scores. The standardised values are referred to as exposures and take values between +/- 3 and are standardised to a square-root capitalisation mean of zero, with an equal-weighted standard deviation of one¹⁹. This procedure mitigates issues of clustering and destroyed rank information in the tails of the substyle (distribution) as compared to the standard Winsorisation procedure."
4. **Substyle Aggregation** — "Following the above transformations, substyles are aggregated to form style factors according to the definitions set out in Appendix B. These values are then passed through the Huberisation procedure once more to ensure that style factor exposures are standardised to a common scale."
5. **Style Factor Exposure Cloning** — "Finally a cloning procedure is applied to ensure that fungible assets receive same style factor exposures. Assuming that no barriers exist, these assets should converge in traded price to eradicate any arbitrage opportunities. Thus, over longer horizons their returns are expected to converge, even if their shorter-term (observed) price journeys do not exactly match." / "This approach is applied to related listings such as Depositary Receipts (and their root assets) and cross-listed assets. In general style factor exposures are cloned from the more liquid (or primary) listing to the less liquid listing."

Footnote 19: "The universe used for standardisation is similar to one used in the core model estimation"

### Numbers
- **five** — number of transformations applied to raw substyles ("Up to five").
- **+/- 3** — the bounds within which Huberised exposures lie.
- **zero** — the (square-root-capitalisation-weighted) mean of standardised exposures.
- **one** — the equal-weighted standard deviation of standardised exposures.
- Numbered list 1–5.

### Terms
- Raw substyle; substyle; style factor; exposure (= z-score).
- **Cloning**, **Fill-Miss**, **Huberisation**, **Substyle Aggregation**, **Style Factor Exposure Cloning**.
- Winsorisation (contrast procedure); depositary receipt; root asset; cross-listing; fungible assets; primary listing.
- Appendix B (substyle → style aggregation definitions), Appendix C (raw substyle equations).

### Claims / methodological choices
- Transformations are applied in a stated order; some consume model-universe information, making transformed substyles **model-specific**.
- Fill-Miss regresses the substyle on log market cap plus market, country and industry factors — i.e. missing values are imputed from similar-sized, same-industry, same-country assets. Chosen "typically … to handle listings of new companies".
- Huberisation is asserted to beat Winsorisation on two grounds: less clustering at the caps and preservation of rank information in the tails. No empirical evidence is offered on the page.
- Note the asymmetry of the standardisation: mean taken **square-root-capitalisation-weighted**, standard deviation taken **equal-weighted**. No justification given for the mismatch.
- Style exposures are Huberised a second time after aggregation.
- Exposure cloning is justified by an arbitrage/convergence argument for fungible listings; direction of cloning is from the more liquid (primary) listing to the less liquid one.

### Figures
None.

### Unreadable
- None; page is clean.

---

## PDF page 40 (printed p. 40 — footer cropped from photo)

### Headings
- **STYLE DEFINITIONS** (section heading)
- Two stacked tables, no numbered captions. Both have the column headers `Style | Substyle Description | AUST | EMEA | UKIN | NAMR | CAND | LATC`.
- Bottom note: **"Note that the substyles with [*] are negated."**

### Equations
None.

### Tables

The cell values are the **weights of each substyle within its style factor, per regional model**. Blank = substyle not used in that model. Weights within a style sum to 1.00 within each region column (verified below).

**Table A (p.40, upper) — Style/substyle weights: AUST, EMEA, UKIN, NAMR, CAND, LATC**

| Style | Substyle Description | AUST | EMEA | UKIN | NAMR | CAND | LATC |
|---|---|---|---|---|---|---|---|
| Volatility | Historical Beta (to Reginal Market Index) [sic — "Reginal"] | 0.34 | 0.2 | 0.25 | 0.34 | 0.34 | 0.1 |
| Volatility | Hist. Beta x Hist. Sigma | | 0.2 | 0.25 | | | |
| Volatility | Cumulative Range – 12M | 0.33 | 0.2 | 0.25 | 0.33 | 0.33 | 0.1 |
| Volatility | Historical Sigma | | 0.2 | | 0.33 | 0.33 | 0.4 |
| Volatility | Standard Deviation – 1Y | 0.33 | 0.2 | 0.25 | | | 0.4 |
| Momentum | Relative Strength – 11M | 0.5 | 1.00 | 0.5 | 0.5 | 0.5 | 0.5 |
| Momentum | Historical Alpha | 0.5 | | 0.5 | 0.5 | 0.5 | 0.5 |
| Size | Log Company Market Cap | 0.34 | 0.25 | 0.25 | 0.75 | 0.34 | 1.00 |
| Size | Log of Total Assets | | 0.25 | 0.25 | | | |
| Size | Broker Coverage* | 0.33 | 0.25 | 0.25 | | 0.33 | |
| Size | Log of Sales | 0.33 | 0.25 | 0.25 | 0.25 | 0.33 | |
| Reversal | Relative Strength – 1M | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Liquidity | Prop. of Active Trade days – 3M | | 0.2 | | 0.1 | | |
| Liquidity | Prop. of Active Trade days – 6M | | 0.2 | | 0.1 | | |
| Liquidity | Prop. of Active Trade days –12M | | 0.2 | | 0.1 | | |
| Liquidity | Price Pressure 1M* | | | | | | |
| Liquidity | Price Pressure 3M* | | | | | | |
| Liquidity | Return to Turnover* | | 0.2 | | 0.1 | | |
| Liquidity | Amihud Ratio – 1Y* | | 0.2 | | 0.6 | 0.34 | |
| Liquidity | Growth of Trading Volume 12M | | | | | | |
| Liquidity | Growth of Trading Volume 36M | | | | | | |
| Liquidity | Stock Turnover – 3M | | | 0.34 | | 0.33 | 0.34 |
| Liquidity | Stock Turnover – 6M | | | 0.33 | | 0.33 | 0.33 |
| Liquidity | Stock Turnover – 12M | | | 0.33 | | | 0.33 |
| SmallCap/ MidCap | SmallCap Factor | 1.00 | 1.00 | 1.00 | | | |
| SmallCap/ MidCap | MidCap Factor | | | | 1.00 | | |
| Emerging/ Developed | Decoupling: Beta to (iShares MSCI EM – SP500) | | 1.00 | | | | |

Column sum checks (all = 1.00): Volatility AUST 0.34+0.33+0.33; EMEA 5×0.2; UKIN 4×0.25; NAMR 0.34+0.33+0.33; CAND 0.34+0.33+0.33; LATC 0.1+0.1+0.4+0.4. Size NAMR 0.75+0.25. Liquidity EMEA 5×0.2; NAMR 0.1+0.1+0.1+0.1+0.6; CAND 0.34+0.33+0.33; UKIN and LATC 0.34+0.33+0.33.

**Table B (p.40, lower) — Style/substyle weights: AUST, EMEA, UKIN, NAMR, CAND, LATC**

| Style | Substyle Description | AUST | EMEA | UKIN | NAMR | CAND | LATC |
|---|---|---|---|---|---|---|---|
| Value | Book Value to Price | 0.34 | 0.34 | | 0.34 | | |
| Value | Sales to Price | 0.33 | 0.33 | 0.5 | 0.33 | | |
| Value | Cash Flow to Price | 0.33 | 0.33 | 0.5 | 0.33 | | |
| Profit | Return on Capital Employed | | 0.25 | | | | |
| Profit | Return on Equity | | 0.25 | | 0.33 | | |
| Profit | Return on Assets | 0.33 | 0.25 | | 0.33 | | |
| Profit | Interest Coverage | 0.34 | 0.25 | 0.5 | 0.34 | | |
| Profit | Cash Flow to Liabilities | | | | | | |
| Profit | Operating Profit Margin | 0.33 | | 0.5 | | | |
| EarnYield | Earnings to Price | | 0.25 | | 0.34 | 0.34 | 0.5 |
| EarnYield | EBITDA to Enterprise Value | | 0.25 | | 0.33 | 0.33 | |
| EarnYield | Normalised Earnings to Price | | 0.25 | | 0.33 | 0.33 | 0.5 |
| DivYield | Dividend Yield | | 0.25 | | 1.00 | | |
| Growth | Asset Growth Rate | | 0.25 | | 0.34 | 0.5 | |
| Growth | Change in Assets | | 0.25 | | 0.33 | 0.5 | |
| Growth | Predicted Sales Growth | | 0.25 | | 0.33 | | |
| Growth | Growth of Total Sales | | 0.25 | | | | |
| Growth | Variation in Capital Structure | | | | | | |
| Sentiment | Beta on VIX (Regional) | | 1.00 | | 1.00 | | |
| Leverage | Debt to Assets | | | 0.34 | | | 1.00 |
| Leverage | Market Leverage | | | 0.33 | | | |
| Leverage | Balance Sheet Cash | | | | | | |
| Leverage | Book Leverage | | | 0.33 | | | |
| Oil | Crude Oil-Brent M+3 | | | | | | |
| Oil | UK Close US$/BBL (Regional) | | | | | | |
| Quality | Equity Dilution | | | | | | |
| Foreign Sensitivity | Foreign Sales | | | | | 0.5 (see note) | |
| Foreign Sensitivity | Foreign Assets | | | | | 0.5 (see note) | |

Note on the last block: a single value **0.5** is printed in the CAND column vertically centred across the two Foreign Sensitivity rows. It is most consistent with 0.5 on Foreign Sales and 0.5 on Foreign Assets (summing to 1.00), but only one glyph is printed, so the row attribution is not certain — flagged below.

Column sum checks: Value AUST/EMEA/NAMR 0.34+0.33+0.33, UKIN 0.5+0.5. Profit AUST 0.33+0.34+0.33; EMEA 4×0.25; UKIN 0.5+0.5; NAMR 0.33+0.33+0.34. EarnYield NAMR/CAND 0.34+0.33+0.33; LATC 0.5+0.5; **EMEA EarnYield 0.25+0.25+0.25 = 0.75** unless the EMEA Dividend Yield 0.25 is counted inside EarnYield (see Claims). Growth EMEA 4×0.25; NAMR 0.34+0.33+0.33; CAND 0.5+0.5. Leverage UKIN 0.34+0.33+0.33.

### Numbers
Every weight is listed in the tables above. Distinct weight values used: 1.00, 0.75, 0.6, 0.5, 0.34, 0.33, 0.25, 0.2, 0.4, 0.1.

### Terms — named styles and substyles introduced on this page
- **Styles**: Volatility, Momentum, Size, Reversal, Liquidity, SmallCap/MidCap, Emerging/Developed, Value, Profit, EarnYield, DivYield, Growth, Sentiment, Leverage, Oil, Quality, Foreign Sensitivity.
- **Substyles**: Historical Beta (to Regional Market Index); Hist. Beta × Hist. Sigma; Cumulative Range – 12M; Historical Sigma; Standard Deviation – 1Y; Relative Strength – 11M; Historical Alpha; Log Company Market Cap; Log of Total Assets; Broker Coverage*; Log of Sales; Relative Strength – 1M; Prop. of Active Trade days – 3M/6M/12M; Price Pressure 1M*; Price Pressure 3M*; Return to Turnover*; Amihud Ratio – 1Y*; Growth of Trading Volume 12M; Growth of Trading Volume 36M; Stock Turnover – 3M/6M/12M; SmallCap Factor; MidCap Factor; Decoupling: Beta to (iShares MSCI EM – SP500); Book Value to Price; Sales to Price; Cash Flow to Price; Return on Capital Employed; Return on Equity; Return on Assets; Interest Coverage; Cash Flow to Liabilities; Operating Profit Margin; Earnings to Price; EBITDA to Enterprise Value; Normalised Earnings to Price; Dividend Yield; Asset Growth Rate; Change in Assets; Predicted Sales Growth; Growth of Total Sales; Variation in Capital Structure; Beta on VIX (Regional); Debt to Assets; Market Leverage; Balance Sheet Cash; Book Leverage; Crude Oil-Brent M+3; UK Close US$/BBL (Regional); Equity Dilution; Foreign Sales; Foreign Assets.
- **Regional model codes on this page**: AUST, EMEA, UKIN, NAMR, CAND, LATC.

### Claims / methodological choices
- Style composition is region-specific: the same style name is built from different substyles with different weights in each regional model. No justification for the regional differences is given on this page.
- Weights are essentially equal-weighting within each style (0.5/0.5, 0.34/0.33/0.33, 4×0.25, 5×0.2), with a handful of deliberate exceptions: NAMR Size = 0.75 Log Company Market Cap + 0.25 Log of Sales; NAMR Liquidity = 0.6 Amihud + 4×0.1; LATC Volatility = 0.1/0.1/0.4/0.4.
- Substyles marked `*` (Broker Coverage*, Price Pressure 1M*, Price Pressure 3M*, Return to Turnover*, Amihud Ratio – 1Y*) are **negated** before aggregation, i.e. these are illiquidity/coverage measures whose sign is flipped so that higher = more liquid / larger.
- The EMEA column shows Dividend Yield 0.25 alongside three 0.25 EarnYield substyles; taken literally EMEA's EarnYield weights sum to only 0.75 and its DivYield style has weight 0.25 rather than 1.00. The consistent reading is that in EMEA Dividend Yield is a fourth substyle *inside* EarnYield, but the table does not say so.
- Emerging/Developed is defined by a "Decoupling" beta to the return spread iShares MSCI EM minus S&P 500 (EMEA = 1.00 here).

### Figures
None.

### Unreadable
- p.40: the CAND value **0.5** in the Foreign Sensitivity block is printed once, centred between the "Foreign Sales" and "Foreign Assets" rows; which row (or both) it belongs to cannot be determined from the scan.
- p.40: the printed page-number footer is cut off by the photograph's lower edge.

---

## PDF page 41 (printed p. 41 — footer cropped from photo)

Continuation of **STYLE DEFINITIONS** (no new heading; same two-table layout, different region columns).

### Headings
- Running head only. Column headers: `Style | Substyle Description | JAPN | APXJ | WRLD | USAM | EMKT`.

### Equations
None.

### Tables

**Table C (p.41, upper) — Style/substyle weights: JAPN, APXJ, WRLD, USAM, EMKT**

| Style | Substyle Description | JAPN | APXJ | WRLD | USAM | EMKT |
|---|---|---|---|---|---|---|
| Volatility | Historical Beta (to Reginal Market Index) | 0.2 | 0.34 | 0.25 | 0.34 | 0.34 |
| Volatility | Hist. Beta x Hist. Sigma | 0.2 | | | | 0.33 |
| Volatility | Cumulative Range – 12M | 0.2 | 0.33 | 0.25 | 0.33 | 0.33 |
| Volatility | Historical Sigma | 0.2 | | 0.25 | 0.33 | |
| Volatility | Standard Deviation – 1Y | 0.2 | 0.33 | 0.25 | | |
| Momentum | Relative Strength – 11M | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Momentum | Historical Alpha | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
| Size | Log Company Market Cap | 0.34 | 0.34 | 0.34 | 0.5 | 0.25 |
| Size | Log of Total Assets | | | | | 0.25 |
| Size | Broker Coverage* | 0.33 | 0.33 | 0.33 | | 0.25 |
| Size | Log of Sales | 0.33 | 0.33 | 0.33 | 0.5 | 0.25 |
| Reversal | Relative Strength – 1M | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Liquidity | Prop. of Active Trade days – 3M | | | 0.17 | 0.2 | |
| Liquidity | Prop. of Active Trade days – 6M | | | 0.17 | 0.2 | |
| Liquidity | Prop. of Active Trade days –12M | | | 0.17 | 0.2 | |
| Liquidity | Price Pressure 1M* | | | | | 0.34 |
| Liquidity | Price Pressure 3M* | | | | | 0.33 |
| Liquidity | Return to Turnover* | 1.00 | | 0.16 | 0.2 | |
| Liquidity | Amihud Ratio – 1Y* | | 0.34 | 0.16 | | |
| Liquidity | Growth of Trading Volume 12M | | | | | 0.33 |
| Liquidity | Growth of Trading Volume 36M | | | 0.17 | 0.2 | |
| Liquidity | Stock Turnover – 3M | | 0.33 | | | |
| Liquidity | Stock Turnover – 6M | | 0.33 | | | |
| Liquidity | Stock Turnover – 12M | | | | | |
| SmallCap/ MidCap | SmallCap Factor | | 1.00 | 1.00 | 1.00 | 1.00 |
| SmallCap/ MidCap | MidCap Factor | | | | | |
| Emerging/ Developed | Decoupling: Beta to (iShares MSCI EM – SP500) | 1.00 | | 1.00 | | **-1.00** |

Column sum checks: Volatility JAPN 5×0.2; APXJ 0.34+0.33+0.33; WRLD 4×0.25; USAM 0.34+0.33+0.33; EMKT 0.34+0.33+0.33. Size EMKT 4×0.25; USAM 0.5+0.5. Liquidity WRLD 0.17+0.17+0.17+0.16+0.16+0.17 = 1.00; USAM 5×0.2; APXJ 0.34+0.33+0.33; EMKT 0.34+0.33+0.33; JAPN 1.00.

**Table D (p.41, lower) — Style/substyle weights: JAPN, APXJ, WRLD, USAM, EMKT**

| Style | Substyle Description | JAPN | APXJ | WRLD | USAM | EMKT |
|---|---|---|---|---|---|---|
| Value | Book Value to Price | 0.67 | 0.34 | 0.34 | 0.34 | 0.34 |
| Value | Sales to Price | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| Value | Cash Flow to Price | | 0.33 | 0.33 | 0.33 | 0.33 |
| Profit | Return on Capital Employed | | | | 0.33 | |
| Profit | Return on Equity | | | | | |
| Profit | Return on Assets | | | 0.25 | 0.33 | |
| Profit | Interest Coverage | | | 0.25 | 0.34 | |
| Profit | Cash Flow to Liabilities | | | 0.25 | | |
| Profit | Operating Profit Margin | | | 0.25 | | |
| EarnYield | Earnings to Price | 0.34 | 0.34 | 0.34 | 0.34 | 0.34 |
| EarnYield | EBITDA to Enterprise Value | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| EarnYield | Normalised Earnings to Price | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| DivYield | Dividend Yield | | | 1.00 | 1.00 | |
| Growth | Asset Growth Rate | 0.34 | | 0.25 | 0.34 | |
| Growth | Change in Assets | 0.33 | | 0.25 | 0.33 | |
| Growth | Predicted Sales Growth | | | | | |
| Growth | Growth of Total Sales | 0.33 | | 0.25 | 0.33 | |
| Growth | Variation in Capital Structure | | | 0.25 | | |
| Sentiment | Beta on VIX (Regional) | 1.00 | 1.00 | 1.00 | | |
| Leverage | Debt to Assets | 0.34 | | 0.5 | 0.5 | |
| Leverage | Market Leverage | 0.33 | | | | |
| Leverage | Balance Sheet Cash | | | **-0.5** | | |
| Leverage | Book Leverage | 0.33 | | | 0.5 | |
| Oil | Crude Oil-Brent M+3 | 1.00 | | | | 1.00 |
| Oil | UK Close US$/BBL (Regional) | | | 1.00 | | |
| Quality | Equity Dilution | | 1.00 | | | 1.00 |
| Foreign Sensitivity | Foreign Sales | (blank) | (blank) | (blank) | [cut off] | [cut off] |
| Foreign Sensitivity | Foreign Assets | (blank) | (blank) | (blank) | [cut off] | [cut off] |

Column sum checks: Value JAPN 0.67+0.33; others 0.34+0.33+0.33. Profit USAM 0.33+0.33+0.34; WRLD 4×0.25. EarnYield all five 0.34+0.33+0.33. Growth JAPN/USAM 0.34+0.33+0.33; WRLD 4×0.25. Leverage JAPN 0.34+0.33+0.33; USAM 0.5+0.5; WRLD 0.5 + (-0.5).

### Numbers
All weights listed above. Notable non-standard values on this page: **0.67** (JAPN Book Value to Price), **0.17 / 0.16** (WRLD liquidity six-way split), **-0.5** (WRLD Balance Sheet Cash inside Leverage), **-1.00** (EMKT Emerging/Developed decoupling beta), **0.75** does not appear here.

### Terms
- Regional model codes on this page: **JAPN, APXJ, WRLD, USAM, EMKT** (Japan, Asia-Pacific ex-Japan, World, US America, Emerging Markets — expansions inferred, not printed here).
- Same substyle vocabulary as p.40.

### Claims / methodological choices
- **EMKT's Emerging/Developed exposure is -1.00** — the emerging-markets model takes the opposite sign of the same decoupling beta used with +1.00 in JAPN and WRLD.
- **WRLD Leverage nets Balance Sheet Cash at -0.5 against Debt to Assets at +0.5** — i.e. leverage is built as debt minus cash; the absolute weights still sum to 1 but the signed sum is 0.
- JAPN Value is deliberately unequal (0.67 Book/Price, 0.33 Sales/Price) and omits Cash Flow to Price; JAPN Liquidity is a single substyle (Return to Turnover*, 1.00).
- WRLD Liquidity spreads over six substyles at 0.17/0.17/0.17/0.16/0.16/0.17.
- EMKT Liquidity uses Price Pressure 1M*/3M* plus Growth of Trading Volume 12M — the only model using the Price Pressure substyles.
- Oil is modelled with Crude Oil-Brent M+3 (JAPN, EMKT) or UK Close US$/BBL (Regional) (WRLD); Quality = Equity Dilution alone (APXJ, EMKT).
- No JAPN SmallCap/MidCap factor; the other four models here use SmallCap Factor at 1.00.
- No justification is offered anywhere on pp. 40–41 for why particular substyles enter particular regional models.

### Figures
None.

### Unreadable
- p.41: the last two table rows (Foreign Sensitivity — Foreign Sales, Foreign Assets) run off the bottom edge of the photograph; the USAM and EMKT cells for those rows are not visible at all, and the JAPN/APXJ/WRLD cells appear empty but the row bottoms are clipped.
- p.41: the printed page-number footer is cut off by the photograph's lower edge.

---

## PDF page 42 (printed p. 42)

### Headings
- **SUBSTYLE DEFINITIONS** (section heading)
- **Volatility** (style heading)
- Sub-headings (underlined): **Historical Beta**, **Historical Sigma**, **Beta × Sigma**, **Cumulative Range – 12 months**, **Standard Deviation – 1 year**

### Equations

**(1.12)** Historical Beta — "The estimated slope coefficient β̂_i from an exponentially weighted univariate regression of asset returns r on a market index r^M:"

```
r_{i,s} = alpha_i + beta_i * r^M_{i,s} + epsilon_{i,s}
```

Symbols: `r_{i,s}` = weekly excess return of asset i at time s; `alpha_i` = intercept (this intercept is the "Historical Alpha" substyle, see p.44); `beta_i` = slope (the Historical Beta substyle); `r^M_{i,s}` = return on the market index applicable to asset i at time s; `epsilon_{i,s}` = regression residual.

**(1.13)** Cumulative Range – 12 months — "The difference between the maximum and minimum cumulative log returns over the last 12 months:"

```
max_{s=0,...,11} { sum_{u=t-s}^{t} ln(1 + r_{i,u}) }  -  min_{s=0,...,11} { sum_{u=t-s}^{t} ln(1 + r_{i,u}) }
```

Symbols: `r_{i,u}` = total return of asset i in month u; s indexes the look-back length 0…11 months; t = current month.

Non-displayed definitions on the page:
- **Historical Sigma** = "An equally-weighted standard deviation of the residuals in regression (1.12)", i.e. sd(epsilon_{i,s}) computed with equal weights.
- **Beta × Sigma** = "The product of Historical Beta and Historical Sigma" = betâ_i × sigmâ_i.
- **Standard Deviation – 1 year** = "An exponentially-weighted estimate of the standard deviation of daily total returns."

### Tables
None.

### Numbers
- **(1.12)**: returns are **weekly** and in excess of the **local risk-free rate**; exponential weighting **half-life = 52 weeks**; estimation sample = **5 years of weekly observations**.
- **(1.13)**: window = **12 months**; s runs 0…**11**.
- Standard Deviation – 1 year: **daily** total returns; exponential weighting **half-life = 180 days**; sample = **360 observations**.
- Equation numbers 1.12, 1.13.

### Terms
- Historical Beta; Historical Sigma; Beta × Sigma; Cumulative Range – 12 months; Standard Deviation – 1 year.
- "Estimation Universe" — the market index is defined as the **market-capitalisation-weighted Estimation Universe**.

### Claims / methodological choices
- Betas are estimated on **weekly excess returns** with a **52-week half-life** over a **5-year** window; the market proxy is the cap-weighted Estimation Universe rather than a commercial index. No justification given for 52 weeks / 5 years.
- Historical Sigma deliberately uses **equal weighting** for the residual standard deviation even though the regression that produced the residuals is **exponentially weighted** — an explicit inconsistency, unjustified.
- Standard Deviation – 1Y uses **daily total** returns (not excess) with a 180-day half-life over 360 observations — a different frequency, weighting and return definition from the beta regression, again with no stated rationale.
- Cumulative Range uses **log total returns** ("All returns are total returns").

### Figures
None.

### Unreadable
- In (1.12) the market-return term is printed as r with superscript M and subscript "i,s"; the subscript characters are small but legible as `i,s`. Recorded as `r^M_{i,s}`.

---

## PDF page 43 (printed p. 43)

### Headings
- **Size** (style heading)
- Sub-headings (underlined): **Log of Company Market Capitalisation**, **Log of Total Assets**, **Broker Coverage**, **Log of Sales**

### Equations

**Log of Company Market Capitalisation** (no numbered equation) — "The natural logarithm of company market capitalisation in USD." i.e. `ln(MarketCap_i)` in USD.

**(1.14)** Log of Total Assets — "The natural logarithm of the average Total Assets A over the last 5 years:"

```
ln( (1/5) * sum_{s=t-4}^{t} A_{i,s} )
```
Symbols: `A_{i,s}` = Total Assets of company i in (annual) period s; t = current period.

**(1.15)** Broker Coverage — "Broker Coverage is based on the number B of EPS FY1 estimates in the IBES database:"

```
- ln(1 + B_{i,t})
```
Symbols: `B_{i,t}` = number of EPS FY1 estimates for asset i at time t. The leading minus sign is the negation flagged by the `*` in the style tables.

**(1.16)** Log of Sales — "The natural logarithm of the average Total Sales S over the last 5 years:"

```
ln( (1/5) * sum_{s=t-4}^{t} S_{i,s} )
```
Symbols: `S_{i,s}` = Total Sales of company i in period s.

### Tables
None.

### Numbers
- **5 years** averaging window for Total Assets (1.14) and Total Sales (1.16); the sums run `s = t-4 … t` (5 terms) with the `1/5` prefactor.
- **FY1** — the forecast year of the EPS estimates counted.
- Equation numbers 1.14, 1.15, 1.16.

### Terms
- Log of Company Market Capitalisation; Log of Total Assets; Broker Coverage; Log of Sales.
- **IBES** database (source of EPS FY1 estimate counts); **USD** (currency of market cap).

### Claims / methodological choices
- Market cap is converted to **USD** before taking logs — cross-market comparability.
- Assets and Sales are **5-year averages** before the log, smoothing single-year distortions; the choice of 5 years is asserted without justification.
- Broker Coverage enters **negated** (`-ln(1+B)`) so that a *smaller* analyst following loads positively — consistent with its `*` marking as a size/liquidity proxy in the style tables.
- `ln(1+B)` handles zero-coverage assets without a log of zero.

### Figures
None.

### Unreadable
- Bleed-through from the reverse page is visible in the lower half but no page 43 content is obscured. The `aladdin` logo is partially overwritten by the phone-camera watermark "Galaxy Z Flip7"; the footer "Page 43" is legible.

---

## PDF page 44 (printed p. 44)

### Headings
- **Momentum** (style heading); sub-headings **Relative Strength – 11 Months**, **Historical Alpha**
- **Reversal** (style heading; the definition follows immediately, no separate sub-heading)
- **Liquidity** (style heading); sub-headings **Proportion of Active Trade Days – 3 months, 6 months & 12 months**, **Return-to-Turnover**

### Equations

**(1.17)** Relative Strength – 11 Months — "The cumulative log excess return over the last 11 months²⁰ with a one month lag:"

```
ln( 1 + prod_{s=t-11}^{t-1} (1 + r_{i,s}) - prod_{s=t-11}^{t-1} (1 + r^f_s) )
```
Symbols: `r_{i,s}` = total return of asset i in month s; `r^f_s` = risk-free rate in month s; the product runs from t-11 to **t-1** (the one-month lag).

**Historical Alpha** (no numbered equation) — "The Historical alpha from the exponentially weighted univariate regression (1.12)", i.e. `alphâ_i` from (1.12).

**(1.18)** Reversal — "The log excess return over the previous month²¹:"

```
ln(1 + r_{i,t} - r^f_t)
```

**(1.19)** Proportion of Active Trade Days — "The proportion of active trade days over some specified window T. Active trade days are defined as those where the close price is not equal to the close price of the previous day, or where the traded volume is non-zero:"

```
[ sum_{s=t-T+1}^{t} 1_{(P_{i,s} != P_{i,s-1}) OR (V_{i,s} > 0)} ]  /  [ sum_{s=t-T+1}^{t} 1_{(s is a trade day)} ]
```
"where 1_X is a 0-1 indicator on the Boolean expression X and T = number of days in the previous 3, 6 or 12 calendar months."
Symbols: `P_{i,s}` = close price of asset i on day s; `V_{i,s}` = traded volume on day s; `∨` = logical OR.

**(1.20)** Return-to-Turnover — "The average daily ratio of absolute total return to share turnover:"

```
(1/T) * sum_{s=t-T+1}^{t} |r_{i,s}| / ( V_{i,s} / N_{i,s} )
```
"where T = number of days in the last 360 with non-missing volume."
Symbols: `r_{i,s}` = daily total return; `V_{i,s}` = traded volume (shares); `N_{i,s}` = shares outstanding; `V/N` = share turnover.

Footnotes: **20** "One month is measured as 22 working days"; **21** "One month is measured as 22 working days".

### Tables
None.

### Numbers
- **11 months** momentum window with a **one month** lag; product indices `t-11 … t-1`.
- **22 working days** = definition of one month (footnotes 20 and 21).
- Proportion of Active Trade Days windows: **3, 6 or 12 calendar months** (T = number of days therein).
- Return-to-Turnover: **T = number of days in the last 360 with non-missing volume**.
- Equation numbers 1.17, 1.18, 1.19, 1.20.

### Terms
- Relative Strength – 11 Months; Historical Alpha; Reversal (log excess return over previous month); Proportion of Active Trade Days – 3M/6M/12M; Return-to-Turnover.
- "Active trade day"; "trade day"; 0-1 indicator `1_X`.

### Claims / methodological choices
- Momentum skips the most recent month (the standard 12-1 momentum construction, here 11 months ending at t-1), and Reversal is exactly that skipped month — the two are constructed to be non-overlapping.
- Momentum and reversal are both **excess** of the risk-free rate and taken in logs.
- A month is operationalised as **22 working days** rather than a calendar month for these two substyles, while the Proportion of Active Trade Days uses **calendar** months — an inconsistency the text does not remark on.
- "Active" is defined by *either* a price change *or* non-zero volume (logical OR), which counts a stale-priced but traded day as active.
- Return-to-Turnover's denominator window (last 360 days with non-missing volume) differs from the 3/6/12-month windows used by the neighbouring liquidity substyles; no justification is given.
- Return-to-Turnover is an illiquidity measure (high = illiquid) and is negated when aggregated (marked `*` in the style tables).

### Figures
None.

### Unreadable
- None material; equation (1.19)'s indicator subscripts are small but legible.

---

## PDF page 45 (printed p. 45)

### Headings
- Sub-headings (underlined, all within the **Liquidity** style continued from p.44): **Amihud Ratio**, **Growth of Trading Volume – 12 months & 36 months**, **Share Turnover – 3 months, 6 months & 12 months**, **Price Pressure – 1 month & 3 months**

### Equations

**(1.21)** Amihud Ratio — "The average daily ratio of absolute total return to value traded:"

```
(1/T) * sum_{s=t-T+1}^{t} |r_{i,s}| / ( V_{i,s} * P_{i,s} )
```
"where T = number of days in the last 360 with non-missing volume."
"An FX conversion is applied from local currency to USD to ensure comparability across all values."
Symbols: `V_{i,s} * P_{i,s}` = value traded (volume × price).

**(1.22)** Growth of Trading Volume – 12 & 36 months — "The ratio of the estimated slope coefficient from a regression of monthly traded volume on time, to the average Total Assets over the last T months:"

```
betâ_i / ( (1/T) * sum_{s=t-T+1}^{t} V_{i,s} )
```

**(1.23)** "where β̂_i is estimated in the following regression:"

```
V_{i,s} = alpha_i + beta_i * s + epsilon_{i,s}
```
"where s = t - T, ..., t"
Symbols: `V_{i,s}` = monthly traded volume; `s` = time index (the regressor); `beta_i` = trend slope.

**(1.24)** Share Turnover – 3, 6 & 12 months — "The natural logarithm of the average daily ratio of traded volume to number of shares outstanding over some specified window T:"

```
ln( (1/T) * sum_{s=t-T+1}^{t} V_{i,s} / N_{i,s} )
```
"where T = number of days in the previous 3, 6 or 12 calendar months."

**(1.25)** Price Pressure – 1 month & 3 months — "The proportion of aggregated price pressure over aggregated total return for some specified window T. No trade days are defined as those where the close price is equal to the close price of the previous day, and the traded volume is zero." / "The price pressure for asset i at time t over the previous T periods is defined as"

```
[ sum_{s=t-T+1}^{t} delta_{i,s} * |r_{i,s,tau}| ]  /  [ sum_{s=t-T+1}^{t} |r_{i,s,tau}| ]
```
"where r_{i,s,tau} is the estimate of asset return that would have occurred if the asset had traded, r_{i,s} is the asset return, delta_{i,s} is an indicator the asset would have felt 'price pressure' if traded, and τ is number of consecutive …" *(sentence continues onto the next page)*

### Tables
None.

### Numbers
- Amihud: **T = number of days in the last 360 with non-missing volume**.
- Growth of Trading Volume windows: **12 months & 36 months**.
- Share Turnover windows: **3, 6 or 12 calendar months**.
- Price Pressure windows: **1 month & 3 months**.
- Equation numbers 1.21, 1.22, 1.23, 1.24, 1.25.

### Terms
- Amihud Ratio; Growth of Trading Volume – 12M/36M; Share Turnover – 3M/6M/12M; Price Pressure – 1M/3M.
- "value traded" (= V×P); "no trade days"; "price pressure" indicator `delta_{i,s}`; `tau` = number of consecutive [non-trading days — definition truncated at the page break].

### Claims / methodological choices
- Amihud is computed in **USD after FX conversion** explicitly "to ensure comparability across all values" — one of the few explicitly justified choices in this appendix.
- **Inconsistency:** the prose for Growth of Trading Volume says the slope is divided by "the average **Total Assets** over the last T months", but the printed denominator in (1.22) is `(1/T) sum V_{i,s}` — the average **traded volume**, not Total Assets. One of the two is wrong; the formula is the more specific statement.
- The volume-trend regression (1.23) is a plain OLS of volume on a linear time index over s = t-T,…,t (i.e. T+1 observations, while the normalising average in (1.22) runs over T observations — an off-by-one between the two expressions as printed).
- Share Turnover is log-transformed; the same 3/6/12-calendar-month window convention as Proportion of Active Trade Days.
- Price Pressure is a *counterfactual* construct: it needs an estimate `r_{i,s,tau}` of the return that *would* have occurred had the asset traded, plus an indicator `delta_{i,s}` for whether the asset would have felt price pressure. The estimation method for `r_{i,s,tau}` is not given on this page.
- A "no trade day" requires **both** an unchanged close price **and** zero volume (logical AND) — the exact complement of the "active trade day" OR-condition in (1.19).
- Price Pressure enters styles negated (marked `*`).

### Figures
None.

### Unreadable
- p.45: the definition of `τ` is cut off mid-sentence at the page break ("… and τ is number of consecutive"); the completion is on PDF p.46.
- The `aladdin` logo in the footer is partly overlaid by the camera watermark; the footer "Page 45" is legible.
