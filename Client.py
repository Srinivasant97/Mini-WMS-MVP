
import requests

P = False
while True:
    while P:
        source = input("Enter the Source:")
        N = int(input("Enter the number of SKU to Order:"))
        Lines = []
        for i in range(N):
            L = {}
            name1 = input("Enter the name of SKU:")
            quantity1 = int(input("Enter the Quantity:"))
            L["name"] = name1
            L["quantity"] = quantity1
            Lines.append(L)

        da = {"source": source, "Lines": Lines}
        a = requests.post("http://127.0.0.1:8000/", json=da)
        print(a.status_code)
        if a.status_code == 400:
            print("Quantity Should be above 0 and below 6")
            continue
        Conti = input("Another Order?[Y/N]")
        if Conti == "N":
            P = False
        if a.status_code == 500:
            P = False
    Report = input("Do you want to See Report?[Y/N]:")
    if Report == "Y":
        Order_Report = requests.get("http://127.0.0.1:8000/order_report/")
        print(Order_Report.content.decode())

    Setup = input("Do you want to Set SKU?[Y/N]:")
    if Setup == "N":
        continue
    Item = ["A", "B", "C", "D", "E"]
    SKU = {}
    for i in Item:
        SKU[i] = int(input(f"Enter the Quantity of {i}:"))
    Se = requests.post("http://127.0.0.1:8000/setup/", json=SKU)
    print(Se.content.decode())
    Exit = input("Do You Want to Exit?[Y/N]:")
    if Exit == "Y":
        break
