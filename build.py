"""Regenerate CLAIMS.md from claims.csv and print the rating tally."""
import collections
import csv

ORDER = ["Statewide", "Biography", "Legislation", "Funding", "State aid",
         "Volunteer events", "Constituent service", "Advocacy"]

rows = list(csv.DictReader(open("claims.csv", encoding="utf-8")))
print(len(rows), "claims", dict(collections.Counter(r["rating"] for r in rows)))

out = ["# Claims ledger\n",
       "Every distinct claim on the *Rebecca Delivers* page (reviewed 2026-10-24), "
       "deduplicated across community tabs. Ratings key is in [README.md](README.md).\n"]
for cat in ORDER:
    rs = [r for r in rows if r["category"] == cat]
    if not rs:
        continue
    out.append(f"\n## {cat}\n\n| ID | Claim (paraphrased) | Tabs | Rating | Finding | Sources |\n|---|---|---|---|---|---|")
    for r in rs:
        urls = [u.strip() for u in r["sources"].split("|") if u.strip()]
        src = " ".join(f"[{i + 1}]({u})" for i, u in enumerate(urls)) or "—"
        out.append(f"| {r['id']} | {r['claim']} | {r['communities']} | {r['rating']} | {r['finding']} | {src} |")

open("CLAIMS.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
