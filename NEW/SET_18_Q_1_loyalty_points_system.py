purchases = [
    {'customer_id': 1001, 'purchase_amount': 4500},
    {'customer_id': 1002, 'purchase_amount': 6000}
]

points = {}

for p in purchases:
    cid = p['customer_id']
    amt = p['purchase_amount']

    pts = amt // 100
    if amt > 5000:
        pts += 50

    points[cid] = pts

print("Loyalty Points:", points)