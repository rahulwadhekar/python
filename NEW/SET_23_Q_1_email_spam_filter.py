subjects = ["Win free lottery", "Meeting update", "URGENT notice"]

spam = set()
inbox = set()

for s in subjects:
    if "free" in s.lower() or "lottery" in s.lower() or "urgent" in s.lower():
        spam.add(s)
    else:
        inbox.add(s)

print("Spam:", spam)
print("Inbox:", inbox)