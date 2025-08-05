from calculator import add
from calculator import sub
from calculator import mult
from calculator import div

def main_calculator():
  x = int(input("Please enter a number"))
  y = int(input("Please enter another nunber"))
  sign = input("Please choose your sign: Add, Subtract, Multiply, Divide").lower()
  if sign == "add":
    print("Your result is :")
    add(x, y)
  elif sign == "subtract":
    print("Your result is :")
    sub(x, y)
  elif sign == "multiply":
    print("Your result is :")
  elif sign == "divide":
    print("Your result is :")
  else:
    print("Please try again")

if __name__ == "__main_calculator__"
  main_calculator()
