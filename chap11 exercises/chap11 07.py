def dot_product(u, v):
  return sum(x*y for x,y in zip(u,v))

def test(expr):
  print(expr)

test(dot_product([1, 1], [1, 1]) == 2)
test(dot_product([1, 2], [1, 4]) == 9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)