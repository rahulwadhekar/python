stocks = {
    "AAPL": [150, 170],
    "GOOG": [200, 180],
    "TSLA": [300, 350]
}

top_gainer = ""
top_loser = ""
max_gain = -999
min_gain = 999

for name, (open_p, close_p) in stocks.items():
    change = ((close_p - open_p) / open_p) * 100

    if change > max_gain:
        max_gain = change
        top_gainer = name

    if change < min_gain:
        min_gain = change
        top_loser = name

print("Top Gainer:", top_gainer)
print("Top Loser:", top_loser)