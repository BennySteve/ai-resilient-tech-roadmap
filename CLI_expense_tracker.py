import json
## FIRST PROJECT ##
# loading json file
def load_expenses():
  try:
    with open("expenses.json", "r") as f:
    return json.load(f)
  except FileNotFoundError:
    return []
# saving to json file
def save_expenses(expenses):
  with open("expenses.json", "w") as f:
  json.dump(expenses, f)
# adding expense in python and calling save_expenses()
def add_expense(expenses):
  item = input("Item: ").strip()
while True:
  try:
    cost = float(input("Cost ($): ").strip().lstrip("$"))
    if cost > 0: break
  except ValueError:
    print("Enter a valid positive number.")
    expenses.append({"item": item, "cost": cost})
    save_expenses(expenses)

def main():
  expenses = load_expenses()
# Interactive menu loop here...
if __name__ == "__main__":
  main()
