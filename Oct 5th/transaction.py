def analysis(transactions):
    dic = {
        "balance" : 0,
"total_income" : 0,
"total_expenses" : 0,
"largest_expense" : [ "", 0],
"largest_income" : [ "", 0],
"expense_count" : 0,
"income_count" : 0,
"status" : ""
    }
    for transaction in transactions:
        if transaction["type"] == "income":
            print("rrrr")
            dic["balance"] += transaction["amount"]
            dic["income_count"] += 1
            dic["total_income"] += transaction["amount"]
            if transaction["amount"] > dic["largest_income"][1]:
                dic["largest_income"][1] = transaction["amount"]
                dic["largest_income"][0] = transaction["name"]
        if dic["balance"] > 0:
            dic["status"] = "Positive balance"
        elif dic["balance"] == 0:
            dic["status"] = "Zero balance"
        else:
            dic["status"] = "Negative balance"
        if transaction["type"] == "expense":
            dic["balance"] -= transaction["amount"]
            dic["expense_count"] += 1
            dic["total_expenses"] += transaction["amount"]
            if transaction["amount"] > dic["largest_expense"][1]:
                dic["largest_expense"][1] = transaction["amount"]
                dic["largest_expense"][0] = transaction["name"]
        
        return dic


transactions = [
    {"name": "Laptop", "amount": 250000, "type": "expense"},
    {"name": "Salary", "amount": 500000, "type": "income"},
    {"name": "Internet", "amount": 30000, "type": "expense"},
    {"name": "Freelance", "amount": 150000, "type": "income"},
    {"name": "Food", "amount": 45000, "type": "expense"}
]

# Expected Output
# Total income: 650000
# Total expenses: 325000
# Balance: 325000
# Largest expense: Laptop (250000)
# Number of expenses: 3
# Status: Positive balance

print(analysis(transactions))

