playlist = {
    "Pop": [3, 4, 5],
    "Rock": [6, 7, 8],
    "EDM": [2, 3, 4]
}

total_duration = {}

for genre, durations in playlist.items():
    total = sum(durations)
    total_duration[genre] = total

    if total > 60:
        print(f"Warning: {genre} exceeds 60 minutes")

print("Total Duration:", total_duration)