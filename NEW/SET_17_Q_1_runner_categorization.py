runners = {
    101: (25, 120),
    102: (40, 110),
    103: (60, 130)
}

categories = {
    "Under30": [],
    "30to50": [],
    "Over50": []
}

for bib, (age, time) in runners.items():
    if age < 30:
        categories["Under30"].append((bib, time))
    elif age <= 50:
        categories["30to50"].append((bib, time))
    else:
        categories["Over50"].append((bib, time))

for cat, data in categories.items():
    if data:
        fastest = min(data, key=lambda x: x[1])
        print(cat, "Fastest Runner:", fastest[0])