# BFRE — transcription of PDF pages 46–55

Source images: `/tmp/claude-0/-home-user-cp/79206b60-659d-5f16-a034-7d8ab14cc34a/scratchpad/img/p046.jpg` … `p055.jpg`
Printed page numbers match the PDF page indices exactly (PDF p.46 = "Page 46", … PDF p.55 = "Page 55").
Every page carries the running header band "BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)" and the footer logo "aladdin by BLACKROCK" plus "Page NN".

**Scan artefact affecting every page in this range:** each page shows faint grey "ghost" text that is the *next* page's content bleeding through the paper (verified: the ghost on p.46 is exactly p.47's headings; the ghost on p.48 is p.49's; the ghost on p.49 is p.50's; etc.). Ghost content is NOT transcribed as belonging to the page it appears on.

---

## PDF page 46 (printed p.46)

### Headings
- (running header) BLACKROCK FUNDAMENTAL RISK FOR EQUITIES (BFRE)
- No new section heading on this page — the page is a continuation of a definition begun on p.45.

### Body text
Top (continuation line): "days the asset has not been trading as of time s"

### Equations
- (1.26)
  `delta_{i,s} = { 1, if r_{i,s-1} = 0 or v_{i,s-1} = 0 ; 0, otherwise }`
  Symbols: `delta_{i,s}` = non-trading / stale-data indicator for asset i at time s; `r_{i,s-1}` = return of asset i at s-1; `v_{i,s-1}` = (volume / traded-volume variable) of asset i at s-1 — the page itself does not re-define `v` here.
- (1.27)
  `r_{i,s,tau} = { r_{i,s},                                        if delta_{i,s} = 0 and delta_{i,s+1} = 0`
  `             { prod_{k=0}^{tau-1} (1 + r_{market,s-k}) - 1,      if delta_{i,s} != 0 or delta_{i,s+1} != 0`
  `             { 0,                                               if model country is on holiday`
  Symbols: `r_{i,s,tau}` = the return used for asset i at time s over horizon tau; `r_{market,s-k}` = market return at s-k; `tau` = number of periods being compounded (tied to the "days the asset has not been trading as of time s" phrase carried over from p.45).

### Tables
None.

### Numbers
- p.46: 1 and 0 — the two values `delta_{i,s}` can take (indicator variable).
- p.46: "-1" — the subtraction applied to the compounded market product in (1.27).
- p.46: k runs 0 … tau-1 in the product of (1.27).

### Terms
None newly named on this page (indicator `delta`, proxy return `r_{i,s,tau}`).

### Claims / methodological choices
- When an asset is non-trading (zero return or zero volume at s-1), or is about to be non-trading at s+1, its return is **replaced by the compounded market return** over the stale window, rather than being left as zero or dropped.
- Returns are set to exactly **0 when the model country is on holiday** (i.e. market-wide non-trading is treated differently from asset-specific non-trading).
- No justification, back-test, or sensitivity analysis for this proxying rule is given on this page.

### Figures
None.

### Unreadable
- p.46: the symbol `v_{i,s-1}` in (1.26) is legible as "v", but the page gives no definition of it — its meaning is inferred, not stated here.
- p.46: the whole lower two-thirds of the page is faint show-through of p.47 and is not readable as p.46 content (correctly so — it is not p.46 content).

---

## PDF page 47 (printed p.47)

### Headings
- **Earnings Yield** (style/section heading, bold)
  - __Earnings-to-Price__ (underlined sub-heading)
  - __EBITDA-to-Enterprise Value__ (underlined sub-heading)
  - __Normalised Earnings-to-Price__ (underlined sub-heading)
- **Dividend Yield** (bold heading)
- **Value** (bold heading)
  - __Book Value-to-Price__ (underlined sub-heading, section continues on p.48)

### Equations
- (1.28) Earnings-to-Price: "The ratio of Earnings-per-share EPS to month end price:"
  `EPS_{i,s} / P_{i,t}` , where `s <= t`
- (1.29) EBITDA-to-Enterprise Value: "The ratio of EBITDA to Enterprise Value EV:"
  `EBITDA_{i,s} / EV_{i,t}`
- (1.30) Normalised Earnings-to-Price: "An Earnings-to-Price ratio where the numerator is replaced by the fitted value of the most recent EPS from a univariate regression of EPS on time:"
  `(alphahat_i + betahat_i * s) / P_{i,t}`
- (1.31) the regression that produces those estimates: "where alphahat_i and betahat_i are estimated in the following regression:"
  `EPS_{i,u} = alpha_i + beta_i * u + epsilon_{i,u}`
- (1.32) Dividend Yield: "The ratio of Dividends-per-share DPS to month end price:"
  `DPS_{i,s} / P_{i,t}` , where `s <= t`

Symbols defined on this page: `EPS_{i,s}` = earnings per share of company i at financial-statement date s; `P_{i,t}` = month-end price of i at t; `EBITDA_{i,s}`; `EV_{i,t}` = Enterprise Value; `DPS_{i,s}` = dividends per share; `alphahat_i`, `betahat_i` = OLS intercept/slope of EPS on time; `u` = the time index in the EPS-on-time regression; `epsilon_{i,u}` = regression residual; `s <= t` = accounting data as of a date no later than the pricing date.

### Tables
None.

### Numbers
- p.47: **5 years** — "The regression uses the last 5 years of EPS data." (window for the Normalised Earnings-to-Price regression 1.31).
- p.47: equation numbers 1.28–1.32.

### Terms (named descriptors / styles)
- p.47: Style **Earnings Yield**, with descriptors **Earnings-to-Price**, **EBITDA-to-Enterprise Value**, **Normalised Earnings-to-Price**.
- p.47: Descriptor/style **Dividend Yield**.
- p.47: Style **Value**, first descriptor **Book Value-to-Price**.

### Claims / methodological choices
- Every yield descriptor uses **month-end price** in the denominator while the numerator uses the most recent available accounting figure at date `s <= t` — an explicit lag convention to avoid look-ahead, though no justification is spelled out.
- "Normalised" earnings are the **fitted value at the most recent date** from a 5-year linear time regression of EPS — i.e. a trend-smoothed EPS rather than a trailing average. No reason is given for choosing a linear trend fit over an average, nor for the 5-year window.
- EBITDA is scaled by Enterprise Value (not by price), unlike the other two Earnings Yield descriptors.

### Figures
None.

### Unreadable
- p.47: nothing material. (Equation 1.31 is printed in noticeably light grey but is legible when enlarged.)

---

## PDF page 48 (printed p.48)

### Headings
- (continuation of __Book Value-to-Price__ from p.47 — no repeated heading)
- __Sales-to-Price__ (underlined sub-heading)
- __Cash Flow-to-Price__ (underlined sub-heading)

### Equations
- (1.33) Book Value-to-Price: "The ratio of Book Value of Common Equity (per share) to month end price:"
  `(CE_{i,s} / N_{i,s}) / P_{i,t}` , where `s <= t`
- (1.34) Sales-to-Price: "The ratio of Net Sales/Revenues (per share) to month end price:"
  `(S_{i,s} / N_{i,s}) / P_{i,t}` , where `s <= t`
- (1.35) Cash Flow-to-Price: "The ratio of Funds From Operations (per share) to month end price:"
  `(FFO_{i,s} / N_{i,s}) / P_{i,t}` , where `s <= t`

Symbols defined here: `CE_{i,s}` = Book Value of Common Equity; `N_{i,s}` = number of shares (share count used to put the accounting item on a per-share basis); `S_{i,s}` = Net Sales / Revenues; `FFO_{i,s}` = Funds From Operations; `P_{i,t}` = month-end price.

### Tables
None.

### Numbers
- p.48: equation numbers 1.33, 1.34, 1.35. No other numeric values appear on this page.

### Terms
- p.48: Value-style descriptors **Book Value-to-Price**, **Sales-to-Price**, **Cash Flow-to-Price**.
- p.48: "Funds From Operations" is the cash-flow proxy chosen (not free cash flow, not operating cash flow).

### Claims / methodological choices
- All three Value descriptors are constructed **per share** (accounting item divided by share count `N_{i,s}`) and then divided by month-end price, rather than as aggregate ratios (market cap in the denominator).
- The `s <= t` lag convention is repeated for each descriptor.
- No justification given for choosing FFO as the cash-flow measure.

### Figures
None.

### Unreadable
- p.48: nothing material on the dark (real) text. Lower half of the page is show-through of p.49.

---

## PDF page 49 (printed p.49)

### Headings
- **Growth** (bold style heading)
  - __Asset Growth Rate__
  - __Change in Assets__
  - __Predicted Sales Growth__
  - __Growth of Total Sales__
- **Variation in Capital Structure** (bold heading; content continues on p.50)

### Equations
- (1.36) Asset Growth Rate: "The ratio of the estimated slope coefficient from a regression of Total Assets A on time, to the average Total Assets over the last 5 years:"
  `betahat_i / ( (1/5) * sum_{s=t-4}^{t} A_{i,s} )`
- (1.37) "where beta_i is estimated in the following regression:"
  `A_{i,s} = alpha_i + beta_i * s + epsilon_{i,s}` , where `s = t-4, ..., t`
- (1.38) Change in Assets: "The difference in the natural logarithm of Total Assets A_i over the previous two years:"
  `ln(A_{i,t}) - ln(A_{i,t-1})`
- (1.39) Predicted Sales Growth: "The percentage difference in the mean Sales forecast for FY1 and FY2:"
  `(FY2_{i,t} - FY1_{i,t}) / ( (1/2) * ( |FY2_{i,t}| + |FY1_{i,t}| ) )`
- (1.40) Growth of Total Sales: "The ratio of the estimated slope coefficient from a regression of Total Sales S on time, to the average Total Sales over the last 5 years:"
  `betahat_i / ( (1/5) * sum_{s=t-4}^{t} S_{i,s} )`
- (1.41) "where betahat_i is estimated in the following regression:"
  `S_{i,s} = alpha_i + beta_i * s + epsilon_{i,s}` , where `s = t-4, ..., t`

Symbols: `A_{i,s}` = Total Assets of company i at s; `S_{i,s}` = Total Sales; `betahat_i` = OLS slope of the accounting item on time; `FY1_{i,t}` / `FY2_{i,t}` = mean analyst Sales forecast for fiscal year 1 and fiscal year 2; `epsilon_{i,s}` = residual.

### Tables
None.

### Numbers
- p.49: **5 years** — averaging window and regression window for Asset Growth Rate (1.36/1.37) and Growth of Total Sales (1.40/1.41); the sum runs `s = t-4 … t` (5 annual observations) and is divided by 5 (`1/5`).
- p.49: **two years** — Change in Assets (1.38) is a 1-lag log difference over "the previous two years", i.e. `ln A_t - ln A_{t-1}` with annual data.
- p.49: **1/2** — the symmetric-denominator factor in Predicted Sales Growth (1.39).
- p.49: FY1 and FY2 — forecast horizons 1 and 2 fiscal years ahead.
- p.49: equation numbers 1.36–1.41.

### Terms
- p.49: Style **Growth** with descriptors **Asset Growth Rate**, **Change in Assets**, **Predicted Sales Growth**, **Growth of Total Sales**.
- p.49: Style/descriptor group **Variation in Capital Structure**.

### Claims / methodological choices
- Growth is measured as a **trend slope scaled by the level** (slope of a 5-year time regression divided by the 5-year mean) rather than as a point-to-point growth rate — this makes the descriptor a normalised trend growth rate.
- Predicted Sales Growth uses a **symmetric denominator built from absolute values** ((|FY2| + |FY1|)/2), which keeps the ratio defined and sign-stable when forecasts are near zero or negative. The choice is made without explicit justification.
- Both the Asset and Sales trend descriptors reuse identical machinery (same window, same normalisation).
- Note: (1.36) is described in words as using "the estimated slope coefficient" and the accompanying text of (1.37) refers to `beta_i` (unhatted) while (1.36) and (1.41) use `betahat_i` — inconsistent hatting in the source.

### Figures
None.

### Unreadable
- p.49: in the "where ... is estimated in the following regression" line under (1.36) the coefficient is printed as `beta_i` without a visible hat, whereas the numerator of (1.36) clearly has a hat — [UNREADABLE/AMBIGUOUS: whether the hat is present on beta in the line above (1.37)].

---

## PDF page 50 (printed p.50)

### Headings
- (continuation of **Variation in Capital Structure** from p.49)
- **Profitability** (bold style heading)
  - __Return on Capital Employed__
  - __Return on Equity__
  - __Return on Assets__
  - __Interest Coverage__
  - __Cash Flow to Liabilities__
  - __Operating Profit Margin__

### Equations
- (1.42) Variation in Capital Structure: "The average 1-year change in various segments of the capital structure over the previous 4 years:"
  `[ (1/4) * sum_{s=t-3}^{t} ( |N_{i,s-1} - N_{i,s}| * P_{i,s-1} + |LTD_{i,s-1} - LTD_{i,s}| + |PS_{i,s-1} - PS_{i,s}| ) ] / |CE_{i,t} + LTD_{i,t} + PS_{i,t}|`
  , where `s <= t`
- Return on Capital Employed: no equation — "The latest Return on Capital Employed provided by Worldscope."
- (1.43) Return on Equity: "The ratio of Earnings-per-share EPS to average Book Value of Common Equity CE over the previous 2 years:"
  `100 * [ EPS_{i,t} / ( (1/2) * ( CE_{i,t}/N_{i,t} + CE_{i,t-1}/N_{i,t-1} ) ) ]`
- Return on Assets: no equation — "The latest Return on Assets provided by Worldscope."
- (1.44) Interest Coverage: "The ratio of Operating Income OI to Interest Expense on Debt I:"
  `OI_{i,t} / I_{i,t}`
- (1.45) Cash Flow to Liabilities: "The ratio of average Funds From Operations FFO over the previous 5 years, to Current Liabilities CL:"
  `( (1/5) * sum_{s=t-4}^{t} FFO_{i,s} ) / CL_{i,t}`
- (1.46) Operating Profit Margin: "The ratio of Operating Income OI to Net Sales S:"
  `100 * ( OI_{i,t} / S_{i,t} )`

Symbols: `N` = shares outstanding; `P` = price; `LTD` = Long-term Debt; `PS` = Preferred Stock; `CE` = Book Value of Common Equity; `OI` = Operating Income; `I` = Interest Expense on Debt; `FFO` = Funds From Operations; `CL` = Current Liabilities; `S` = Net Sales.

### Tables
None.

### Numbers
- p.50: **1-year change**, averaged over the **previous 4 years** — Variation in Capital Structure; sum runs `s = t-3 … t` (4 annual differences) with factor `1/4`.
- p.50: **previous 2 years** — averaging window for Book Value of Common Equity in Return on Equity (1.43); factor `1/2`.
- p.50: **previous 5 years** — averaging window for FFO in Cash Flow to Liabilities (1.45); factor `1/5`, sum `s = t-4 … t`.
- p.50: **100 ×** — Return on Equity (1.43) and Operating Profit Margin (1.46) are expressed in percent.
- p.50: equation numbers 1.42–1.46.

### Terms
- p.50: Style **Profitability** with descriptors **Return on Capital Employed**, **Return on Equity**, **Return on Assets**, **Interest Coverage**, **Cash Flow to Liabilities**, **Operating Profit Margin**.
- p.50: **Worldscope** named as the vendor data source for two descriptors.

### Claims / methodological choices
- Two of the six Profitability descriptors (**Return on Capital Employed** and **Return on Assets**) are taken **directly from Worldscope as vendor-computed fields** with no formula given and no statement of how Worldscope defines them — a conspicuous absence of definition relative to the other descriptors.
- Variation in Capital Structure valuates share-count changes at the **lagged price** `P_{i,s-1}`, and takes absolute values of each segment change, so issuance and buy-backs both increase the descriptor (it measures *activity*, not direction). The denominator is the absolute total book capital `|CE + LTD + PS|` at t.
- Return on Equity uses a **2-year average book equity per share** denominator rather than beginning-of-period equity; no justification given.
- Descriptor windows are heterogeneous within the same style (4-year, 2-year, 5-year, latest) with no stated rationale.

### Figures
None.

### Unreadable
- p.50: nothing material. (The lower-left "aladdin" footer is partly covered by a "Galaxy Z Flip7" camera watermark; the footer "Page 50" is legible.)

---

## PDF page 51 (printed p.51)

### Headings
- **Small-Cap** (bold heading)
- **Mid-Cap** (bold heading)

### Equations
- (1.47) Small-Cap: "Small-Cap is a continuous function taking values in the interval [0,1], which identifies small cap stocks in the Estimation Universe:"
  `SML_{i,t} = { exp( -( ( ln(1 + k_{i,t}) - mu_t ) / sigma_t )^2 ),   if k_{i,t} <  alpha_1 * M_t`
  `            { 1,                                                    if k_{i,t} >= alpha_1 * M_t`
  where
  - `mu_t    = ln(1 + alpha_1 * M_t)`
  - `sigma_t = sqrt( -( ln(1 + alpha_2 * M_t) - mu_t )^2 / ln(alpha_3) )`
  - `M_t`     = number of assets in the Estimation Universe
  - `k_{i,t}` = numerical rank assigned to the company market capitalisation relative to other companies in the Estimation Universe
  - `alpha_1 = 0.95, alpha_2 = 0.75, alpha_3 = 0.2`
- (1.48) Mid-Cap: "The Mid-Cap factor for asset i, date t is defined as:"
  `MID_{i,t} = exp( -( ( ln(1 + r_{i,t}) - mu_t ) / sigma_t )^2 )`
  where
  - `mu_t    = ln(1 + alpha_1 * N_t)`
  - `sigma_t = sqrt( -( ln(1 + alpha_2 * N_t) - mu_t )^2 / ln(alpha_3) )`
  - `N_t`     = number of assets in the stadardisation [sic] universe at time t
  - `r_{i,t}` = numerical rank of asset i at time t, based on the company market capitalisation of asset i relative to the standardisation universe at time t, defined below
  - `alpha_1 = 0.60, alpha_2 = 0.54, alpha_3 = 0.7`

### Tables
None (the parameter definitions are laid out as an aligned "where" list, not a ruled table).

### Numbers
- p.51: Small-Cap parameters — **alpha_1 = 0.95**, **alpha_2 = 0.75**, **alpha_3 = 0.2** (verified at 4x enlargement).
- p.51: Mid-Cap parameters — **alpha_1 = 0.60**, **alpha_2 = 0.54**, **alpha_3 = 0.7** (verified at 4x enlargement).
- p.51: Small-Cap is a continuous function on the interval **[0,1]**.
- p.51: Small-Cap "is designed to give exposure to smaller companies which reside in capitalisation **deciles 8, 9 and 10**."
- p.51: "The Mid-Cap substyle assigns an exposure to companies in **deciles 6 and 7**."
- p.51: exponent **2** (the Gaussian squared term) in both (1.47) and (1.48).
- p.51: equation numbers 1.47, 1.48.

### Terms
- p.51: Sub-styles **Small-Cap** (`SML`) and **Mid-Cap** (`MID`).
- p.51: **Estimation Universe** (used for Small-Cap ranking, size `M_t`).
- p.51: **standardisation universe** (used for Mid-Cap ranking, size `N_t`; printed once as "stadardisation universe" — typo in source).
- p.51: **capitalisation deciles** as the targeting device (8/9/10 for Small-Cap, 6/7 for Mid-Cap).

### Claims / methodological choices
- Both size sub-styles are built as **Gaussian (bell-shaped) functions of the log of the market-cap rank**, not of log market cap itself — i.e. exposure is a smooth function of cross-sectional rank, making the descriptor distribution-free with respect to the level of capitalisation.
- Small-Cap is deliberately **capped at 1** (flat top) for all companies ranked beyond `alpha_1 * M_t`, so the smallest ~5% (given alpha_1 = 0.95) all get full exposure; Mid-Cap has no such flat region and is a pure bell centred on the mid-cap rank.
- `sigma_t` is calibrated by construction: it is set so that the Gaussian takes value `alpha_3` at rank `alpha_2 * M_t` (this follows algebraically from the formula), i.e. the authors pin the curve through a chosen (rank, exposure) point. The paper states the parameter values but gives **no empirical justification for the specific choices 0.95/0.75/0.2 and 0.60/0.54/0.7** beyond the stated decile-targeting intent.
- Small-Cap and Mid-Cap use **different universes** (Estimation Universe vs. standardisation universe) — the reason for the difference is not explained on this page.

### Figures
None (though both formulas describe a bell curve / capped bell curve in rank space).

### Unreadable
- p.51: the Mid-Cap rank symbol is printed as `r_{i,t}`, the same glyph used elsewhere in the paper for returns — legible but ambiguous in meaning; the page says it is "defined below" but no definition appears on this page.
- p.51: source typo "stadardisation" (transcribed verbatim, not a scan error).

---

## PDF page 52 (printed p.52)

### Headings
- **Macro-economic Betas** (bold heading)

### Equations
- (1.49) "The estimated slope coefficient gammahat_i from an exponentially weighted univariate regression of the residuals in regression (1.12) on the returns of the specified macro-economic factor f:"
  `l*ehat_{i,s} = a_i + gamma_i * f_s + u_{i,s}`
  Symbols: `l*ehat_{i,s}` = the dependent variable, the residual from regression (1.12) — printed as an italic "l" immediately followed by "e" with a circumflex/hat, i.e. `lê_{i,s}`; `a_i` = intercept; `gamma_i` = the macro-economic beta (its estimate `gammahat_i` is the descriptor); `f_s` = return of the specified macro-economic factor at s; `u_{i,s}` = residual.

### Tables
None.

### Numbers
- p.52: reference to **regression (1.12)** twice (residual source, and weighting/window source).
- p.52: equation number 1.49.
- p.52: returns are **weekly**.

### Terms
- p.52: **Macro-economic Betas** — descriptor family; the specific macro-economic factors are not enumerated on this page ("the specified macro-economic factor f").

### Claims / methodological choices
- "All returns are **weekly** and in **excess of the local risk-free rate**."
- "The exponential weighting function and data window **match those used in regression 1.12**." — i.e. the half-life and window are inherited from the earlier market-beta regression and are deliberately not restated here; **no half-life number is given on this page**.
- The macro betas are estimated on the **residuals** of (1.12), not on raw returns — so they are orthogonal to whatever (1.12) already explains, but this design choice is stated without justification.
- The page is otherwise nearly empty (three sentences and one equation), the remaining space being show-through of p.53.

### Figures
None.

### Unreadable
- p.52: [UNREADABLE/AMBIGUOUS: the dependent-variable symbol in (1.49). At 12x magnification it clearly renders as an italic lowercase "l" followed by "ê" (e with hat). Whether the leading "l" is a separate modifier (e.g. "local"), part of a two-letter symbol, or a typesetting artefact cannot be determined from this page.]

---

## PDF page 53 (printed p.53)

### Headings
- **Leverage** (bold style heading)
  - __Debt-to-Assets__
  - __Market Leverage__
  - __Balance Sheet Cash__
  - __Book Leverage__
- **Quality** (bold style heading)
  - __Equity Dilution__

### Equations
- Debt-to-Assets: no equation — "The latest Debt-to-Assets ratio provided by Worldscope."
- (1.50) Market Leverage: "The ratio of Long-term Debt LTD and Preferred Stock PS to Market Capitalisation:"
  `1 + ( LTD_{i,s} + PS_{i,s} ) / ( N_{i,t} * P_{i,t} )` , where `s <= t`
- (1.51) Balance Sheet Cash: "The ratio of Balance Sheet Cash C to Total Assets A:"
  `C_{i,t} / A_{i,t}`
- (1.52) Book Leverage: "The ratio of Long-term Debt LTD and Preferred Stock PS to the Book Value of Common Equity CE:"
  `1 + ( LTD_{i,s} + PS_{i,s} ) / CE_{i,t}`
- (1.53) Equity Dilution: "The 1 year difference in log market capitalisation due to dilution of common equity:"
  `- ln[ ( Capt_{i,t-1} * (1 + r_{i,t}) ) / Capt_{i,t} ]`
  "where r is the total return over the previous year."

Symbols: `LTD` = Long-term Debt; `PS` = Preferred Stock; `N_{i,t} * P_{i,t}` = market capitalisation (shares × price); `C_{i,t}` = Balance Sheet Cash; `A_{i,t}` = Total Assets; `CE_{i,t}` = Book Value of Common Equity; `Capt_{i,t}` = market capitalisation at t; `r_{i,t}` = total return over the previous year.

### Tables
None.

### Numbers
- p.53: the additive constant **1** in both (1.50) and (1.52) (leverage descriptors are shifted by 1).
- p.53: **1 year** difference window for Equity Dilution (1.53).
- p.53: equation numbers 1.50–1.53.

### Terms
- p.53: Style **Leverage** with descriptors **Debt-to-Assets**, **Market Leverage**, **Balance Sheet Cash**, **Book Leverage**.
- p.53: Style **Quality** with descriptor **Equity Dilution**.
- p.53: **Worldscope** again named as vendor source for Debt-to-Assets.

### Claims / methodological choices
- Leverage descriptors are defined as `1 + debt/equity-or-cap` rather than `debt/(debt+equity)`; the "+1" shift is applied without explanation (it makes the descriptor equal to (capital + debt)/capital and keeps it positive).
- **Balance Sheet Cash** — a cash-holding ratio — is filed under *Leverage* rather than Quality or Profitability; no rationale given.
- Equity Dilution isolates the part of the market-cap change **not** explained by total return: the ratio compares last year's cap grown at the total return to this year's actual cap, and the **negative** log makes issuance (dilution) a positive exposure.
- **Debt-to-Assets is taken as a vendor field with no formula**, unlike the other three Leverage descriptors.

### Figures
None.

### Unreadable
- p.53: nothing material. The footer logo is partially obscured by a camera watermark; "Page 53" is legible.

---

## PDF page 54 (printed p.54)

### Headings
- **Foreign Sensitivity** (bold style heading)
  - __Foreign Sales__
  - __Foreign Assets__

### Equations
- (1.54) Foreign Sales: "The Foreign Sales (FSAL) Sub-Style for company i, at financial period end t is defined as:"
  `FSAL_{i,t} = FS_{i,t} / S_{i,t}`
  "where FS_{i,t} denotes the foreign sales for company i and S_{i,t} the total assets of company i"  ← transcribed verbatim; the source says "total assets" where "total sales" is evidently meant.
- (1.55) Foreign Assets: "The Foreign Assets (FASS) Sub-Style for company i, at financial period end t is defined as"
  `FASS_{i,t} = FS_{i,t} / A_{i,t}`
  "where FS_{i,t} denotes the foreign assets for company i and A_{i,t} the total assets of company i."

Symbols: `FSAL_{i,t}` = Foreign Sales sub-style exposure; `FASS_{i,t}` = Foreign Assets sub-style exposure; `FS_{i,t}` = foreign sales in (1.54) and foreign **assets** in (1.55) — the same symbol `FS` is reused for two different quantities; `S_{i,t}` = total sales (labelled "total assets" in the source); `A_{i,t}` = total assets.

### Tables
None.

### Numbers
- p.54: equation numbers 1.54, 1.55. No other numeric values on this page — no windows, no parameters, no counts.

### Terms
- p.54: Style **Foreign Sensitivity** with sub-styles **Foreign Sales (FSAL)** and **Foreign Assets (FASS)**.
- p.54: "financial period end t" — the timing convention for both sub-styles.

### Claims / methodological choices
- Both foreign-sensitivity descriptors are simple **contemporaneous ratios at financial-period end**, with no averaging, no lag convention (`s <= t` is not used here, unlike the Value/Yield descriptors) and no winsorisation stated.
- No justification is given for using raw foreign-share ratios as a proxy for currency/foreign-market sensitivity rather than, for example, an estimated FX beta.
- Notational defect: `FS` denotes foreign *sales* in (1.54) and foreign *assets* in (1.55), and the "where" clause of (1.54) mislabels `S_{i,t}` as "total assets".

### Figures
None.

### Unreadable
- p.54: nothing unreadable — the page is mostly blank below (1.55) apart from faint show-through of p.55's heading and table.

---

## PDF page 55 (printed p.55)

### Headings
- **INVENTORY OF ALL SUBSTYLES INVESTIGATED** (large bold section heading, all caps)

### Body text (verbatim)
"This list shows an inventory of substyles that were investigated during the model construction process. This is a subset of the full list of 200+ which includes all variants, e.g. relative strength was constructed over different horizons: 1 month, 3 months, 6 months, 11 months (with a 1 month lag) and 12 months — which are counted as 5 different substyles."

### Equations
None on this page.

### Tables
- p.55: A large two-column-pair table (apparently: Style category | Substyle name, repeated twice across the page, roughly 40+ rows) is **visible only as faint grey show-through** on this scan. Consistent with the pattern on pages 46–54, this ghost image is the content of the FOLLOWING page (p.56), not of p.55. On p.55 itself only the heading and the introductory paragraph above are actually printed in black ink.
  I attempted contrast stretching, autocontrast, unsharp masking and up to 6x upscaling on the region; the glyphs remain below the resolution of the 952×1288 source image. **No cell values are transcribed, because none could be read with confidence.**

### Numbers
- p.55: **200+** — the size of the full list of substyles investigated (of which the printed inventory is a subset).
- p.55: relative-strength horizons investigated: **1 month, 3 months, 6 months, 11 months (with a 1 month lag), 12 months**.
- p.55: **5** — the number of distinct substyles those relative-strength variants are counted as.
- p.55: **1 month lag** applied to the 11-month relative strength variant.

### Terms
- p.55: **substyle** (the unit of the inventory); **relative strength** named as the worked example of a substyle with multiple horizon variants.

### Claims / methodological choices
- The authors state the model-construction process investigated **more than 200 substyles**, and that the printed inventory is only a subset (variants collapsed).
- Each horizon variant of a descriptor is **counted as a separate substyle**, which is how the 200+ count is reached — an important caveat for interpreting that headline number.
- The page gives **no information about the selection procedure** — no criterion, statistic, or threshold by which substyles were kept or discarded, and no multiple-testing correction is mentioned despite 200+ candidates being tested. This is a conspicuous omission.

### Figures
None.

### Unreadable
- p.55: [UNREADABLE: the entire substyle inventory table occupying roughly the middle half of the page. It appears only as faint show-through of the next page at this scan resolution; category labels and substyle names cannot be read with confidence. Cropping/enhancement at 3x–6x was attempted and failed. Treat the table content as belonging to PDF p.56 and transcribe it from that page's image.]
