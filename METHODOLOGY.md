# Methodology

**Subject:** https://www.kassayforassembly.com/rebecca-delivers ("Paid for by Friends of Kassay for Assembly 2026"), captured October 24, 2026.

## Process

1. **Inventory.** Every factual statement across the intro and all 13 community tabs (Coram, Gordon Heights, Selden, Port Jefferson Village, Port Jefferson Station, Stony Brook, Strongs Neck, Old Field, Poquott, Terryville, Setauket, Belle Terre, Three Village) was extracted, then deduplicated into 64 unique claims. The `communities` column records every tab a claim appears in.
2. **Source hierarchy.** (1) Official records: NYS Senate/Assembly bill pages, chapter numbers, Governor's releases, NYS Division of the Budget. (2) The member's own Assembly office releases (official, but self-reported). (3) Independent news (TBR News Media, News12, SI/High School). (4) Supporter letters — used only as weak corroboration.
3. **Rating.** Each claim is rated on whether the evidence supports it *as worded on the page*:
   - ✅ **Verified** — matches the source.
   - 🟡 **Verified with caveat** — accurate or plausible, but omitted context (shared credit, outcome, attribution) would change a reasonable reader's takeaway.
   - 🟠 **Overstated / partly accurate** — a material part is inflated, conflated with someone else's work, or contradicted by the candidate's own records.
   - ⚪ **Unverified** — no public record found. This is *not* a finding that the claim is false.
   - 🔵 **Activity claim** — ongoing work or attendance that public records can't confirm or refute.
   - ❌ **False** — contradicted by evidence. (None found.)

## Limits

- The NYSED state-aid run portal was unreachable during this review, so the five school-aid totals were checked for magnitude only.
- Legislative-initiative (member item) grants are often not published per member; a ⚪ rating there reflects missing public data.
- The member's own releases count as confirmation that funding was *announced*, not that it was *disbursed*.
- The page may change after capture; claim wording here is paraphrased.

## Reproducing / updating

`claims.csv` is the source of truth. Regenerate `CLAIMS.md` with:

```bash
python3 build.py
```
