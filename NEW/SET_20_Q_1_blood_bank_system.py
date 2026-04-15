blood = {"A+": 10, "O-": 5}

while True:
    req = input("Enter blood type (STOP to exit): ")
    if req == "STOP":
        break

    qty = int(input("Enter units: "))

    if req in blood and blood[req] >= qty:
        blood[req] -= qty
        print("Dispatched")
    else:
        print("Insufficient Stock")