votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "Bob", "Bob"]

vote_count = {}

for candidate in votes:
    if candidate in vote_count:
        vote_count[candidate] += 1
    else:
        vote_count[candidate] = 1

winner = None
max_votes = 0

for candidate, count in vote_count.items():
    if count > max_votes:
        max_votes = count
        winner = candidate

print("Vote Count:", vote_count)
print("Winner:", winner)