messages = ["item broken", "hello", "need refund", "call manager"]

urgent = []

keywords = ["broken", "refund", "manager"]

for msg in messages:
    if any(k in msg.lower() for k in keywords):
        urgent.append(msg)

print("Urgent Messages:", urgent)