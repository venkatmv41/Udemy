from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


def calculator():
  n1 = float(input("What is the first number  "))
  is_continue = True
  
  while is_continue:
    n2 = float(input("What is the next number  " ))
    operation_sym = input("choose one arithmetic operator to work on number ")
    calculation_function = operations[operation_sym]
    answer = calculation_function(n1, n2)
    print(f"{n1} {operation_sym} {n2} = {answer}")
    
    continue_calculation = input(f"Do you want to continue calculation with {answer} ? Type 'y' or 'n' ")
    if continue_calculation =="y":
      n1 = answer
    else:
      is_continue = False
      calculator()
   
calculator()
