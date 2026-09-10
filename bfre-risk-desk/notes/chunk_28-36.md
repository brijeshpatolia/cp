# BFRE whitepaper — transcription of PDF pages 28–36

Source images: `/tmp/claude-0/-home-user-cp/79206b60-659d-5f16-a034-7d8ab14cc34a/scratchpad/img/p028.jpg` … `p036.jpg`

Every page carries the running header banner **BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)** and the footer logo **aladdin — by BlackRock** with a printed page number at bottom-right. For pages 28–36 the printed footer number equals the PDF page index (PDF p.28 → "Page 28", … PDF p.36 → "Page 36"). No offset. Verified on every page of this range.

**Source-quality caveat (applies to everything below).** The "PDF" pages are phone photographs of a printed copy (a "Galaxy Z Flip7" watermark is burned into each frame) at roughly **950 × 1300 px per full page**, and `scratchpad/pages/*.txt` is empty — there is **no text layer**, so every character here was read off a photograph. Body text at that resolution is reliable; 5–6 px glyphs (chart tick labels, rotated category labels, the small figures in the banner of Figure 1.18) are at the edge of legibility and are flagged individually. Where a small glyph was recovered it was done by cropping, upscaling ×10–24 with Lanczos, autocontrast and — for 45°-rotated labels — a −45° deskew before reading.

Two pages (29 and 33) are largely blank apart from a short block of text; the remainder of each shows a faint, low-contrast "ghost" of the text of the *following* page. I enhanced those regions (autocontrast + unsharp) and confirmed the ghost text is a duplicate of pp. 30 and 34 respectively — i.e. show-through / bleed-through from the reverse of the leaf, not distinct content. It is recorded as such, not transcribed as page content. The same show-through appears in the lower half of pp. 31 and 36 (from pp. 32 and 37).

**Audit pass.** Every page image in this range was re-read independently against this file. Findings and their disposition:

| # | Page | Issue | Disposition |
|---|---|---|---|
| 1 | 35 | Claimed the ten "Top Style Contributions" labels were illegible and unrecoverable | **Wrong — withdrawn.** All ten recovered by deskewing: Volatility, Momentum, Size, Yield, Reversal, Emerging, Sentiment, Growth, Market, Profitability |
| 2 | 35 | Second large negative industry exposure attributed to **Media** | **Wrong — corrected.** It belongs to Food Household (4th); Media's exposure is ≈ +4.5% of NAV. A third negative (Chemicals - Agr, ≈ −3%) had been missed entirely |
| 3 | 35 | Asset-exposure dots stated as "+1 to +2.5% of NAV" | Corrected to ≈ +1.3 to +3.0% |
| 4 | 35 | FX base-currency codes listed as confirmed terms | **Demoted to `[TENTATIVE]`** — only the `/USD` suffix is actually legible |
| 5 | 35 | "~15" asset bars; 9 jumbled tentative names, "several others unrecoverable" | Replaced with the ordered 15-name list, per-item confidence, and 2 explicit `[UNREADABLE]` slots |
| 6 | 30 | Terms line implied **style** exposures are dummy variables | **Wrong — corrected.** The source assigns dummy variables to industry, country and currency only |
| 7 | 32 | Opening sentence of MODEL ESTIMATION DIAGNOSTICS omitted | Restored ("The model estimation is a core component of the model construction process.") |
| 8 | 28 | Structural/empirical passage paraphrased | Replaced with verbatim text incl. "The first approach…" / "In contrast, the second – empirical– approach" |
| 9 | 31 | Row-alignment flagged as broadly ambiguous | Narrowed — three cells resolved at zoom, four genuinely straddle; listed individually |
| 10 | 36 | "daily basis" | Source actually prints **"dailybasis"**; marked *[sic]* |
| 11 | 35 | Pie "Act Sec 1%" | Kept, but relabelled `[INFERRED]` — the glyph is at least as consistent with 2%; only the sum-to-100 argument selects 1% |
| 12 | 35 | Bar magnitudes stated alongside transcribed numbers | Explicit warning added: all bar/dot magnitudes are pixel measurements (±10%), not printed values |
| 13 | all | No note on source resolution | Source-quality caveat added above |

**Re-verified correct, no change needed:** Table 1.3 (every cell, digit for digit); ±8% / ±20% currency truncation bounds; 1–2 day lag; 1-month horizon; 1996 to 2013; 10% t-statistic threshold; footnote markers 16 and 17 and their text; references [17] and [27]; February 2018; the entire p.31 table body and all four of its footnotes; the p.35 banner (2.99% / 1.02 / 15.62% / 14.98% / EUR); all five directly-read pie percentages; all six axis tick-label sets in Figure 1.18; the ten country and ten industry category labels; the Thursday / previous-Wednesday update cycle; and the ghost-page attributions.

---

## PDF page 28 (printed p. 28)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **Specific Return Correlation** (bold sub-heading)
- **Structural & Empirical Models** (bold sub-heading)
- Table caption: *Table 1.3. BFRE specific risk parameters*

### Equations
None. No displayed mathematics on this page.

### Tables

**Table 1.3. BFRE specific risk parameters** — 3 data columns + 1 row-label column; 2 data rows (header row shaded grey).

| Model frequency | Half-life | Observations | Newey-West Lag |
|---|---|---|---|
| Daily | 125 days | 375 days | 10 days |
| Weekly (WRLD and EMKT) | 26 weeks | 104 weeks | 2 weeks |

### Numbers
- p.28: 125 days = half-life of the daily-frequency specific risk model
- p.28: 375 days = number of observations used, daily model
- p.28: 10 days = Newey-West lag, daily model
- p.28: 26 weeks = half-life of the weekly (WRLD and EMKT) specific risk model
- p.28: 104 weeks = number of observations used, weekly model
- p.28: 2 weeks = Newey-West lag, weekly model
- p.28: 1 = constant override value imposed on specific return correlation when correlations are not estimated
- p.28: 1 = limiting value of the weight placed on the time-series specific-risk forecast (cross-sectional overlay weight → 0)

### Terms / named entities
- WRLD, EMKT (the two weekly-frequency model variants named in Table 1.3)
- Cross-sectional overlay (specific risk)
- Time-series forecast vs. cross-sectional forecast (of specific risk)
- Specific Return Correlation
- Structural approach / Empirical approach (the two specific-covariance methodologies)
- Related-asset groups affected: (a) cross-listings, (b) derived securities — ADRs, GDRs, NVDRs & Certificates — and their root assets
- Share-class examples: 'A' and 'B' shares in Sweden; 'Registered' and 'Bearer' shares in Switzerland; ordinary and preference shares
- IPOs (as the example of assets with little or no history)

### Claims / methodological choices
- (first, partial line, continuing from p.27) "…West serial correlation adjustment." — i.e. specific risk estimation uses a Newey-West serial correlation adjustment.
- "The above approach is predicated on having a sufficient history of data. For assets with little or no history, e.g. IPOs, this is not the case. Therefore, the specific risk model includes a **cross-sectional overlay** which is used to infer missing specific risk forecasts based on (non-missing) forecasts for assets with a **similar market capitalisation, in the same industry and country**."
- "The final specific risk forecast for every asset is then formed as a **weighted sum** of its time-series forecast (if it exists) and its cross-sectional forecast. The weighting function places more weight on the time-series forecast as more data becomes available. In the limit this weight is set to 1 so that every asset eventually has a specific risk forecast based on the time-series estimate alone." — NOTE: the functional form of the weighting function is *not* given.
- Specific Return Correlation: "Linkages between related assets in the same company are not completely captured by the common factors in the model. In these instances, specific returns continue to capture both the idiosyncrasies of asset return and company return. As a result these specific returns may be positively correlated, and so ignoring this correlation would lead to under (or over) prediction of specific risk in a long-only (long-short) portfolio context."
- "Examples of such related assets include cross-listings of the same security; ADRs and their root assets; and different share classes, e.g. 'A' and 'B' shares in Sweden, and 'Registered' and 'Bearer' shares in Switzerland."
- "In all circumstances linkages can be captured through specific return correlations, either **imposed via a constant override of 1**, or where data availability permits, **estimated using asset specific returns**. Note that specific return correlations are only estimated between assets **in the same company**. Specific return correlations between assets in different companies are **assumed to be zero** in-line with standard modelling practice." — justification given is only "in-line with standard modelling practice".
- Structural & Empirical (verbatim, checked at 3× zoom): "The BFRE models use two different methodologies to construct the asset specific covariance matrix. These differ only in their treatment of related listings in the same company. **The first approach is referred to as the structural approach** and assigns related listings identical specific risk forecasts (typically cloned from the primary listing) and forces the specific return correlation to be 1. **In contrast, the second – empirical– approach** estimates these quantities separately using data specific to each asset, and so results in different specific risk forecasts and specific return correlations."
  - (The printed text really does read `– empirical–` with an unbalanced dash pair; reproduced as printed.)
- "These approaches impact the following related asset groups: (a) cross-listings and (b) derived securities (ADRs, GDRs, NVDRs & Certificates) and their root assets."
- "Note that specific risk forecasts and specific return correlations for different share classes, e.g. 'A' and 'B', ordinary and preference shares, are **still estimated empirically under the structural approach** as these lines confer different rights to the owner and are in no way fungible."
- "The model user is free to choose the approach that best applies to their investment process and horizon. The…" (sentence continues on p.29)

### Figures
None.

### Unreadable
- Nothing material. Re-checked Table 1.3 at 4× zoom: every cell is crisp and matches the transcription digit for digit (125 / 375 / 10 days; 26 / 104 / 2 weeks), header row shaded grey, four columns as printed.

---

## PDF page 29 (printed p. 29)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- No section headings printed on this page.

### Equations
None.

### Tables
None.

### Numbers
None stated in the legible text on this page.

### Terms
- structural approach, empirical approach, related listings, index tracking portfolios

### Claims / methodological choices
Single paragraph (completes the sentence begun at the foot of p.28):

> "…structural approach is typically used by **active portfolio managers** who view related listings as being entirely fungible over longer horizons, i.e. **many months**, whereas the **empirical approach** is typically more suited to **index tracking portfolios**, where even small differences in how related listings trade on a day-on-day basis can significantly impact their performance."

This is the whole of the page's own printed content; the "Model Assumptions & Limitations" section starts fresh on p.30.

### Figures
None.

### Unreadable
- p.29: The lower ~70% of the page carries a very faint block of text. After contrast enhancement (`enh_p029_a.png`, `enh_p029_b.png`) the visible line structure and the readable fragments ("Due to vendor limitations, certain equity assets… 1-2 day lag… Chinese MMA securities", "The forecast horizon of the model is 1-month…", "Model users are referred to [17]…") match **page 30**. Assessment: this is show-through / ghosting of the reverse of the leaf (page 30), not distinct page-29 content. (Stated more carefully than before: what is actually verifiable is that the bullet/indent structure and the legible fragments correspond to p.30's bullet list; "line for line" overstated it, since individual characters in the ghost are not readable.) It is *not* transcribed here as page-29 text. Individual characters within the ghost block are not reliably readable.

---

## PDF page 30 (printed p. 30)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **MODEL ASSUMPTIONS & LIMITATIONS** (large bold section heading)

### Equations
None.

### Tables
None.

### Numbers
- p.30: 1–2 day lag = the vendor-driven lag with which certain equity assets (e.g. Chinese MMA securities) enter the coverage universe
- p.30: 1-month = the model's forecast horizon
- p.30: 1-month = the horizon at which risk estimates are computed
- p.30: +/- 8% = truncation bound on **daily** currency factor returns prior to factor covariance estimation
- p.30: +/- 20% = truncation bound on **weekly** currency factor returns
- p.30: [17] = reference cited for more details on assumptions/limitations of fundamental multi-factor models

### Terms
- BRS' Covariance Matrix Estimation methodology
- Chinese MMA securities
- Dummy-variable exposures — the page assigns these to the **industry, country and currency** blocks only. **Style factors are explicitly not in that list**; styles are mentioned separately, as being *selected* by monthly cross-sectional explanatory power.
- Factor blocks named on this page: styles, industries, countries, currencies
- Royal Dutch Shell (named as the dual-listed special case)
- Quarterly Aladdin Risk Model conference calls

### Claims / methodological choices
Lead-in: "Model users should note the following assumptions and limitations of the BFRE risk models:"

- "All the standard assumptions of **BRS' Covariance Matrix Estimation methodology** apply"
- "Due to vendor limitations, certain equity assets are incorporated into the coverage universe with a minor **1-2 day lag**, e.g. Chinese MMA securities. This will be addressed in a forthcoming model release"
- "The forecast horizon of the model is **1-month**. This is reflected in different aspects of the model construction:"
  - "Style and industry factors are **selected by assessing explanatory power using monthly cross-sectional regressions**"
  - "Risk estimates are computed at a **1-month horizon** taking into account **daily serial correlations** in factor returns and asset specific returns"
  - "Model bias statistics are evaluated using **monthly standardised returns**"
- "Industry, country and currency factor exposures are assigned using **dummy variables**, e.g. all assets with exposure to the same industry factor receive the same risk from that exposure. **Heterogeneity in the industry block is captured via the granularity of the industry factors**"
- "The **currency factor exposures are always assigned based upon the country factor exposures**"
- "Currency factor returns are **truncated to remove outliers** prior to the estimation of the factor covariance matrix. Daily currency returns are bounded by **+/- 8%**, and weekly currency returns are bounded by **+/- 20%**"
- "Factor returns have **zero correlation with asset specific returns**, and specific returns from different issuers are unrelated and have **zero correlation**"
- "Specific return correlations are computed **relative to a representative, root asset**. Despite being a popular approach in industry, this model **does not adequately capture all relationships between different listings of companies, which have more than one share class with derived securities linked to those share classes**, e.g. Chinese MMA securities. This will be addressed in a forthcoming model release"
- "**Dual-listed companies share the same fundamental data for both sister companies**, and therefore have identical fundamental, style factor exposures. This treatment also extends to **Royal Dutch Shell** which retains aspects of the dual-listed structure after its unification"
- "The model should be used with care on portfolios covering assets not well represented in the estimation universe. **Out-of-sample model back-testing is conducted on a subset of such portfolios** as part of the **Quarterly Aladdin Risk Model conference calls**"
- Closing (unbulleted): "Model users are referred to **[17]** for more details on the assumptions and limitations of fundamental multi-factor models."

### Figures
None.

### Unreadable
- Nothing material; all bullets legible after zoom. The `+/- 8%` (daily) and `+/- 20%` (weekly) currency-return truncation bounds were re-verified independently at 4× on the raw scan — both are unambiguous, as is the `1-2 day lag`.

---

## PDF page 31 (printed p. 31)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **Model Data & Inputs** (large chapter-style heading)
- Lead-in line: "This section describes the input data used by the BFRE risk models."

### Equations
None.

### Tables

**Unnumbered table (no "Table 1.x" caption printed)** — 4 columns × 8 item rows. Header row is dark/reversed. Note: cell boundaries in the "Preparation & Quality Control" and "Limitations" columns are staggered relative to the item rows, so some QC/limitation cells straddle two items; transcription preserves the printed layout as closely as possible.

| Item Description | Data Source(s) | Preparation & Quality Control | Limitations |
|---|---|---|---|
| Company Fundamentals | Worldscope\* | Rolling 12-month ('RTM') logic applied to choose between annual, semi-annual and quarterly items — *and* — Large differences reviewed in Data QC | Fundamental price ratios are normalized by WS prices |
| Analyst Estimates | I/B/E/S\* | Large differences reviewed in Data QC — *and* — Roll-forward logic applied to stale/illiquid assets | (blank) |
| Market Data (e.g. returns, volumes) | Datastream | Returns reviewed as part of Data QC\*\*\*\* | Limited coverage; in-house logic applied as an alternative |
| Company Market Capitalisation | Datastream | (cell spans from the row above / blank) | Current: overrides applied to expand coverage |
| Industry Classifications | Current: Thomson Reuters Business Classifications ('TRBC'), and FTSE Russell Industry Classification Benchmark ('ICB')\*\* ; Historical\*\*\*: MSCI S&P Global Industry Classification Schema ('GICS') | Cloning logic applied to ensure consistency across all listings within the same issuer | Historical\*\*\*: overrides applied to separate composite assets into multi-sector sub-industry, and expand coverage |
| Asset Coverage / Universe | Bloomberg Equity BulkFeed & Datastream Equity | Coverage universe restricted to assets with sufficient market data | Securities on the same exchange with different traded currencies, e.g. Chinese MMA securities |
| Country Classifications | Preferred: Worldscope ; Fall-back: Datastream | Proxies applied to small jurisdictions, e.g. Panama -> USA | Overrides applied on an ad-hoc basis |
| FX / Risk Free Rate | Reuters | Large differences reviewed in Data QC | (blank) |

Table footnotes (printed directly under the table):
- `*` via Thomson Quantitative Analytics ('TQA')
- `**` BFRE UK model only
- `***` before February 2018
- `****` IDC and Bloomberg market data are used as secondary source for Data QC

### Numbers
- p.31: Rolling **12-month** ('RTM') logic — used to choose between annual, semi-annual and quarterly fundamental items
- p.31: **February 2018** — the cut-off date before which GICS was the historical industry classification source

### Terms
- Worldscope (WS); I/B/E/S; Datastream; Bloomberg Equity BulkFeed; Datastream Equity; Reuters; IDC
- Thomson Quantitative Analytics ('TQA')
- Thomson Reuters Business Classifications ('TRBC')
- FTSE Russell Industry Classification Benchmark ('ICB')
- MSCI S&P Global Industry Classification Schema ('GICS')
- RTM = Rolling 12-month
- Data QC
- Chinese MMA securities
- Item categories: Company Fundamentals, Analyst Estimates, Market Data, Company Market Capitalisation, Industry Classifications, Asset Coverage / Universe, Country Classifications, FX / Risk Free Rate

### Claims / methodological choices
- Industry classification source switched: **GICS historically (before February 2018)**, **TRBC currently**, with **ICB used for the BFRE UK model only**. No justification for the switch is given on this page.
- Country classification uses **Worldscope preferred, Datastream as fall-back**, with **proxies applied to small jurisdictions (e.g. Panama → USA)**. No criteria for "small jurisdiction" are given.
- **Cloning logic** applied to industry classifications to force consistency across all listings within the same issuer.
- Coverage universe is **restricted to assets with sufficient market data** — "sufficient" is not quantified.
- Fundamental price ratios are **normalized by Worldscope prices**.
- **Roll-forward logic** applied to stale/illiquid analyst estimates.

### Figures
None.

### Unreadable
- p.31: Re-checked the whole table at 4× in three overlapping bands. **All cell text is legible and matches the transcription above**, including the four footnote lines. What remains uncertain is only row *alignment*, and less of it than first reported:
  - **Resolved at zoom (no longer ambiguous):** "Current: overrides applied to expand coverage" sits opposite **Company Market Capitalisation**, and "Historical\*\*\*: overrides applied to separate composite assets into multi-sector sub-industry, and expand coverage" sits opposite **Industry Classifications** — the ruled line between them lines up with the Item-Description row break. "Limited coverage; in-house logic applied as an alternative" sits opposite **Market Data**.
  - **Still genuinely straddling:** the two separate "Large differences reviewed in Data QC" cells (one belongs with Company Fundamentals, one with Analyst Estimates — the second is drawn *above* the Analyst Estimates row line); "Securities on the same exchange with different traded currencies, e.g. Chinese MMA securities" (drawn across the Industry Classifications / Asset Coverage break, assigned to Asset Coverage on sense); "Overrides applied on an ad-hoc basis" (drawn across the Asset Coverage / Country Classifications break, assigned to Country Classifications on sense); and the final "Large differences reviewed in Data QC" (assigned to FX / Risk Free Rate).
- p.31: Two "Limitations" cells (opposite Analyst Estimates and FX / Risk Free Rate) are genuinely empty at 4× — no faint content.
- p.31: Faint ghost text is visible in the lower half of the page (below the table). It is show-through from p.32 and is not legible.

---

## PDF page 32 (printed p. 32)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **Model Testing** (large chapter-style heading)
- **MODEL ESTIMATION DIAGNOSTICS** (bold section heading)
- **ASSESSMENT OF VOLATILITY FORECASTS** (bold section heading)

### Equations
- p.32: `R^2` — the coefficient of determination, defined in words as "the proportion of cross-sectional variation in asset returns explained by the set of common factors in the model". Printed as an italic *R²* inline; no displayed formula is given.
- No other mathematics on the page.

### Tables
None.

### Numbers
- p.32: **1996 to 2013** = span of the data history over which all models were tested ("several different market environments")
- p.32: **10%** = threshold proportion of significant t-statistics; "the majority of factors are significant more than 10% of time over the research history, with most well in excess of this threshold"
- p.32: footnote marker **16**

### Terms
- R² (overall explanatory power)
- t-statistics / individual factor efficacy / persistence of individual factor effects
- Variance inflation factors (VIFs) — multicollinearity diagnostic
- Bias statistic
- Pure factor portfolios
- Market capitalisation-weighted estimation universes; industry and country based carve-outs
- Market capitalisation-weighted terciles: large-cap, mid-cap, small-cap segments
- Common factor blocks listed: markets, styles, industries, countries and currencies

### Claims / methodological choices
- "All models were tested extensively using a history of data spanning several different market environments from **1996 to 2013**. The section below provides a brief overview of the various diagnostics and backtests performed on the BFRE models prior to their release."
- MODEL ESTIMATION DIAGNOSTICS: "**The model estimation is a core component of the model construction process.** Several standard diagnostics were appraised during this process to check the overall explanatory power of the models, individual factor efficacy and also multicollinearity:" — the opening sentence is what "this process" refers back to.
  - "The *R²* quantifies the proportion of cross-sectional variation in asset returns explained by the set of common factors in the model. This is a standard measure of any factor model's overall explanatory power"
  - "Individual factor efficacy is assessed using a history of t-statistics for each common factor by calculating the proportion of significant t-statistics over different periods. This metric serves as a good proxy for the persistence of individual factor effects. **The majority of factors are significant more than 10% of time over the research history, with most well in excess of this threshold**"
  - "The final set of diagnostics are **variance inflation factors**. These help diagnose issues relating to multicollinearity between the style factors. If style exposures are too closely correlated then the regression procedure will encounter problems in apportioning the factor return between them. This can result in significant instability in the factor return estimates through time¹⁶. In order to guard against these effects, variance inflation factors were reviewed over the research history and **were found to be well within suitable thresholds**" — NOTE: no numeric VIF values or thresholds are reported.
- Footnote 16: "In the most extreme case, where factor exposures are perfectly correlated, identification issues will exist causing the estimation process to fail"
- ASSESSMENT OF VOLATILITY FORECASTS: "A well-calibrated model should provide risk forecasts that are stable and accurate. One way of testing the accuracy of the risk forecasts is to compare the volatility of realised returns to forecast risks. This forms the basis of the **bias statistic** used to evaluate the BFRE models."
- "An exhaustive set of bias statistics was generated and reviewed over the entire research history. The tests themselves were conducted using an exhaustive set of portfolios:" (list continues onto p.33)
  - "Pure factor portfolios for all common factors: markets, styles, industries, countries and currencies,"
  - "Market capitalisation-weighted estimation universes, and their industry and country based carve-outs,"
  - "Market capitalisation-weighted terciles of the estimation universe into large-cap, mid-cap and small-cap segments,"

### Figures
None.

### Unreadable
- Nothing material; the page is legible throughout, including the footnote. "1996 to 2013" and "more than 10% of time" were both re-verified at 4× and are unambiguous.

---

## PDF page 33 (printed p. 33)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- No new section headings printed on this page (continuation of ASSESSMENT OF VOLATILITY FORECASTS from p.32).

### Equations
None.

### Tables
None.

### Numbers
- p.33: **[27]** = reference cited for more details of the testing, "available on request"

### Terms
- Minimum variance portfolios
- Active portfolios
- Estimation universe / individual stocks

### Claims / methodological choices
Completion of the p.32 bullet list of test portfolios:
- "Individual stocks in the estimation universe,"
- "Minimum variance portfolios, and"
- "Active portfolios"

Closing paragraph:
> "Furthermore, the final suite of test statistics included a significant number of **genuine portfolios** covering different geographical areas and market segments. More details of the testing are provided by **[27] available on request**."

NOTE (methodological gap): no bias-statistic values, no pass/fail criteria and no summary results are printed anywhere in the Model Testing chapter — the reader is referred to an unpublished document available on request.

### Figures
None.

### Unreadable
- p.33: Below the closing paragraph, roughly the bottom two-thirds of the page carries a faint ghost block of text. After enhancement (`enh_p033_a.png`, `enh_p033_b.png`, `enh_p033_c.png`) the readable fragments and paragraph structure match **page 34** (paragraph block structure and heading positions; not character-level — "Top-line risk numbers are shown along the top of the report…", "For each factor block, there is a corresponding bar chart…", "MODEL PRODUCTION PROCESS & QUALITY CONTROLS", "PROXYING IN ALADDIN"-adjacent headings). Assessment: show-through from p.34, not page-33 content. Individual characters in the ghost are not reliably readable.

---

## PDF page 34 (printed p. 34)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **Model Outputs and Use** (large chapter-style heading)
- **BFRE MODELS IN ALADDIN** (bold section heading)
- **MODEL PRODUCTION PROCESS & QUALITY CONTROLS** (bold section heading)

### Equations
None.

### Tables
None.

### Numbers
- p.34: **Figure 1.18** = the sample Equity Daily Risk (EDR) report referenced (reproduced on p.35)
- p.34: **flowchart 1.19** = the daily production process flowchart referenced
- p.34: footnote marker **17**

### Terms
- Aladdin tools providing BFRE-based analytics: **the Green Package, PRT, Portfolio Construction (PfC) and Prism**
- **Equity Daily Risk (EDR)** report
- **EMEA model** (used for the European Equity portfolio example)
- Top-line risk numbers: **Active Risk, Portfolio Beta, Portfolio Risk and Benchmark Risk**
- Factor blocks: **styles (including the market factor), industries, countries and currencies**
- Style tilts named in the example: **high volatility, momentum driven, low-yielding, smaller stocks**
- Data QC content: **Raw market data** (prices, shares and total returns); **Derived market data** (security-level market capitalisations, company-level market capitalisations and volumes)
- **Substyle standardization** process, **style factor aggregation** (cross-reference to the Style Factors section)

### Claims / methodological choices
- "There are several tools which provide access to BFRE-based analytics in Aladdin: the Green Package, PRT, Portfolio Construction (PfC) and Prism. To give an example, **Figure 1.18** shows an **Equity Daily Risk (EDR)** report for a European Equity portfolio using the **EMEA model**. This report was generated using PRT, and provides an extremely intuitive, graphical description of the active bets being taken in this portfolio."
- "Top-line risk numbers are shown along the top of the report: Active Risk, Portfolio Beta, Portfolio Risk and Benchmark Risk. **Active Risk is then decomposed along the different factor blocks in the model, shown in the pie chart: styles (including the market factor), industries, countries and currencies.** The report shows that the **Active Risk is split equally between common factors and stock specific sources**. Style and industry factors account for most of the common factor risks."
- "For each factor block, there is a corresponding bar chart (using a consistent colour) that shows the top contributing factors in that block – this displays the active exposure together with the contribution to active risk. For instance, within the style block (bottom-left), this portfolio has significant tilts towards **high volatility, momentum driven, low-yielding, smaller stocks**."
- "Information of this nature is extremely useful and can be fed back into the portfolio construction process and used to promote more informed discussions between portfolio managers and risk managers around the level and types of risks being taken in portfolios. The factor structure used in BFRE is particularly relevant here as using an intuitive, relevant set of factors that align with how portfolio managers structure their investment process promotes clearer understanding of portfolio risks, leading to more informed decision-making and better portfolio construction."
- MODEL PRODUCTION PROCESS & QUALITY CONTROLS: "The **flowchart 1.19** illustrates the daily production process for the model estimation. We retrieve data from various vendor sources¹⁷ and apply QC to ensure that all model inputs are cleaned and suitable for model usage. The data content covered in the **Data QC** procedure includes"
  - "Raw market data: prices, shares and total returns"
  - "Derived market data: security-level market capitalisations, company-level market capitalisations and volumes"
- "The procedure is **exception-based** and identifies missing returns and market capitalisations to ensure that all actively traded securities with non-zero trade volumes and prices have corresponding returns and market capitalisations. Additionally, the QC procedure validates securities with extreme returns and market capitalisations to ensure that any extreme values are accurate, and correctly reflect market events. Finally, missing values or changes in industry codes from our vendors are identified and investigated."
- "After the Data QC procedure, we proceed to the **substyle standardization** process which is then followed by **style factor aggregation**, as described in the Style Factors section. Once the factor exposures have been computed, the…" (continues on p.36)
- Footnote 17: "See the Model Data & Inputs section for more details"

### Figures
None on this page (Figure 1.18 is referenced here and printed on p.35).

### Unreadable
- Nothing material; page is legible throughout.

---

## PDF page 35 (printed p. 35)

**Orientation note:** this page is scanned upside-down — confirmed, not inferred: the running header banner sits at the *bottom* of the raw frame and reads mirrored ("(BFRE) SEITIUQE ROF …"). The figure itself is printed in landscape on the portrait page, so the figure sits at 270° in the raw scan. **Rotating the raw scan 90° counter-clockwise (`Image.rotate(90, expand=True)`) puts the figure upright**; rotating 180° instead puts the *page* upright with the figure on its side. All page-35 readings below were taken from the 90°-CCW view. Earlier working copies: `rot_p035.png` (180°), `r35_cw.png`.

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- Figure caption: *Figure 1.18. a sample Equity Daily Risk (EDR) report in Aladdin*

### Equations
None.

### Tables
None (the page is a single full-page figure).

### Numbers (all read from the reproduced EDR report banner and the pie chart)
- p.35: **Active Risk: 2.99%**
- p.35: **Portfolio Beta: 1.02**
- p.35: **Portfolio Risk: 15.62%**
- p.35: **Benchmark Risk: 14.98%**
- p.35: **Base Currency: EUR**
- p.35 (pie "Risk Contributions by Block"): **Specific 50%**, **Style 25%**, **Industry 14%**, **Country 6%**, **FX 4%**, **Act Sec 1%** `[INFERRED — the glyph reads 1 or 2; see Unreadable]`. The five directly-read values plus 1% sum to exactly 100%. Geometry corroborates the two largest: the Specific slice is drawn as the exact right half of the circle (12 → 6 o'clock) and the Style slice as the exact upper-left quadrant.
- p.35 axis ranges — Top Style Contributions: left axis "Contrib. (% of Act. Risk)" ticks at −5, 0, 5, 10, 15; right axis "Exposure (Std. Devs)" ticks at −0.4, −0.3, −0.2, −0.1, 0.0, 0.1, 0.2, 0.3, 0.4
- p.35 axis ranges — Top Asset Contributions: left axis "Contribution (%)" ticks at 0, 2, 4, 6, 8; right axis "Exposure (% of NAV)" ticks at −3, −2, −1, 0, 1, 2, 3
- p.35 axis ranges — Top Industry Contributions: left axis "Contrib. (% of Act. Risk)" ticks at 0, 1, 2, 3, 4; right axis "Exposure (% of NAV)" ticks at −6, −4, −2, 0, 2, 4
- p.35 axis ranges — Top Country Contributions: left axis "Contrib. (% of Act. Risk)" ticks at 0, 1, 2, 3; right axis "Exposure (% of NAV)" ticks at −15, −10, −5, 0, 5
- p.35 axis ranges — Top & Bottom FX Contributions: left axis "Contrib. (% of Act. Risk)" ticks at −1, 0, 1, 2, 3; right axis "Exposure (% of NAV)" ticks at −15, −10, −5, 0, 5, 10

### Terms
- Panel titles: **Risk Contributions by Block** (pie); **Top Asset Contributions**; **Top & Bottom FX Contributions**; **Top Style Contributions**; **Top Industry Contributions**; **Top Country Contributions**
- Legend series: **Contrib. to Act. Risk** (bar), **Contrib. to Spec. Risk** (bar, Top Asset Contributions panel only), **Act. Exp.** (dot marker)
- Pie slice labels: Specific, Style, Industry, Country, FX, Act Sec
- **Style categories (Top Style Contributions, left→right) — RECOVERED, ten factors:** **Volatility, Momentum, Size, Yield, Reversal, Emerging, Sentiment, Growth, Market, Profitability.** (Read after deskewing the 45° label strip; all ten resolved cleanly. Note "Market" appears here as a style-block member, matching p.34's "styles (including the market factor)".)
- Country categories (Top Country Contributions, left→right): **United Kingdom, Poland, Switzerland, Portugal, France, Sweden, Finland, Netherlands, Spain, Germany** — all ten confirmed after deskew.
- Industry categories (Top Industry Contributions, left→right): **Integrated Oil, Airlines, Media, Food Household, HR & Employment, Diversified Fin[…], Biotechnology, Chemicals - Agr[…], Software & Serv[…], Trading Compan[ies]** — after deskew. The 4th reads "Food Household"; whether a connector ("&", "/", ",") sits between the two words is not resolvable. Items 6, 8, 9, 10 are truncated by the chart itself, not by the scan.
- FX pair categories (Top & Bottom FX Contributions, left→right): the **`/USD`** quote suffix is unambiguous on all five. The three-letter base codes read as **EUR/USD, GBP/USD, CHF/USD, DKK/USD, SEK/USD** but these are **best readings, not confirmed** — at this resolution each base code is a 3-glyph blob. Treat as `[TENTATIVE]`. (They are consistent with the portfolio's EUR base currency and its UK/Swiss/Nordic country exposures, which is corroboration, not evidence.)

### Claims / methodological choices
The figure is presented purely as an illustration of model output; no methodological statements are printed on the page beyond the caption. Two independent cross-checks against p.34's prose both hold:
- The pie corroborates "Active Risk is split equally between common factors and stock specific sources": common-factor slices 25 + 14 + 6 + 4 + 1 = 50%, Specific = 50%. It also corroborates "Style and industry factors account for most of the common factor risks" (25 + 14 = 39 of the 50 common-factor points).
- With the style labels now recovered, the style panel corroborates "significant tilts towards high volatility, momentum driven, low-yielding, smaller stocks" factor by factor: Volatility ≈ +0.42 sd and Momentum ≈ +0.38 sd (long), Yield ≈ −0.30 sd and Size ≈ −0.20 sd (short). Nothing in the figure contradicts the text.

### Figures
**Figure 1.18 — a sample Equity Daily Risk (EDR) report in Aladdin.** Landscape, six panels in a 2×3 arrangement beneath a banner of top-line statistics.

- Banner (top): Active Risk 2.99% | Portfolio Beta 1.02 | Portfolio Risk 15.62% | Benchmark Risk 14.98%, with "Base Currency: EUR" at far right.
- **Panel 1 (top-left) — "Risk Contributions by Block":** pie chart. Specific 50% is the single largest slice (drawn as the exact right half); Style 25% (upper-left quadrant); then Industry 14%, Country 6%, FX 4%, Act Sec 1%. The scan is effectively monochrome here — the slices are separated by hairlines rather than by distinguishable fills, except for one light sliver at about the 6-o'clock position corresponding to the FX / Act Sec pair. Slice-to-label mapping is by leader line and by the geometry above, not by colour.
- **Panel 2 (top-centre) — "Top Asset Contributions":** paired vertical bars for **exactly 15** named holdings (counted at 5×), sorted by descending contribution to active risk. Light bar = Contrib. to Act. Risk, dark bar = Contrib. to Spec. Risk, dot = Act. Exp. on the right-hand "Exposure (% of NAV)" axis. Shape: the light (active-risk) bar declines gently from ≈6.7% for the first name to ≈2% for the last; the dark (specific-risk) bar is sometimes above it (≈7.5% on the first name, and a spike to ≈5.3% at the 12th) and sometimes well below (≈0.5% at the 6th). Exposure dots run roughly **+1.3 to +3.0% of NAV**, with **one clear outlier at about −2% of NAV** (6th name) sitting below the plot area.
- **Panel 3 (top-right) — "Top & Bottom FX Contributions":** five bars, monotonically decreasing left to right: 1st ≈ +2.55% of active risk (exposure dot ≈ +9% of NAV), 2nd ≈ +0.55, 3rd ≈ +0.45 (dot ≈ +3.6% NAV), 4th ≈ +0.13 (dot ≈ +0.9% NAV), 5th ≈ −0.05 (dot ≈ −0.7% NAV). The 2nd pair's exposure dot is the outlier, sitting far below at roughly **−10% of NAV** — i.e. a large short in that currency alongside a positive risk contribution.
- **Panel 4 (bottom-left) — "Top Style Contributions":** the ten style factors named above. Bars decline steeply: Volatility ≈ 11% of active risk, Momentum ≈ 6, Size ≈ 3.5, Yield ≈ 3, Reversal ≈ 1, and Emerging through Profitability all ≈ 0. Exposure dots (right axis, Std. Devs), matched to the recovered labels: **Volatility ≈ +0.42, Momentum ≈ +0.38, Size ≈ −0.20, Yield ≈ −0.30, Reversal ≈ +0.17, Emerging ≈ −0.10, Sentiment/Growth/Profitability ≈ +0.05 to +0.06, Market ≈ 0.0.** This is a direct, independent confirmation of p.34's prose — long Volatility and Momentum, short Yield and Size = "high volatility, momentum driven, low-yielding, smaller stocks" — and it also shows two factors (Emerging, and the near-zero-contribution tail) carrying exposure without contributing risk.
- **Panel 5 (bottom-centre) — "Top Industry Contributions":** ten industries, bars declining from ≈3.05% of active risk (Integrated Oil) through Airlines ≈1.9 and Media ≈1.0 to ≈0.3% (Trading Compan[ies]). Exposure dots, matched to labels: **Integrated Oil ≈ −6% of NAV, Airlines ≈ +2.2, Media ≈ +4.5, Food Household ≈ −5.5, HR & Employment ≈ +2.0, Diversified Fin ≈ +4.3, Biotechnology ≈ +4.3, Chemicals - Agr ≈ −3.0, Software & Serv ≈ +3.9, Trading Compan ≈ +3.8.** So there are **three** negative industry exposures, at positions 1, 4 and 8.
  - *(Correction to an earlier reading of this panel: the second large negative dot belongs to **Food Household** (4th), not to Media. Media's dot is clearly positive at ≈ +4.5% of NAV — it is the third-highest positive exposure in the panel.)*
- **Panel 6 (bottom-right) — "Top Country Contributions":** ten countries, bars declining from ≈2.4% of active risk (United Kingdom) through Poland ≈0.85, Switzerland ≈0.7, Portugal ≈0.7, then France ≈0.15 and a flat tail to ≈0.03 (Germany). United Kingdom carries a large negative active exposure of roughly **−10% of NAV** (its dot sits below the plot area); the remaining exposures cluster between about −2 and +5% of NAV, with Poland ≈ +4.7 and Switzerland ≈ +5.0 the largest positives.

### Unreadable
- p.35: ~~All ten style labels are illegible~~ — **withdrawn; this was wrong.** All ten *are* recoverable, and are listed under Terms above (Volatility … Profitability). The earlier attempt failed because the labels were read at 45°; deskewing the label strip by −45° after upscaling makes them plainly legible. Same technique recovered the country and industry labels.
- p.35: **Asset names in "Top Asset Contributions" — 15 in order, with per-item confidence.** Positions 1–4 and 12–14 are solid; the rest are tentative or unrecoverable:
  1. Commerzbank — confident
  2. Ryanair Holdin[gs] — confident
  3. Ing Groep NV — confident
  4. Prosiebensat1 — confident
  5. Volkswagen — `[TENTATIVE]`
  6. Royal Dutch Sh[ell] — confident (truncated by chart)
  7. Randstad Holdi[ng] — confident (truncated by chart)
  8. KBC Groep NV — `[TENTATIVE]` (first glyph could be K or V)
  9. Kingspan Group — confident
  10. Continental — confident
  11. `[UNREADABLE: renders roughly as "CN Sh--- Ra--"; not recoverable at this resolution]`
  12. Telecom Italia — confident
  13. Capgemini — confident
  14. Societe Generale — confident
  15. `[UNREADABLE: ends "… Ltd"; the preceding word renders roughly as "Ashtead"/"Amsterdam" but is not resolvable]`
- p.35: Banner figures re-verified at 9× on the 90°-CCW view: **Active Risk 2.99%**, **Portfolio Beta 1.02**, **Portfolio Risk 15.62%**, **Benchmark Risk 14.98%**, **Base Currency: EUR**. Residual doubt: the middle digit of "2.99" is blobby (2.89 not fully excluded) and the last digit of "15.62" is soft (15.67 not fully excluded). "14.98" and "1.02" are clean.
- p.35: Pie "Act Sec" slice label — the percent glyph is genuinely ambiguous between **1%** and **2%**, and on shape alone 2% is at least as good a reading. **1%** is recorded solely because the six slices then sum to exactly 100 (50 + 25 + 14 + 6 + 4 + 1). Treat as an inference from the arithmetic, not a reading. The other five pie values (Specific 50%, Style 25%, Industry 14%, Country 6%, FX 4%) are read directly and are unambiguous.
- p.35: No individual bar values are printed anywhere in the figure. **Every bar magnitude and every exposure-dot value quoted above is measured from pixel position against the printed axis ticks**, so treat all of them as ±10% of the stated figure, not as transcribed numbers. The axis tick *labels* themselves (listed under Numbers) are read directly and are reliable.

---

## PDF page 36 (printed p. 36)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- **PROXYING IN ALADDIN** (bold section heading)

### Equations
None.

### Tables
None printed on this page (a faint ghost of a table from p.37 is visible in the lower half; see Unreadable).

### Numbers
- p.36: **Figure 1.20** = referenced for the criteria securities must pass to be covered in the BFRE models
- p.36: **two** types of proxy available (unit proxy, sedol proxy)
- p.36: model universes / factor exposures / specific risk / specific return correlations updated **weekly on Thursday**, incorporating data as of **previous Wednesday market close**

### Terms
- **Thinness corrections** for country and industry factors
- **Bayesian prior** (thin country/industry correction)
- **Data QC** vs **Model QC** (two distinct processes)
- **Daily Model QC**
- **Unit proxy**; **sedol proxying**
- Security meta-data
- Model outputs checked: common factor volatilities, specific risk forecasts, specific return correlations

### Claims / methodological choices
- (continuing from p.34) "…process of factor return estimation commences. The estimation procedure uses **thinness corrections for country and industry factors** where limited, or no data exists to reliably estimate those factor returns."
- "We impose the thin country/industry correction by **adding a Bayesian prior**, which in essence diverts the estimated country/industry return away from the sample factor return and towards a **theoretical prior**. In its purest sense this can be understood as capturing a true country/industry return rather than asset-specific returns. Estimated factor returns and specific returns are then used to compute a factor covariance matrix, and specific risk forecasts, respectively." — NOTE: the prior's form, strength and shrinkage parameter are **not** specified anywhere on this page.
- "Prior to the models being released to Aladdin clients, the research team conducts a **daily Model QC process** that checks the quality of the model outputs. This is a separate process to the **Data QC** which is used to sanitise the raw inputs to the models. Instead, the Model QC process focuses on appraising"
  - "the turnover in membership of the standardisation and estimation universes"
  - "changes in factor exposures"
  - "model estimation diagnostics and"
  - "risk outputs: common factor volatilities, specific risk forecasts and specific return correlations"
- "**Daily Model QC** comprises all checks that are performed on a **dailybasis** [*sic* — printed as one word in the source] to ensure that the models correctly reflect updates to factor returns, factor covariance matrices and incorporate new listings. The **model universes, factor exposures, specific risk and specific return correlations are updated on a weekly basis on Thursday to incorporate the data as of previous Wednesday market close**, which necessitates additional checks on these items beyond those covered in the Daily Model QC." (Whole passage re-verified at 4×; the Thursday / previous-Wednesday pairing is unambiguous.)
- PROXYING IN ALADDIN: "As described in **Figure 1.20**, securities need to pass several criteria to be covered in the BFRE models. For securities not covered by the model, there are **two types of proxy** available depending on the availability of security meta-data. Typically, for a security with country and/or industry information, we apply a **unit proxy** that calculates a security's factor exposures using the **average value from those in the same country and/or industry**. For a security with no such data, **sedol proxying** may be applied to map the security to another one with the same issuer."

### Figures
None printed on this page; Figure 1.20 is referenced and presumably appears on p.37.

### Unreadable
- p.36: The lower third of the page (below the PROXYING IN ALADDIN paragraph) shows a faint ghost of a **table-like grid with ~4 rows of two-column text plus three shaded boxes at the bottom** — show-through from p.37. None of its text is legible in this scan; it is not page-36 content.
