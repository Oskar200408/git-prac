from calculator import add
from calculator import sub
from calculator import div
from calculator import mult

def test_add():
  assert add(7, 3) == 10

def test_sub():
  assert sub(10, 5) == 5

def test_div():
  assert div(10, 5) == 2

def test_div_zero():
  assert div(10,0) is None

def test_mult():
  assert mult(5, 5) == 25


  
