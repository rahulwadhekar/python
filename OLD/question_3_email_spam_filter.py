subs = ["Win free lottery", "Meeting", "URGENT update"]

spam = set()
inbox = set()
keywords = ["free", "lottery", "urgent"]

for s in subs:
    if any(k in s.lower() for k in keywords):
        spam.add(s)
    else:
        inbox.add(s)

print("Spam:", spam)
print("Inbox:", inbox)