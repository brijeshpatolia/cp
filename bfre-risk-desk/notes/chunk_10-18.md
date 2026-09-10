# BFRE Whitepaper — Transcription of PDF pages 10–18

Note on pagination: for this chunk the PDF page index and the printed footer page number **match exactly** (PDF p.10 = printed "Page 10", … PDF p.18 = printed "Page 18"). Every page carries the running header "BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)" and the footer logo "aladdin by BLACKROCK" with "Page N" at bottom-right. Scans are photographs of a bound printed copy (Galaxy Z Flip7 watermark), moderately legible; low-confidence items are flagged inline.

Audit note (second pass): every page image was re-read and, where the 952×1288 scan is too coarse for the naked eye, regions were cropped/upscaled and chart geometry was measured against the printed gridlines. Chart values below marked "measured" come from pixel measurement against the axis calibration (±0.5pp on bar charts, ±0.05 on Figure 1.11/1.6); they are still *not* printed numbers.

---

## PDF page 10 (printed p.10)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Table caption: *Table 1.2. Market and style factor summary statistics for the NAMR model, Mar 1996 – Dec 2013*
- (No new section heading on this page; body text continues a discussion of substyles and style-factor construction.)

### Tables

**Table 1.2. Market and style factor summary statistics for the NAMR model, Mar 1996 – Dec 2013**
13 rows × 5 data columns. **Verified digit-for-digit against a 2.6× crop of the scan.**

| Factor | Annualised Return | Annualised Volatility | Sharpe Ratio | Correlation with Market Factor | First-Order Autocorrelation |
|---|---|---|---|---|---|
| Market | 7.0% | 19.8% | 0.35 | 1.00 | 0.00 |
| Size | -1.2% | 3.7% | -0.33 | 0.23 | -0.05 |
| Volatility | -0.6% | 7.5% | -0.08 | 0.84 | 0.10 |
| Mid-cap | 0.9% | 1.8% | 0.52 | 0.04 | -0.08 |
| Reversal | -5.1% | 3.2% | -1.59 | -0.32 | 0.17 |
| Momentum | 5.4% | 3.8% | 1.43 | -0.02 | 0.22 |
| Liquidity | 2.7% | 5.5% | 0.49 | 0.69 | -0.02 |
| Value | 3.3% | 2.3% | 1.43 | 0.03 | 0.14 |
| Earnings Yield | 0.7% | 2.1% | 0.32 | 0.02 | 0.00 |
| Dividend Yield | -0.3% | 1.9% | -0.18 | 0.04 | 0.02 |
| Profitability | 3.1% | 2.2% | 1.37 | -0.14 | 0.08 |
| Growth | -2.0% | 2.0% | -1.01 | 0.16 | 0.03 |
| Sentiment | -0.1% | 1.5% | -0.05 | 0.01 | -0.02 |

Layout caveat (not a data issue): in the printed table the entries of the last three columns sit slightly higher within each row band than the row label, so the table must be read row-band by row-band; the mapping above is the correct one (checked against the top and bottom rows of the grid).

### Equations

Equation (1.3) — verified against a 3× crop:
```
r = X_{Mkt} f_{Mkt} + sum_{k in CCty} X_{CCty,k} f_{CCty,k} + sum_{j in CInd} X_{CInd,j} f_{CInd,j} + epsilon
```

Equation (1.4):
```
epsilon = X_{subSty,i} f_{subSty,i} + epsilon_tilde_i
```
(the second residual is epsilon with a tilde accent and subscript i; symbol glossary appears on PDF p.11.)

Indexing statement in the text: "for i = 1, 2, …, N (where N >= 200 is the number of candidate substyles) we run the following two-step regression".

### Numbers
- Table sample window: **Mar 1996 – Dec 2013** (NAMR model).
- All Table 1.2 cell values listed above.
- "over 200 substyles" in the exhaustive candidate set; formally **N >= 200**.
- Footnote 9: "Earnings-per-share (EPS) forecasts for the current fiscal year (FY1)".
- Cross-reference: full candidate-substyle list is in **Table 1.4**.

### Terms / factors named
Market, Size, Volatility, Mid-cap, Reversal, Momentum, Liquidity, Value, Earnings Yield, Dividend Yield, Profitability, Growth, Sentiment (the 12 NAMR style factors plus Market). Substyle examples mentioned in running text: total sales, number of analyst estimates for FY1 EPS. Factor-block labels: Mkt (market), CCty (core country), CInd (core industry), subSty (substyle).

### Claims / methodological choices
- Combining multiple substyles "leads a more robust definition of style factor returns and typically increases the explanatory power of the factor."
- **Standardisation choice** (paragraph verified word-for-word): "Substyles are standardised to a common scale to facilitate comparison of securities across different regions, and to allow substyles, measured in different units, to be combined to form style factor exposures. Conceptually, the standardisation process is similar to forming a z-score. The mean is defined as the square-root of market capitalisation weighted average value so that the transformed substyles (and styles) have the property that their weighted average is zero. Additionally, these values are divided by their **equally-weighted standard deviation** so that a value of +1 for a substyle or style can be interpreted as a security having an exposure of one standard deviation above the market average. An exposure of zero indicates that a security has the market average value for a given substyle, or style." (Note: the mean uses sqrt-market-cap weights while the standard deviation uses equal weights — the asymmetry is stated but not justified.)
- **Factor selection choice**: style factors are added **recursively** based on incremental significance, starting from a model with market, country and industry factors only, then regressing substyles against that model's residuals (two-step regression (1.3)–(1.4)).
- Candidate set drawn from "the academic literature and current investment risk practice."

### Figures
None on this page (table only).

### Unreadable
- Nothing materially unreadable; the table grid is clear. Minor: some column-header words sit at the very top of shaded cells but are legible.

---

## PDF page 11 (printed p.11)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.3. style exposure correlations in the NAMR model, Dec 2013*
- Inline lead-in word: "where" (introducing the symbol glossary for Equations 1.3–1.4)

### Tables / Figures

**Figure 1.3 — style exposure correlation matrix (NAMR model, Dec 2013).** A heat-shaded 12×12 symmetric matrix (diagonal = 1.00). Row and column order: Size, Volatility, MidCap, Reversal, Momentum, Liquidity, Value, Earnings Yield, Dividend Yield, Profitability, Growth, Sentiment. Shading is a **diverging** ramp — near-white at 0.00, darkening towards both +1 and -1 — so darkness alone does not encode sign.

| | Size | Volatility | MidCap | Reversal | Momentum | Liquidity | Value | Earnings Yield | Dividend Yield | Profitability | Growth | Sentiment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Size | 1.00 | -0.36 | -0.11 | 0.07 | 0.37 | 0.74 | 0.00 | 0.31 | -0.01 | 0.40 | -0.32 | 0.08 |
| Volatility | -0.36 | 1.00 | 0.03 | 0.06 | -0.20 | -0.30 | -0.05 | -0.35 | -0.46 | -0.38 | 0.24 | -0.15 |
| MidCap | -0.11 | 0.03 | 1.00 | -0.01 | 0.12 | 0.21 | -0.02 | 0.05 | -0.01 | 0.03 | -0.02 | 0.00 |
| Reversal | 0.07 | 0.06 | -0.01 | 1.00 | 0.08 | 0.03 | 0.02 | 0.01 | -0.05 | 0.00 | -0.03 | -0.01 |
| Momentum | 0.37 | -0.20 | 0.12 | 0.08 | 1.00 | 0.36 | -0.18 | 0.20 | -0.08 | 0.36 | -0.03 | 0.14 |
| Liquidity | 0.74 | -0.30 | 0.21 | 0.03 | 0.36 | 1.00 | -0.07 | 0.30 | 0.02 | 0.40 | -0.20 | 0.03 |
| Value | 0.00 | -0.05 | -0.02 | 0.02 | -0.18 | -0.07 | 1.00 | 0.40 | 0.17 | -0.01 | -0.27 | 0.05 |
| Earnings Yield | 0.31 | -0.35 | 0.05 | 0.01 | 0.20 | 0.30 | 0.40 | 1.00 | 0.20 | 0.64 | -0.20 | 0.05 |
| Dividend Yield | -0.01 | -0.46 | -0.01 | -0.05 | -0.08 | 0.02 | 0.17 | 0.20 | 1.00 | 0.07 | -0.10 | 0.06 |
| Profitability | 0.40 | -0.38 | 0.03 | 0.00 | 0.36 | 0.40 | -0.01 | 0.64 | 0.07 | 1.00 | -0.13 | 0.04 |
| Growth | -0.32 | 0.24 | -0.02 | -0.03 | -0.03 | -0.20 | -0.27 | -0.20 | -0.10 | -0.13 | 1.00 | -0.12 |
| Sentiment | 0.08 | -0.15 | 0.00 | -0.01 | 0.14 | 0.03 | 0.05 | 0.05 | 0.06 | 0.04 | -0.12 | 1.00 |

(All 144 cells re-read cell-by-cell on a 2.7× crop in the audit pass; the matrix is internally symmetric.)

### Equations / symbol definitions (the "where" glossary for Eq. 1.3–1.4)
```
r                          : Monthly local asset returns in excess of the risk-free rate
X_{Mkt} f_{Mkt}            : Market exposures and factor returns
X_{CCty,k} f_{CCty,k}      : Core country exposures and factor returns
X_{CInd,j} f_{CInd,j}      : Core industry exposures and factor returns
X_{subSty,i} f_{subSty,i}  : Substyle i exposures and factor returns
epsilon                    : Residual returns from the regression on market, core countries
                             and core industries
epsilon_tilde_i            : Residual returns from the regression on factors including substyle i
```

### Numbers
- Figure 1.3 snapshot date: **Dec 2013**.
- All correlation cells above; notable: Size–Liquidity **0.74** (highest off-diagonal), Earnings Yield–Profitability **0.64**, Volatility–Dividend Yield **-0.46**, Size–Volatility **-0.36**.
- "Special emphasis is placed on statistical significance in the **last five years** of the research history."
- Figure 1.4 shows the **top four** candidate substyles with the largest proportion of significant t-statistics in the **BFRE UK model** prior to the addition of any style factors.

### Terms / factors named
Style names as above. Named substyles for the size aggregation: **Sales, Market Cap, Broker Coverage, Total Assets** (the four that "should all be aggregated together to form the size factor").

### Claims / methodological choices
- Candidate substyles are ranked by **statistical significance metrics over the full sample (and sub-samples)**, with extra weight on the last five years "so that emerging stylistic themes are appropriately incorporated into the models."
- Typically top-ranking substyles "are all revolve around a common theme" (sic); the top four in the UK model share the theme of **size**.
- To decide the aggregation, "we run additional univariate regressions on various combinations of these four candidate substyles as in Equation (1.4)" — i.e. the grouping decision is empirical but the exact combination criterion/threshold is not stated on this page.
- The chosen style factor is then added into the first-step regression (sentence continues onto p.12).

### Unreadable
- Nothing material. Figure 1.3 heat shading makes a few light cells low-contrast at page scale, but all 144 numeric cells resolve on a 2.7× crop. Column headers "Earnings Yield"/"Dividend Yield" wrap onto two lines (legible).

---

## PDF page 12 (printed p.12)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.4. Proportion of Significant T-Statistics from the First Stage Regression*
- Figure caption: *Figure 1.5. Proportion of Significant T-Statistics from the Second Stage Regression*
- Section heading (bold): **Size**

### Equations

Equation (1.5) — verified against a 3× crop:
```
r = X_{Mkt} f_{Mkt} + sum_{k in CCty} X_{CCty,k} f_{CCty,k} + sum_{j in CInd} X_{CInd,j} f_{CInd,j} + X_{size} f_{size} + eta
```

Equation (1.6):
```
eta = X_{subSty,i} f_{subSty,i} + eta_tilde_i
```
(i.e. exactly (1.3)/(1.4) with the newly-accepted size factor X_size f_size added to the first stage; the first-stage residual is renamed eta and the second-stage residual eta-tilde-i. The accent over the second eta prints as a short bar/tilde and cannot be distinguished from a macron at this scan resolution; by analogy with (1.4) it is a tilde.)

Lead-in sentence (carried over from p.11): "step regression in Equation (1.3) and re-run the two-step regression".

### Numbers
- **Stopping rule**: the recursive process "is repeated until the largest proportion of t-statistics from the second step univariate regression is no larger than **10% - 15%**."
- Figure 1.4 y-axis: 0.0% to **45.0%** in 5.0% increments (top label legible as 45.0%).
- Figure 1.5 y-axis: 0.0% to 45.0% in 5.0% increments (see Unreadable — the top label renders like "45.5%" but the label pitch is uniform, which forces 45.0%).
- Bar heights are not printed as data labels; measured values are given in the Figures section.

### Terms / factors named
- Figure 1.4 categories (first-stage top substyles): **Sales, Market Cap, Broker Coverage, Total Assets**.
- Figure 1.5 categories (second-stage top substyles, after size is added): **Historical Alpha, Relative Strength 11 Months, Log Price, Predicted Earnings Growth**.
- Section factor: **Size**.

### Claims / methodological choices
- After adding size, "the ranking of substyles after this regression is shown in Figure 1.5, which suggests **momentum** is the next style factor to add to the model."
- "We follow a similar procedure as in the previous stage to form the next style factor and incorporate this into the first-step regression in Equation (1.5)."
- Explicit admission of judgement: "Throughout the whole selection process, **qualitative judgement and statistical analysis are combined** to identify substyle factors that explain asset returns and how they should be grouped together into a style factor." (No formal criterion is given for the qualitative part.)
- **Size rationale**: "The size factor captures the increased risks associated with investing in small-cap companies as compared with large-cap companies. Large companies are typically more immune to difficult economic conditions and general downturns in the business cycle, as compared with smaller companies. In this sense, similar sized companies behave in a similar fashion at different points of the business cycle, and so size has significant explanatory power in explaining asset return commonality."

### Figures
- **Figure 1.4** — vertical bar chart, 4 bars, y = proportion of significant t-statistics (0.0%–45.0%). Measured heights (no printed data labels): Sales ≈ **43.9%**, Market Cap ≈ **43.9%**, Broker Coverage ≈ **43.6%**, Total Assets ≈ **34.8%**. Shape: three near-identical tall bars and a clearly lower fourth.
- **Figure 1.5** — vertical bar chart, 4 bars, same y-scale. Measured heights: Historical Alpha ≈ **40.2%**, Relative Strength 11 Months ≈ **40.5%**, Log Price ≈ **26.7%**, Predicted Earnings Growth ≈ **6.9%**. Shape: two tall near-equal bars, then a sharp two-step decline.

### Unreadable
- Exact bar values in Figures 1.4 and 1.5 (no data labels; the percentages above are measured off the calibrated axis, not printed).
- Figure 1.5's top y-axis label images as "45.5%" at this resolution. All ten of its labels are evenly pitched (14.4 px apart, same as Figure 1.4's confirmed 45.0/40.0/…/0.0 ladder), so the value is 45.0% and the apparent extra "5" is a scan artefact. [UNREADABLE: the glyph itself — 45.0% vs 45.5% — cannot be settled from the ink alone.]

---

## PDF page 13 (printed p.13)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.6. substyle exposures of AOL Inc., Jul 1996 – Jul 2003*
- (Body continues the **Size** section.)

### Equations
None on this page.

### Numbers
- Figure 1.6 window: **Jul 1996 – Jul 2003**; y-axis "substyle exposure" from **-1.5 to 2.5** in 0.5 steps; x-axis quarterly tick labels Jul 1996, Oct 1996, Jan 1997, Apr 1997, Jul 1997, Oct 1997, Jan 1998, Apr 1998, Jul 1998, Oct 1998, Jan 1999, Apr 1999, Jul 1999, Oct 1999, Jan 2000, Apr 2000, Jul 2000, Oct 2000, Jan 2001, Apr 2001, Jul 2001, Oct 2001, Jan 2002, Apr 2002, Jul 2002, Oct 2002, Jan 2003, Apr 2003, Jul 2003 (29 labels).
- AOL market-cap exposure "increases substantially during **1998-9** following strong price performance."
- The NAMR size factor's negative cumulative returns are visible "in figure 1.7 **since 2000**" (the "since 2000" attaches to the size factor's underperformance of large- vs small-caps, **not** to the Fama-French series).
- **Correlation of 0.67** between the NAMR size factor cumulative return series and the (negated) Fama-French SMB series "over the entire history."
- References cited: **Banz [10]** (small-cap risk premium).
- Footnote 10: "Source: http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html".

### Terms / factors named
- Substyles plotted: **market capitalisation**, **total sales**.
- **Fama-French SMB ('small minus big')** factor.
- Models named: **North America model / NAMR model**.
- Company example: **AOL Inc.** ("before and after the dotcom bubble").

### Claims / methodological choices
- "Size is traditionally defined using market capitalisation; however, this only offers a single, and often incomplete, measure of the size of a company. In contrast, the BFRE definition uses different formulations of size based on **balance sheet information, market data and analyst estimate data** leading to a more robust definition."
- AOL case study: market capitalisation exposure "is significantly positive at the beginning of the period, and increases substantially during 1998-9 following strong price performance. A measure of size based on market capitalisation alone would confer large-size status on AOL, and reduce its risk forecast accordingly. However, this fails to capture the underlying fundamentals, such as total sales, which describe a significantly smaller, and riskier, company relative to the market."
- Quant-community relevance: "Size is also an important factor within the quantitative investment community since small-cap stocks have historically earned a risk premium relative to their large-cap peers (see Banz [10])."
- Figure 1.7 (next page) interpretation: the NAMR size factor cumulative return "represents the return to a portfolio of securities long large-cap and short small-cap stocks, after neutralising other style tilts, and industry/country effects in the model."
- The Fama-French SMB series is **negated** "to align with the convention used in the BFRE size factor." Not expected to match perfectly "due to different definitions and construction," but the two "are closely related and have a correlation of 0.67 over the entire history."

### Figures
- **Figure 1.6** — two-line time series of AOL Inc. substyle exposures, Jul 1996–Jul 2003. Legend: market capitalisation, total sales. Measured against the gridlines: market-cap exposure starts ≈ **0.8**, sags to ≈ 0.7–0.8 through 1997, climbs from mid-1998 (crossing 1.0 around Oct 1998) to ≈ 1.95–2.2 by Jan 1999, holds ≈ 2.0–2.2 through 1999–2000, cuts down sharply to ≈ **1.5** around Oct 2000, rebounds to ≈ 2.2 in early 2001, drifts to ≈ 1.8–1.95 through 2002–early 2003, then drops steeply in the final quarter to ≈ **1.55–1.6** at Jul 2003. Total-sales exposure starts at ≈ **-0.9**, steps to ≈ -0.45 by Oct 1996 and holds through 1997, ≈ -0.25 in 1998, ≈ -0.1 by late 1998/1999, then jumps to ≈ **0.75–0.85** around Jan 2000; it dips to ≈ 0.45 around Oct 2000–Jan 2001, recovers to ≈ 0.85 and rises stepwise to ≈ **1.15–1.2** at Jul 2003. Qualitative point: a large and persistent gap between the two size substyles, i.e. market cap says "large", sales says "small".

### Unreadable
- Precise data-point values in Figure 1.6 (line chart with no labels); values above are measured against the gridlines, with the caveat that the scanned page is warped (gridlines drift up by ~0.15 exposure units towards the right edge), so late-sample readings carry the larger error.

---

## PDF page 14 (printed p.14)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.7. cumulative returns to NAMR size and Fama-French SMB, Mar 1996 – Dec 2013*
- Section heading (bold): **Volatility**

### Equations
None on this page (prose description of the beta regression only).

### Numbers
- Figure 1.7 window: **Mar 1996 – Dec 2013**; y-axis "cumulative returns" from **-50% to 60%** in 10% steps; x-axis labels (confirmed on a 6× rotated crop) Mar 1996, **Feb 1997**, Mar 1998, Mar 1999, Mar 2000, Mar 2001, Mar 2002, Mar 2003, Mar 2004, Mar 2005, Mar 2006, Mar 2007, Mar 2008, Mar 2009, Mar 2010, Mar 2011, Mar 2012, Mar 2013. (The second label really is "Feb 1997" — it is legible, not an artefact.)
- Historical beta regression: **5 years of weekly data**, exponentially weighted "to place more emphasis on return behaviour in the previous **52 weeks**."
- Inclusion threshold: "A value in excess of **10%** [proportion of significant t-statistics] indicates a statistically significant style effect, and would be considered for inclusion in the models."
- Cross-sectional correlation between **volatility and size exposures = -0.36** ("as shown in figure 1.3").
- Volatility's correlation with the market factor is very high (Table 1.2 value: **0.84**).
- Footnote 11: "t-statistics are based on **monthly cross-sectional regressions**."

### Terms / factors named
- **Volatility** factor; inputs: "various measures of historical return dispersion, and historical beta."
- **Historical beta**: univariate regression of asset returns against a **capitalisation-weighted market index**.
- Sectors named in the Figure 1.9 lead-in: **IT**, **Telecoms**, **Financials**.
- Series in Figure 1.7: **Fama-French SMB (negative)**, **NAMR Size**.

### Claims / methodological choices
- Beta estimation choice: univariate regression vs cap-weighted market index, 5y weekly, exponentially weighted toward the last 52 weeks. (Half-life not stated on this page.)
- "Volatility is very highly correlated with the market (see table 1.2) and is empirically proven to have significant explanatory power in explaining asset return commonality."
- Figure 1.8's proportion-of-significant-t-stats is "a standard measure of factor efficacy and is one of metrics used to select which style factors are eligible for inclusion in BFRE" (sic, "one of metrics").
- Volatility's proportion of significant t-stats is "considerably higher than this threshold and larger than the other style factors, and incidentally **most industry and country factors**, which shows the relative strength of the volatility factor in explaining cross-sectional asset returns."
- "Large volatility exposures tend to be associated with small-cap stocks through time… This negative relationship is fairly stable over time. Consequently, portfolios which are positively exposed to size are commonly negatively exposed to volatility, and vice versa."
- Sector observation (leading into Fig 1.9): "The IT sector, and to a lesser extent the Telecoms sector, exhibit the highest levels of volatility exposure leading up to, and during, the dotcom crisis. Financials have relatively…" (sentence completes on p.15).

### Figures
- **Figure 1.7** — two overlaid cumulative-return series (Fama-French SMB negated, light grey; NAMR Size, dark). Both start at 0% in Mar 1996; SMB(neg) dips to ≈ **-8%** in late 1996 while NAMR Size dips only to ≈ -2%. Both then climb: SMB(neg) spikes to ≈ 45% in late 1998 and peaks ≈ **47%** in early/mid 1999, while NAMR Size peaks ≈ **19–20%** in 1999. SMB(neg) has an abrupt vertical drop around **Mar 2000** (briefly to ≈ -9%) then rebounds to ≈ 22% before both series fall through 2000–2003. NAMR Size crosses 0% during 2002 and settles at ≈ **-9% to -13% from 2003 through 2009**, then drifts lower to ≈ -18% by 2011 and ends ≈ **-17% to -18%**. SMB(neg) drops sharply in 2003 to ≈ -20%, oscillates ≈ -20% to -27% through 2004–2007, recovers to ≈ -13% in 2008, then falls to ≈ -30% to -35% over 2010–2013, ending ≈ **-35%**. Qualitative shape: co-moving, sharp dotcom-era spike then long negative drift, i.e. long-large/short-small has lost money over the sample.

### Unreadable
- Exact plotted values in Figure 1.7 (no data labels); values above are measured against the calibrated axis.

---

## PDF page 15 (printed p.15)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.8. proportion of significant t-statistics for NAMR style factors, Mar 1996 – Jun 2013*
- Figure caption: *Figure 1.9. average NAMR volatility factor exposures by sector, Mar 1996 – Dec 2013*
- Section heading (bold): **Mid-Cap & Small-Cap**

### Equations
None on this page, and no equation cross-reference either. (The forward reference to Equations (1.47)/(1.48) is on p.16, not here.)

### Numbers
- Figure 1.8 window: **Mar 1996 – Jun 2013** (note: different end date from most other exhibits, which end Dec 2013). Y-axis "proportion of significant t-stats" 0%–70% in 10% steps. X-axis label: "NAMR style factors".
- Figure 1.9 window: **Mar 1996 – Dec 2013**; columns are years **1996 … 2013** (18 columns); colour-scale legend runs **1.5 (top) → 0 (middle) → -1.5 (bottom)**.
- Financial-crisis reference: exposures increase significantly "during the financial crisis in **2007-8**", at which point the average Financials exposure "changes sign to indicate above average levels of volatility in this sector."
- Closing line, running into p.16: "Figure 1.10 shows the proportion of significant t-statistics for different market capitalisation deciles of the EMEA…"

### Terms / factors named
- Figure 1.8 x-axis categories, in descending order of significance: **Volatility, Momentum, Size, Reversal, Value, Liquidity, Dividend Yield, MidCap, Growth, Profitability, Sentiment, Earnings Yield**.
- Figure 1.9 sector rows (10, GICS-style): **Consumer Discretionary, Consumer Staples, Energy, Financials, Healthcare, Industrials, IT, Materials, Telecoms, Utilities**.
- New factors introduced: **Mid-Cap**, **Small-Cap**.
- Model referenced at the foot of the page: EMEA model (Figure 1.10).

### Claims / methodological choices
- Sector stability claim: "Other sectors are relatively more stable, such as **Utilities and Consumer Staples**, which have consistently lower volatility exposures over the entire period."
- **Mid-Cap & Small-Cap rationale**: "Research into the statistical significance of different market capitalisation deciles of the estimation universe reveals that there is additional asset return commonality present in the mid-cap and small-cap segments that is not fully captured by the existing size factor. **Most BFRE models therefore also include a small-cap or mid-cap factor** to incorporate this source of commonality."

### Figures
- **Figure 1.8** — descending bar chart of the proportion of significant t-statistics for each NAMR style factor. Measured heights (no printed data labels): Volatility ≈ **63%**, Momentum ≈ **50%**, Size ≈ **42%**, Reversal ≈ **37%**, Value ≈ **34%**, Liquidity ≈ **32%**, Dividend Yield ≈ **23%**, MidCap ≈ **20%**, Growth ≈ **18%**, Profitability ≈ **14%**, Sentiment ≈ **7%**, Earnings Yield ≈ **4–5%**. Shape: monotone decline. Against the 10% inclusion threshold stated on p.14, only **Sentiment and Earnings Yield** fall below it; Profitability at ≈14% is clearly above.
- **Figure 1.9** — heat-map grid, 10 sector rows × 18 year columns (1996–2013). **The greyscale ramp is diverging, not monotone**: the legend bar is dark at +1.5, near-white at 0, and dark again at -1.5 (verified by sampling the legend strip). Darkness therefore encodes |exposure|, not sign, and no cell's sign can be read from the scan alone. Shading pattern: the **IT** row is the darkest band in the figure and stays dark across the whole sample (the body text elsewhere identifies IT as the highest-exposure sector); **Industrials** is near-white throughout (i.e. close to the market average); **Telecoms** is dark in the dotcom era and again strongly from ~2006 to 2013; **Materials** darkens from ~2006 onwards; **Financials** is light/near-white through the early sample and darkens from ~2006–2009 (the text says its average exposure changes sign in 2007-8); **Consumer Staples** and **Utilities** carry mid-grey shading for much of the period, which the body text interprets as consistently *lower* (i.e. negative) exposures.

### Unreadable
- Exact bar percentages in Figure 1.8 (measured from the calibrated axis — not printed).
- Individual cell values in the Figure 1.9 heat map cannot be read numerically, and because the ramp is diverging in greyscale, **the sign of any individual cell is not recoverable from the scan**. Sector row labels all resolve.

---

## PDF page 16 (printed p.16)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.10. proportion of significant t-statistics for EMEA universe deciles, Mar 1996 – Dec 2010*
- Section heading (bold): **Reversal & Momentum**

### Equations
None printed here; forward reference: "See Equations **(1.47)** and **(1.48)** for more details on the exact functional form" of the smoothed small-cap/mid-cap exposures.

### Numbers
- Figure 1.10 window: **Mar 1996 – Dec 2010** (note: ends 2010, earlier than other exhibits). Y-axis "proportion of significant t-stats" 0%–25% in 5% steps; dashed horizontal reference line at **10%**. X-axis: "Estimation Universe Deciles by Market Capitalisation (**1 = Largest, 10 = Smallest**)", deciles 1–10. Two series: **Before Small-Cap** and **After Small-Cap**.
- "Prior to the addition of a small-cap factor, there is significant explanatory power in the lower deciles, **9 and 10**, in excess of the **10% threshold used to determine whether styles are eligible for inclusion in the model**."
- "The **mid-cap** factor primarily represents **decile 6 and 7**, whilst the **small-cap** factor represents assets in **deciles 9 and 10**."
- Reversal horizon: "a near-term reversal in strong stock price performance measured over a **one month** period."
- Footnote 12: "t-statistics are based on **monthly cross-sectional regressions**."
- References cited: **Jegadeesh [11]**, **Jacobs and Levy [12]** (reversal), **Subrahmanyam [13]** (behavioural overreaction).

### Terms / factors named
- **Small-cap**, **mid-cap** factors; **Reversal**, **Momentum**.
- Model coverage list: small-cap "was found to be significant in the **WRLD, EMEA, APXJ, AUST, UKIN, USAM and EMKT** models, whilst mid-cap was found to be significant in the **NAMR** model."

### Claims / methodological choices
- Test design: "For each decile, a set of model residuals were regressed against **0/1 dummy variables** indicating decile membership."
- Result: before adding a small-cap factor, deciles 9 and 10 exceed the 10% threshold; "Following the addition of a small-cap factor, the proportion of t-statistics for these deciles is no longer statistically significant."
- **Smoothing choice**: "The small-cap and mid-cap factors are defined as **smoothed versions of dummy variables** indicating membership to particular deciles of the model estimation universe. A smooth function is used in preference to 0/1 indicators **to mitigate instability in exposures for assets on the decile boundaries**."
- Reversal/momentum are "based on anomalies identified in stock market research. Both factors have significant power in explaining the cross-sectional equity returns, and by extension, asset return covariance and beta. Additionally, both are also associated with significant returns in excess of the market which cannot be explained using other common factors."
- Behavioural justification for reversal: "market investors overreacting to stock information in the near-term."

### Figures
- **Figure 1.10** — clustered vertical bar chart, 10 decile groups × 2 series (Before Small-Cap, After Small-Cap), with a dashed 10% threshold line. Measured heights (no printed data labels), Before / After:
  - decile 1: **0.4% / ~0%** (the After bar has no visible height)
  - decile 2: **4.8% / 4.2%**
  - decile 3: **6.4% / 5.8%**
  - decile 4: **3.7% / 4.2%** (After above Before)
  - decile 5: **5.9% / 3.7%**
  - decile 6: **6.6% / 3.9%**
  - decile 7: **4.6% / 3.5%**
  - decile 8: **5.8% / 7.4%** (After above Before)
  - decile 9: **10.8% / 2.1%**
  - decile 10: **21.1% / 3.4%**
  Only deciles 9 and 10 sit above the dashed 10% line before the small-cap factor is added, and both fall far below it afterwards — exactly the claim the body text makes.

### Unreadable
- Exact bar percentages in Figure 1.10 (no data labels; measured from the calibrated axis, ±0.5pp).
- (Resolved in audit: an earlier reading flagged decile 9's two bars as indistinguishable. On a 7× crop they are plainly different — 10.8% before vs 2.1% after — so the figure does corroborate the text.)

---

## PDF page 17 (printed p.17)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.11. style exposure autocorrelations in the NAMR model, Jan 2012 – Dec 2013*
- (Body continues **Reversal & Momentum**.)

### Equations
None on this page.

### Numbers
- Figure 1.11 window: **Jan 2012 – Dec 2013** (24 months). Y-axis: "style exposure correlation: Dec 2013 vs. previous months", scale **-0.2 to 1** (ticks at -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1). X-axis: "Number of months from Dec 2013", ticks **0 through 23**.
- Momentum definition: "The momentum effect has been observed over various horizons, typically ranging from **three months to 12 months**. The BFRE definition focuses on stock returns over the **previous 11 months with a one month lag** to exclude the reversal effect."
- Reference to **Table 1.2**: "momentum and reversal have the largest Sharpe ratios relative to other style factors" (Momentum 1.43, Reversal -1.59 in magnitude; Value is also 1.43) and momentum/reversal returns "are associated with a significant first-order autocorrelation" (Momentum 0.22, Reversal 0.17).
- Events: "**Quant crisis in 2007**" (momentum series flat-lines), then "a significant drawdown during the financial crisis period."
- Reference cited: **Jegadeesh and Titman [14]** (momentum).

### Terms / factors named
- Figure 1.11 legend (verified on a 7× crop), dashed series: **Dividend Yield, Earnings Yield, Mid-Cap, Profitability, Growth, Liquidity**; solid series: **Momentum, Reversal, Sentiment, Size, Value, Volatility**.

### Claims / methodological choices
- Momentum definition/attribution: "The momentum factor is a related effect, first documented in Jegadeesh and Titman [14], and captures the tendency of previous stock winners to continue rising, and for previous stock losers to continue losing."
- **Design choice**: momentum measured over the previous 11 months with a 1-month lag, the lag explicitly there "to exclude the reversal effect."
- Behavioural justification for momentum: "market investors systematically underreacting to newly available company information, and failing to adjust their expectations in the medium-term."
- **What Figure 1.11 plots**: "Figure 1.11 shows the cross-sectional exposure correlations of each style in December 2013 against its previous values for every month in the previous two years, i.e. the correlation of style exposures in Dec 2013 with the previous month, 2 months ago, etc. Correlations close to one indicate a high degree of persistence in asset style exposures through time."
- Exposure persistence: "In contrast to most style factors in BFRE, the reversal and momentum factor exposures of a security can vary considerably through time… **Reversal and momentum clearly exhibit the least persistence** relative to other styles, which reflects the highly time-varying nature of these factor exposures."
- Return persistence: "It is well-documented in the above academic references that a momentum-based portfolio strategy is rewarded with significant positive returns through time, and likewise, a reversal strategy with negative returns… A significant first-order autocorrelation indicates a high degree of persistence in returns."
- Momentum performance narrative (Figure 1.12): "The stable upward trend in the figure below is only briefly interrupted during the Quant crisis in 2007 where the series begins to flat-line prior to suffering a significant drawdown during the financial crisis period. Thereafter, the series continues on its characteristic upward trajectory."
- Modelling choice flagged: "Some multi-factor risk models combine reversal and momentum into a single factor; however, the BFRE models…" (sentence completes on p.18: they are kept separate).

### Figures
- **Figure 1.11** — 12 line series, all pinned at 1.0 at lag 0 and decaying as the lag increases to 23 months. Measured at lag ≈23 the distinct traces sit at ≈ **0.99** (one solid line essentially flat across the whole range), ≈ **0.90** and ≈ **0.87** (dashed, closely spaced), ≈ **0.76**, ≈ **0.64**, ≈ **0.61**, ≈ **0.48**, ≈ **0.42**, ≈ **0.29**, and ≈ **0.09**; two of the twelve overlap others and cannot be separated. Only **one** series collapses immediately — it falls from 1.0 to ≈ 0.0 by lag 1 and then oscillates between ≈ -0.05 and ≈ +0.17 for the remaining lags (a one-month-return exposure behaves this way, so this is presumably reversal). Two further solid series decline steadily rather than abruptly, reaching ≈ 0.42 and ≈ 0.29 at lag 23 — these are the next-least-persistent traces and one of them is presumably momentum. [UNREADABLE: the mapping of individual traces to legend entries — dash patterns and line weights are not separable at this scan resolution.]

### Unreadable
- Mapping of individual plotted lines to legend entries in Figure 1.11.
- Exact correlation values at each lag (no data labels); the figures above are measured against the calibrated axis.

---

## PDF page 18 (printed p.18)

### Headings
- Running header: BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.12. cumulative performance of momentum in the EMEA model, Mar 1996 – Dec 2013*
- Section heading (bold): **Liquidity**

### Equations
None on this page.

### Numbers
- Figure 1.12 window: **Mar 1996 – Dec 2013**; y-axis "cumulative returns" from **-50% to 250%** in 50% steps; x-axis tick labels (all 18 resolved on a 6× rotated crop): Mar 1996, **Feb 1997**, Mar 1998, Mar 1999, Mar 2000, Mar 2001, Mar 2002, **Mar 2003**, Apr 2004, Apr 2005, Apr 2006, Apr 2007, Apr 2008, Apr 2009, May 2010, May 2011, May 2012, May 2013. (The Mar→Apr→May drift across the axis is real, not a misreading.)
- References cited on this page: **Lee and Stefek [15]** (optimisation biases), **Sarr and Lybek [16]**, **Connor et al. [17]** (liquidity definitions), **Bekaert et al [18]** (volume-based measures; also cited for price impact), **Amihud [19]**, **Florackis et al. [20]** (price-impact measures), **Goyenko et al. [21]** (Amihud ratio correlation with alternative measures).

### Terms / factors named
- **Liquidity** factor.
- Volume-based liquidity substyle measures: **share turnover**, **active trade days** ("distinguish liquid stocks by the magnitude and frequency of trades and in doing so capture market breadth").
- Price-impact liquidity substyle measures: **Amihud ratio**, **return-to-turnover ratio (RTO)**, **price pressure**.
- Referenced exhibit: **Figure 1.13** — correlation between the various substyles used to define liquidity in the **EMEA model**.

### Claims / methodological choices
- **Reversal/momentum kept separate**: "…separate these into different factors. This decision allows model users to isolate these effects in risk decomposition and factor attribution analyses. This separation also avoids biases in portfolio optimisations for quantitative equity portfolios that invest in assets heavily tilted towards these factors (see Lee and Stefek [15])."
- **What the liquidity factor is** (opening definition): "The liquidity factor captures the differential return and risk of more liquid stocks relative to less liquid stocks controlling for industry, country and other style effects."
- Liquidity definition rationale: "Liquidity is not directly observable and can relate to a number of different stock characteristics (see Sarr and Lybek [16] or Connor et al. [17]). Liquid stocks typically entail low transaction costs (e.g. low bid-ask spreads); trade frequently at large volumes with minimal price impact; and can be converted into cash quickly. **Given there is no single, widely-accepted metric that captures all of these dimensions, the BFRE liquidity factor uses multiple substyles in its definition.**"
- Regional variation: "The definition of liquidity varies depending on the region or country of interest, and can use a combination of volume-based measures, and price impact measures."
- Interpretation of measures: "Amihud ratio and RTO substyles relate price movement with the volume of transactions and identify illiquid securities as those which exhibit larger price moves for the same level of volume. Price pressure relates price impact with lengthy periods of consecutive non-trading days and identifies assets prone to a subsequent return 'catch-up' effect."
- **Data choice with justification**: "The literature also documents liquidity measures based on higher frequency, intraday data, however, **BFRE only uses low-frequency data as these are more readily available for the different markets covered by BFRE**." Additionally Goyenko et al. [21] "show the Amihud ratio has a significant positive correlation with some of these alternative measures."
- "Although these measures capture different aspects of liquidity, they are nevertheless strongly related… There is significant positive correlation amongst, as well as between, the various volume-based and price impact measures" (continues past this page).

### Figures
- **Figure 1.12** — single cumulative-return line for the EMEA momentum factor, Mar 1996 – Dec 2013. Measured against the calibrated axis: starts at **0%** in Mar 1996, rises with noise to ≈ **45%** by 1999–2000, ≈ **89%** at Mar 2003, ≈ **105–120%** through 2005–2006, reaching ≈ **127%** by mid-2007; it then chops sideways between ≈ **137% and 148%** from late 2007 through early 2009 (the Quant-crisis flat-line), drops to a trough of ≈ **120–122%** in mid-2009 (the financial-crisis drawdown), and then trends strongly upward to ≈ **216%** at the end of the sample. Overall shape: persistent, near-monotone upward drift with one crisis-era interruption.

### Unreadable
- Exact plotted values in Figure 1.12 (no data labels); the percentages above are measured, not printed.
- (Resolved in audit: the rotated x-axis month prefixes are legible at 6× — see the tick list above.)
