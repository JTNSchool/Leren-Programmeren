# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr -1

def add(a: float, b: float) -> float:
  return a + b

def substract(a: float, b: float) -> float:
  return a - b

def multiply(a: float, b: float) -> float:
  return a * b

def divide(a: float, b: float) -> float:
  try:
    return a / b
  except ZeroDivisionError:
    return None

  

