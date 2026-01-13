EXERCISE: You’re given a list of customers and how much they spent in a store. Your task is to classify customers into spending categories. customers = [ {"name": "Alice", "spend": 45}, {"name": "Bob", "spend": 120}, {"name": "Charlie", "spend": 300}, {"name": "Diana", "spend": 80} ] Classify customers based on how much they spent:

Low spender → spend < 50

Medium spender → spend 50–149

High spender → spend ≥ 150
# getting how much each customer spent
customers = [
    {"name": "Alice", "spend": 45},
    {"name": "Bob", "spend": 120},
    {"name": "Charlie", "spend": 300},
    {"name": "Diana", "spend": 80}
]
for customer in customers:
    print(customer)
  {'name': 'Alice', 'spend': 45}
{'name': 'Bob', 'spend': 120}
{'name': 'Charlie', 'spend': 300}
{'name': 'Diana', 'spend': 80}
customers = [
    {"name": "Alice", "spend": 45},
    {"name": "Bob", "spend": 120},
    {"name": "Charlie", "spend": 300},
    {"name": "Diana", "spend": 80}
]
for customer in customers:
    name = customer ["name"]
    spend = customer ["spend"]
    if spend<50:
        print(name,"low spender")
    elif spend <150:
        print(name,"medium spender")
    else :
        print(name,"high spender")
Alice low spender
Bob medium spender
Charlie high spender
Diana medium spender
