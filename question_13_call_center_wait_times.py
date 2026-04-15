call_data = {
    "9876543210": 5,
    "9123456780": 12,
    "9988776655": 8,
    "9090909090": 15,
    "9012345678": 20
}

escalation_queue = []

for phone, wait_time in call_data.items():
    if wait_time > 10:
        escalation_queue.append(phone)

print("Escalation Queue:", escalation_queue)