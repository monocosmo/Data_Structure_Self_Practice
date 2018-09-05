def test1():
  list = [1,2,3,4]
  test2(list, 5)
  return(list)

def test2(list, x):
  list.append(x)

print(test1())

def test3():
  # Note: need global in both test3 and test4
  global result
  result = 0
  test4(5)
  return(result)

def test4(x):
  global result
  result = x

print(test3())

result2 = 0

def test5(x):
  global result2
  result2 = x

test5(5)
print(result2)

# global makes variable static and cannot be used as param anymore.