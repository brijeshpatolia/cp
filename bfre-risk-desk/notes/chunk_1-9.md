# BFRE Transcription — PDF pages 1-9

Source images: /tmp/claude-0/-home-user-cp/79206b60-659d-5f16-a034-7d8ab14cc34a/scratchpad/img/p001.jpg .. p009.jpg
Running header on every page from p2 onward: "BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)". Footer on every page from p2 onward: "aladdin by BlackRock" (logo, left) and "Page N" (right).

**Audit status:** every page re-checked digit-by-digit against the source images. All numbers (TOC page numbers, beta 0.99 / R2 91%, 87 countries, March 1996, 15-year history, five-year sub-samples, |t| > 2, both figure axis ranges), both typeset equations (1.1)-(1.2), the six-row symbol table on p8, and all 18 rows of Table 1.1 verified correct as originally transcribed. Corrections applied were to over-firm paraphrase (notably p9 "typically" equal weighted), unflagged eyeball readings of the two figures, and omitted source sentences — now added inline. Photos are phone captures ("Galaxy Z Flip7" watermark, pp. 4-9); pp. 4-6 are skewed but legible.

---

## PDF page 1 (printed: no page number in footer — title/contents page)

### Headings
- Title: **BlackRock Fundamental Risk for Equities (BFRE)**
- **Contents**

### Tables
Table of contents (2 columns: section title, page number):

| Section | Title | Page |
|---|---|---|
| 1.1 | Introduction | 2 |
| 1.2 | Executive Summary | 3 |
| 1.3 | Methodology | 4 |
| 1.3.1 | Model Structure | 4 |
| 1.3.2 | Model Estimation | 24 |
| 1.3.3 | Model Assumptions & Limitations | 30 |
| 1.4 | Model Data & Inputs | 31 |
| 1.5 | Model Testing | 32 |
| 1.5.1 | Model Estimation Diagnostics | 32 |
| 1.5.2 | Assessment of Volatility Forecasts | 32 |
| 1.6 | Model Outputs and Use | 34 |
| 1.6.1 | BFRE Models in Aladdin | 34 |
| 1.6.2 | Model Production Process & Quality Controls | 34 |
| 1.6.3 | Proxying in Aladdin | 36 |
| 1.7 | Model Surveillance | 38 |
| 1.8 | Appendices | 39 |
| 1.8.1 | Style factor exposure construction | 39 |
| 1.8.2 | Style definitions | 40 |
| 1.8.3 | Substyle definitions | 42 |
| 1.8.4 | Inventory of all substyles investigated | 55 |
| 1.8.5 | Industry Schemas | 57 |

### Equations
None.

### Numbers
- All TOC page numbers as above (2, 3, 4, 4, 24, 30, 31, 32, 32, 32, 34, 34, 34, 36, 38, 39, 39, 40, 42, 55, 57).
- Document body therefore runs to at least printed page 57+.

### Terms
- BFRE = BlackRock Fundamental Risk for Equities.

### Claims / structure
- Document structure signals: Model Structure is by far the longest subsection (pp. 4-23); Model Estimation pp. 24-29; Assumptions & Limitations only ~1 page (p. 30); Model Data & Inputs 1 page (p. 31); Model Testing pp. 32-33 (Estimation Diagnostics and Assessment of Volatility Forecasts both start on p. 32); appendices pp. 39-end.

### Figures
None.

### Unreadable
None on this page.

---

## PDF page 2 (printed p.2)

### Headings
- **Introduction**

### Equations
None.

### Tables
None.

### Numbers
- "five regional models" (North America; Europe, Middle East & Africa; Asia Pacific excluding Japan; Latin America & Caribbean; Emerging Markets).
- "five country models" (Japan; United Kingdom; Australia; Canada; United States).
- "a World model covering the superset of all assets in the regional and country models" (1 World model).
- Reference "[1]" = Rosenberg.

### Terms
- BFRE, "pronounced B-Free".
- BRS = BlackRock Solutions.
- STORM = Aladdin's Security Total Return Methodology (Aladdin's existing equity risk approach; asset-by-asset covariance matrix estimated from asset returns alone, each asset effectively its own factor).
- Aladdin applications named: Portfolio Risk Tools (PRT), Portfolio Construction (PfC), Prism, the Green Package.

### Claims / methodological choices
- Purpose: describe the structure and sources of equity portfolio risk globally.
- Distinguishing feature: use of **company fundamentals in addition to historical market data**, vs. models relying solely on historical stock returns.
- Justification given for fundamentals: return-only forecasts "can quickly become misleading if a company undergoes changes in its operating activities, or is subject to corporate actions, or experiences changes to its capital structure"; such changes are "immediately reflected" by a fundamental model but "only gradually" incorporated by a returns-only model.
- Lineage: "draws on the pioneering work of Rosenberg [1] and the related literature", combined with "lessons learned over several decades of academic research" and "new insights from investment and risk professionals at BlackRock and BlackRock Solutions (BRS)".
- Factor characteristics are based on: balance sheet variables, income statements, analyst estimates, country and industry of business, and historical market data.
- Stated advantage: risk decomposition using an intuitive set of fundamental factors that "align with how portfolio managers structure their investments".
- BFRE positioned as "an alternative and entirely complementary methodology" to STORM; BFRE "imposes far more structure on the asset covariance matrix, reducing the modelling problem to a smaller set of factors, which capture the most important sources of asset return commonality", reframing risk forecasting into (a) deciding what factors influence cross-sectional equity returns and (b) "then deciding how best to forecast the risk of these common structural sources".
- BFRE models described as "factor-based models that can be used to decompose portfolio risk into a series of factors based on technical and fundamental characteristics"; many of those characteristics "are similar to those used by portfolio managers and financial analysts to form investment views on the future performance of companies".
- Framing sentence on the long lineage: "There is a long history of using fundamental information to forecast portfolio risk in this manner."

### Figures
None.

### Unreadable
None.

---

## PDF page 3 (printed p.3)

### Headings
- **Executive Summary**

### Equations
None.

### Tables
None (bulleted list only).

### Full bullet content
- BFRE is a suite of fundamental equity risk models, currently five regional models (North America; Europe, Middle East & Africa; Asia Pacific excluding Japan; Latin America & Caribbean; Emerging Markets), five country models (Japan; United Kingdom; Australia; Canada; United States), and a World model covering the superset of all assets in the regional and country models.
- Asset coverage for **87 countries** spanning all major exchanges and equity asset types: common shares, ordinary shares, preference shares, ADRs, GDRs, certificates, investment trusts and closed-end funds.
- Model structure includes: a market factor, style factors, industry factors, country factors and currency factors; style and industry factors "vary somewhat by region reflecting local variation in the importance of different factors".
- Industry factors derived from third-party industry classification schemas (footnote 1), and "reflect statistical significance as well as forward-looking views from investment professionals".
- Style factors based on well-known and long established investment trends, e.g. value, growth, large-cap vs. small-cap, and pervasive macro-economic themes, e.g. oil price dynamics, emerging markets vs. developed markets.
- Model estimation is performed in cross-section **"in two-passes"** (hyphenated in the original), "with precedence on more representative assets in countries and industries with higher development status and better data coverage and quality".
- Factor covariance matrices are constructed using a **daily** time-series of factor returns "correcting for serial correlations".
- Specific risk forecasts are based on a time-series of **daily asset-level specific returns**.
- Specific return correlations capture linkages between specific risks of related assets in the same company, e.g. between ordinary shares and preference shares. [Source text reads "preferences shares" — typo is in the original.]
- Update cadence: **monthly** updates to model estimation universes; **weekly** updates to factor exposures and specific risk forecasts; **daily** updates to model coverage universes (to reflect corporate actions) and factor covariance matrices; daily factor returns for all models **from March 1996 onwards**.

### Footnote
- 1: "ICB for the UKIN model, TRBC for all other models."

### Numbers
- 87 countries of asset coverage.
- 5 regional + 5 country + 1 World model.
- Two-pass cross-sectional estimation.
- Factor return history start: March 1996.

### Terms
- Asset types covered: common shares, ordinary shares, preference shares, ADRs, GDRs, certificates, investment trusts, closed-end funds.
- Factor blocks: market, style, industry, country, currency.
- ICB (Industry Classification Benchmark) — used for the UKIN model.
- TRBC (Thomson Reuters Business Classification) — used for all other models.
- Model code seen: UKIN (United Kingdom model).

### Figures
None.

### Unreadable
None.

---

## PDF page 4 (printed p.4)

### Headings
- **Methodology**
- **MODEL STRUCTURE**
- **Market factor**

### Factor-selection criteria (all four, verbatim labels)
- **Interpretability**: factors should be easily interpretable, and have a strong economic rationale.
- **Explanatory Power**: factors should explain the covariance structure of stock returns.
- **Consistency**: factors should be significant through time across different market regimes.
- **Efficacy**: factors should improve forecasts of portfolio beta and portfolio risk, and explain portfolio performance in factor-based attribution.

### Equations
No typeset equations on this page. One **handwritten annotation equation** in the margin/footer (reader's pen, not printed text):

- beta_{p,b} = (X_p^T F X_b) / (X_b^T F X_b)
  - X_p = Portfolio factor exposures
  - X_b = Benchmark factor exposures ("Benchmark " " " in the handwriting, i.e. benchmark factor exposures)
  - F = factor covariance matrix
- Second handwritten annotation (top right of body text): "Market factor exp =/= beta" (market factor exposure is not the same as beta).
- Handwritten underlining in the printed text under: "all equity assets have a unit exposure to this factor"; "cross-sectional average return across all assets in the model estimation"; "The market factor exposure represents the fraction of portfolio %NAV invested in equities"; "Portfolio beta to a market index can instead be computed via the risk factor exposures of the portfolio and market index, together with the factor covariance matrix".

### Tables
None.

### Numbers
- Regression of daily S&P 500 excess returns on daily NAMR market factor returns yields **beta = 0.99** with **R2 = 91%**.
- Five blocks of common factors: market factor, country factors, currency factors, industry factors, style factors.
- Footnote markers 2, 3, 4.

### Terms
- NAMR = North America model (used as the region in the S&P 500 regression example).
- %NAV = percent of net asset value.

### Claims / methodological choices
- Framing: "The identification of a relevant set of factors is a critical part of the model construction process of any factor-based approach." BFRE models "use common factors based on highly intuitive, technical and fundamental security characteristics". All common factors are selected on the four criteria below.
- "Each equity, and by extension, all portfolios that contain equities have exposures to these common factors."
- All BFRE models specified with a market factor; **all equity assets have a unit exposure** to it.
- Market factor return = the cross-sectional average return across all assets in the model estimation (footnote 2: "Average return based on regression weights, i.e. square-root of market capitalisation"); captures risk of general market movements.
- Market factor return is highly correlated but **not identical** to the return to "a comparable market index covering the same region"; the imperfect fit "is not expected to be a perfect fit as the NAMR market covers a broader universe of assets, including Canadian stocks, and uses square-root of market capitalisation weights, which assigns greater weight to the mid-cap and small-cap segments relative to large-cap stocks."
- Closing qualifier the digest previously omitted: "Nevertheless, both are expected to be highly correlated through time and exhibit similar levels of volatility."
- Explicit warning: "The market factor exposure of a portfolio should not be confused with its market beta." Market factor exposure = fraction of portfolio %NAV invested in equities (footnote 3: "and delta-adjusted market exposure for derivatives"). The BFRE model does **not** include a single explicit portfolio market beta exposure; beta to a market index is computed from factor exposures of the portfolio and index plus the factor covariance matrix.
- Justification for including a market factor: "leads to a cleaner separation and interpretation of market, industry and country effects, and is a standard approach adopted in the academic literature" (footnote 4: Heston and Rouwenhorst [2]); "especially useful in risk decomposition and factor attribution analysis and provides a better understanding of the contribution of different effects on portfolio risk and return."

### Footnotes
- 2: "Average return based on regression weights, i.e. square-root of market capitalisation"
- 3: "and delta-adjusted market exposure for derivatives"
- 4: "Heston and Rouwenhorst [2]"

### Figures
None (page ends mid-sentence leading into the Figure 1.1 example on p.5: "consider the performance of some ...").

### Unreadable
- The handwritten annotation "X_b = Benchmark " "" uses ditto marks; the intended words are almost certainly "factor exposure", but the handwriting itself is ditto marks — recorded as such.

---

## PDF page 5 (printed p.5)

### Headings
- **Country factors**
- Figure caption: *Figure 1.1. factor attribution of country indices in the EMEA model, 8 August 2011*

### Equations
None.

### Tables
None.

### Figures
**Figure 1.1** — clustered column chart (5 series drawn side-by-side from the zero baseline per country; **not** stacked), "factor attribution of country indices in the EMEA model, 8 August 2011".
- Legend (5 series): market return, specific return, style return, country return, industry return.
- Y axis label: "contribution to return"; ticks from **-7.0% to 3.0%** in **1.0%** increments (-7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0).
- X axis categories (19 country indices, in order): **AUT, BEL, CHE, DEU, DNK, ESP, FIN, FRA, GBR, GRC, HUN, IRL, ITA, NLD, NOR, POL, PRT, SWE, ZAF**.
- Qualitative shape: every country shows a large **negative market-return bar** of roughly uniform magnitude, plus smaller mixed positive/negative contributions from the other four blocks. The uniformity of the market bar is the point being made. [APPROX, read off gridlines only: market bars fall roughly in the -4.5% to -6.5% band, with AUT the deepest at roughly -6.5%; other-block bars roughly within +2% / -1%. No data labels are printed — treat every one of these as an eyeball estimate, not a transcribed value.]
- Exact per-bar values are not printed and cannot be read reliably from the scan — see Unreadable.

### Numbers
- Date of attribution: **8 August 2011** (following the US downgrade by Standard & Poor's).
- Contrast date: **16 August 2011** (Figure 1.2).
- Y-axis range -7.0% to 3.0%, 1% gridlines.
- 19 country indices plotted.
- Market factor exposure of a fully invested index = **1** ("all are fully invested and so have a market factor exposure of one").
- Footnote markers 5, 6.

### Terms
- EMEA model (Europe, Middle East & Africa).
- Country ISO codes listed above; text calls out Denmark (DNK), Poland (POL), Greece (GRC), Hungary (HUN).

### Claims / methodological choices
- On 8 Aug 2011 the largest contribution to return is from the market factor, which "captures the average (negative) return across stocks on this day"; magnitude uniform across indices because all are fully invested (unit market exposure).
- Sentence previously omitted: "Additionally, there are smaller, varying contributions from style, industry, country and specific returns; however, the dominant source of return is clearly due to a broad weakness across markets, which is captured by the market factor."
- Figure 1.1 "shows a factor attribution for each index giving the contribution to return from each factor block in the model" (footnote 6 attaches here; footnote 5 attaches to "European country indices").
- On 16 Aug 2011 (Fig 1.2) the market factor contribution is no longer the largest source of return, "reflecting a comparatively benign trading day across markets in EMEA"; in that instance large country index returns are largely attributed to the **country factor** (clearest for DNK and POL, and to a lesser extent GRC and HUN).
- Because country indices generally represent well-diversified portfolios, **specific returns are for the most part negligible**.
- **Country factors are only included in the specification of all regional models** (models spanning multiple countries). Single-country models such as Japan do **not** require a separate country factor "as this role is assumed by the Market factor".
- Country factor returns are estimated in a **multivariate regression together with other common factors**, and are therefore adjusted to be **neutral with respect to market, style and industry effects**. Justification: this separation disentangles related (and often correlated) effects, e.g. a country with a large concentration in a single industry, so users can understand country exposure and industry exposure in isolation.
- **Every asset is assigned a unit exposure to a single country factor at any point in time** (sentence continues onto p.6: "... at any point in time.").

### Footnotes
- 5: "Indices are market capitalisation weighted, country carve-outs of the EMEA estimation universe"
- 6: "No currency exposure is assumed"

### Unreadable
- Figure 1.1: individual bar heights / per-country per-factor contribution values. The chart has no data labels and the scan resolution does not permit reliable value reading beyond the qualitative bands described.

---

## PDF page 6 (printed p.6)

### Headings
- **Currency factors**
- Figure caption: *Figure 1.2. factor attribution of country indices in the EMEA model, 16 August 2011*

### Equations
None.

### Tables
None.

### Figures
**Figure 1.2** — same chart type as Figure 1.1 (clustered columns from the zero baseline, not stacked), "factor attribution of country indices in the EMEA model, 16 August 2011".
- Legend (5 series): market return, specific return, style return, country return, industry return.
- Y axis label: "contribution to return"; ticks from **-4.0% to 4.0%** in **1.0%** increments.
- X axis categories (same 19, same order): AUT, BEL, CHE, DEU, DNK, ESP, FIN, FRA, GBR, GRC, HUN, IRL, ITA, NLD, NOR, POL, PRT, SWE, ZAF.
- Qualitative shape: no uniform dominant market bar. Contributions are small and mixed, with four conspicuous outliers, which are the country-factor contributions the text points to. [APPROX, read off gridlines only — no data labels are printed: most bars within about +1.5% / -1.5%; POL large positive at roughly +3.5%; GRC large positive at roughly +2.8%; HUN large negative at roughly -3.0%; DNK negative at roughly -2.3%. Eyeball estimates, not transcribed values.]
- Exact per-bar values are not printed and cannot be read reliably — see Unreadable.

### Numbers
- Date: **16 August 2011**.
- Y-axis range -4.0% to 4.0%, 1% gridlines.
- Footnote markers 7, 8.
- Currency numeraire: **US dollars**.

### Terms
- Numeraire, rotation (change of base currency).
- Data sources named in footnote 7: **Worldscope** (country of business) and **Datastream** (country code).
- Example asset mapping named: Panama -> USA proxy country; German listing of AT&T in EMEA -> Germany country exposure.

### Claims / methodological choices
- Country factor exposures assigned based on a company's **country of business** (footnote 7: "Country exposures are primarily determined using a hierarchy of Worldscope country of business, and Datastream country code").
- Special case: if the country of business is a minor region or tax jurisdiction not significant enough for its own factor, it is **mapped to a proxy country** — e.g. assets in Panama are reclassified to a country exposure of USA.
- Model coverage universe includes all listings trading within a region, including listings of companies foreign to that region; foreign listings get a country exposure based on **country of listing** — e.g. the German listing of AT&T in EMEA is assigned a country exposure of Germany "(as there is no USA country factor)".
- Currency factors: models designed to be interpretable from any currency perspective. **"Each model includes a series of currency factors to handle currency risk."** **Non-currency factor returns (market, styles, industries, countries) are estimated from local asset returns in excess of the local risk free rate**, which ensures they are fully hedged from a currency perspective.
- Currency factor returns are **calculated** (not estimated) from daily exchange rates and risk-free rates — footnote 8: "Note the use of the term 'calculated' here, as opposed to 'estimated' — no uncertainty is involved in their construction."
- Returns "are expressed consistently with respect to a common numeraire, chosen to be US dollars. This choice can be changed by performing a simple rotation, for example, to the base currency of a non-US portfolio."
- Currency factor exposures assigned in accordance with the country factor exposure via a **one-to-one mapping between countries and their principal traded currency**; "Every asset is assigned a unit exposure to single currency factor at any point in time." (Source omits "a" before "single" — typo is in the original.)

### Footnotes
- 7: "Country exposures are primarily determined using a hierarchy of Worldscope country of business, and Datastream country code"
- 8: "Note the use of the term 'calculated' here, as opposed to 'estimated' — no uncertainty is involved in their construction"

### Unreadable
- Figure 1.2: individual bar heights / per-country per-factor contribution values (no data labels; scan resolution insufficient for reliable values). The named outliers above are approximate readings off gridlines and are flagged as such.

---

## PDF page 7 (printed p.7)

### Headings
- **Industry factors**

### Equations
Two-step cross-sectional regression, run for n = 1, 2, ... :

Equation (1.1):
  r = X_Mkt * f_Mkt + sum_{k in CCty} X_{CCty,k} * f_{CCty,k} + sum_{j in n-Ind} X_{n-Ind,j} * f_{n-Ind,j} + u

Equation (1.2):
  u = sum_{j in (n+1)-Ind} X_{(n+1)-Ind,j} * f_{(n+1)-Ind,j} + u_bar

(The page ends with the word "where"; the symbol definitions follow at the top of p.8.)

Symbol notes visible here:
- Subscript "Mkt" = market; "CCty" = core country; "n-Ind" = industry at Level n of the third-party schema; "(n+1)-Ind" = industry at Level n+1 (one level more granular).
- u = residual from the first-step regression; u_bar (u with an overbar) = residual from the second-step regression.

### Tables
None.

### Numbers
- "for n = 1, 2, ..." — the two-step regression is repeated over schema levels.
- Equation numbers (1.1) and (1.2).
- Reference numbers: Miller [3], Hocking [4], Thompson [5].
- "Level n + 1", "Level n" nesting relationship.

### Terms
- ICB and TRBC named as example third-party industry schemas.
- Schema level vocabulary: lowest / least granular level = sectors ("maps the whole market into a small number of sectors"); highest / most granular level = sub-industries ("maps to a large number of sub-industries").
- "Core country" (CCty) exposures.
- Frequentist stepwise regression.

### Claims / methodological choices
- All BFRE industry factors are derived from third-party industry schemas (e.g. ICB and TRBC) with a nested structure; industries at Level n+1 are sub-industries of some industry in Level n.
- Justification for third-party schemas: "widely accepted by market participants as an appropriate industry analysis framework for investment research and portfolio management, and as such, serve as a good starting point for the industry factor selection."
- Caveat stated: "Note that not all industries at the same level in an industry schema have equal explanatory power. In some cases individual sub-industries may be economically important and statistically significant, justifying their own category. In other cases, a sector view may be sufficient." Further research determines the appropriate sector cohort "whilst ensuring that each grouping contains a reasonable number of assets and represents a non-negligible proportion of market capitalisation."
- **Industry factors are defined and estimated globally across all countries in the estimation universe.** The only exception is the **Emerging Market model**, which uses **local industry definitions** for certain sectors.
- Local industry factors can be estimated at country- or regional-level, and capture differences in asset return dynamics within a given industry. "To maintain parsimony in the factor structure, local industry factors are only used in instances where there is a strong economic rationale for local effects, and this is supported by significant statistical evidence." Example given: "For example, this is an important consideration in the banking industry where locality specific regulations, fiscal and monetary policies give rise to greater heterogeneity in this group of assets. This is in contrast to developed markets, where there is more cohesion between regulatory bodies, and markets are more homogeneous."
- Industry factor selection determined **primarily using statistical criteria**; BFRE adopts a **frequentist stepwise regression approach**. "We refer the reader to Miller [3], Hocking [4] and Thompson [5] for detailed discussions on frequentist methods. These approaches suggest different heuristics in selecting factors with the most explanatory power from a large pool of candidate factors."
- Procedure: first run a cross-sectional regression of asset returns on the sectors at the **least granular level**; then regress the residuals of that model against the **next, more granular level** of the schema to compute the marginal benefit of increasing granularity.

### Figures
None.

### Unreadable
- Nothing material. Note: in eq. (1.2) the second-step residual is printed with an overbar (u-bar); the overbar is faint in the scan but legible.

---

## PDF page 8 (printed p.8)

### Headings
- (No new section heading; continuation of **Industry factors**. Page opens with the symbol-definition list for equations 1.1-1.2.)

### Equations / symbol definitions (the "where" list from p.7)
- r : Monthly local asset returns in excess of the risk-free rate
- X_Mkt, f_Mkt : Market exposures and factor returns
- X_{CCty,k}, f_{CCty,k} : Core country exposures and factor returns
- X_{n-Ind,j}, f_{n-Ind,j} : Third Party Industry Schema Level n industry exposures and factor returns
- u : Residual returns from the first step regression
- u_bar : Residual returns from the second step regression

(Note the frequency: **monthly** returns for these industry-selection regressions, in contrast to the daily returns used for factor covariance estimation per p.3.)

### Tables
The symbol/definition list is laid out as a two-column table without a caption or ruled borders (6 rows), transcribed above.

### Numbers
- Multivariate regressions performed **monthly** over the **15-year research history**.
- Results summarised over the **full sample period** as well as on **five-year sub-samples**.
- Individual factor efficacy "is assessed using a history of t-statistics".
- Statistical significance threshold: "We consider an absolute t-statistics in excess of **2** as statistically significant." (Source reads "an absolute t-statistics" — grammar error is in the original.)
- Also computed: the **average squared t-statistic**, computed specifically "to distinguish between factors with t-statistics close to +/- 2 and those that are significantly higher"; and — explicitly "to ensure that there are sufficient number of firms to calibrate a separate industry factor in our schema" — the **market capitalization weight** and the **effective number of assets** for each industry **at each level**.
- Reference numbers: Kadane and Lazar [6], Tibshirani [7], Efron [8], Yuan and Lin [9].

### Terms
- Eligibility criteria for an industry to enter the schema as a candidate factor: (a) a large proportion of significant t-statistics, (b) a high number of average squared t-statistics, (c) a large market capitalization weight, (d) a large effective number of assets.
- Cluster analysis / re-grouping decision.
- ESG = environmental, social and corporate governance.
- Industries called out as separated into their own factors in several BFRE models: **Alcohol, Tobacco, and Casinos & Gaming**.
- Alternative selection methods named: Bayesian approach (Kadane and Lazar [6]) using priors to force coefficients on irrelevant candidate factors to zero; penalized likelihood — **LASSO** (Tibshirani [7]), **LARS** (Efron [8]), **Group Lasso and Group LARS** (Yuan and Lin [9]), and **Ridge** techniques.

### Claims / methodological choices
- The proportion of significant t-statistics for each industry factor "serves as a good proxy for the persistence of individual factor effects."
- "A large proportion of significant t-statistics in the second step regression is viewed as evidence that the increased granularity improves the explanatory power of the model."
- Search direction: "We identify eligible factors by examining industries in the most granular level and work up the industry hierarchy to less granular levels."
- Where not all industries at a given level are considered candidate factors, a **re-grouping decision is required based upon cluster analysis**; cluster analysis uses return data as input and suggests a grouping strategy such that industries in the same group are more closely related to each other than to those in other groups.
- After a proposed industry schema is formed it is **peer reviewed by other investment and risk professionals at BlackRock** to ensure sensible groupings; these reviews are an opportunity "to impose forward-looking views of industry behaviour into the schema." Example justification: Alcohol, Tobacco and Casinos & Gaming split out "due to the increasing investor focus on environmental, social and corporate governance (ESG) issues."
- Stated contrast with the alternatives: LASSO/LARS/Ridge/Bayesian methods "are purely statistical in nature and rely heavily on historical data. In contrast, the BFRE industry factor selection methodology starts with a economically intuitive industry definition, and blends this with sophisticated statistical analysis as well as up-to-date market insights and forward-looking views of industry behaviour to determine an appropriate industry schema for each market."
- Note (analyst observation, not the paper's words): no numeric thresholds are given for "large proportion", "high number of average squared t-statistics", "large market capitalization weight", or "large effective number of assets" — the eligibility rule is stated qualitatively only.

### Figures
None.

### Unreadable
- Nothing material; the page is legible throughout. (Faint show-through from the reverse side is present but does not obscure text.)

---

## PDF page 9 (printed p.9)

### Headings
- **Style factors**
- Table caption: *Table 1.1. Style factor descriptions*

### Equations
None typeset. Structural statement (in prose): style exposures "are **typically** defined as an equal weighted combination of substyles, where each substyle reflects a different formulation of the style." Note the hedge "typically" — the source does **not** state equal weighting as an invariant rule. In plain-text form as described:
  Style_exposure = equal-weighted average of its substyle exposures (typical case)
Example begun on this page and cut off mid-sentence at the page break (continues on p.10): "As an example, a definition of size may use three different substyles: market capitalisation,"

### Tables
**Table 1.1. Style factor descriptions** — 2 columns (Style, Description), 18 data rows:

| Style | Description |
|---|---|
| Size | Company size based on market capitalisation & fundamental data |
| Volatility | Various measures of historical volatility & historical beta |
| Small-Cap | Small-cap adjustment to the (linear) size factor exposure |
| Mid-Cap | Mid-cap adjustment to the (linear) size factor exposure |
| Reversal | One month return capturing short-term overreaction |
| Momentum | Longer-term trend in stock prices over the last year |
| Liquidity | Various measures of trading activity & price impact |
| Value | Identifies cheap vs. expensive stocks relative to fundamentals |
| Earnings Yield | Earnings-to-price & related measures |
| Dividend Yield | Dividend-to-price |
| Profitability | Return on equity (ROE) & related measures |
| Growth | Historical growth in assets & sales |
| Leverage | Various measures of indebtedness |
| Quality | A measure of shareholder dilution |
| Foreign Sensitivity | Proportion of foreign assets and revenues |
| Emerging Market | Identifies developed market stocks with emerging market exposure |
| Oil | Sensitivity of stock return with changes to the oil price |
| Sentiment | Sensitivity of stock return with changes in the VIX index |

### Numbers
- 18 style factors listed in Table 1.1.
- Reversal defined over **one month**; Momentum over **the last year** (longer-term trend).
- Forward references: Table 1.2 (summary statistics for the market and style factors in the **NAMR** model) and Figure 1.3 (cross-sectional style factor exposure correlations for the NAMR model).
- Reference [1] = Rosenberg (seminal research).
- Example: "a definition of size may use **three** different substyles".

### Terms
- Named styles: Size, Volatility, Small-Cap, Mid-Cap, Reversal, Momentum, Liquidity, Value, Earnings Yield, Dividend Yield, Profitability, Growth, Leverage, Quality, Foreign Sensitivity, Emerging Market, Oil, Sentiment.
- Substyle (a different formulation of a style; styles are equal-weighted combinations of substyles).
- ROE = return on equity; VIX index (Sentiment).
- NAMR model referenced for Table 1.2 and Figure 1.3.

### Claims / methodological choices
- Style factors capture sources of asset return commonality **not captured by market, country and industry factors**.
- Two kinds of styles distinguished: (a) styles that are "well-known investment themes in the asset management industry" measuring exposure to firm attributes "such as value, growth and size" — useful because "a company's exposure to such attributes will capture the degree to which its return behaviour is influenced by economic and business cycle risks"; and (b) "In contrast, other style factors in the model take a more direct approach and measure exposure to economic risks using empirical analysis based on historical market data."
- Justification for inclusion: "substantial empirical evidence supporting the use of these style factors in multi-factor risk models of this form"; majority of BFRE style factors "feature in the seminal research of Rosenberg [1] and the related literature, and their continued inclusion in the models signify their continued relevance in explaining global and regional sources of equity risk through different market environments."
- Construction inputs: "Style factors are constructed from company fundamentals, analyst estimate data and historical market data."
- Construction rule: **typically** an equal weighted combination of substyles (no justification given on this page for equal weighting, and "typically" leaves room for exceptions — the digest previously stated this as an unqualified rule).
- Pointer sentence: "Table 1.1 provides a short description of each style factor, table 1.2 shows some summary statistics for the market and style factors in the NAMR model, and figure 1.3 shows the cross-sectional style factor exposure correlations for the NAMR model."

### Figures
None on this page (Figure 1.3 is referenced but appears later).

### Unreadable
- Nothing material; Table 1.1 is fully legible.
