nums = 1,2,3,4,5

def do_squares(some_nums):
  # squares = []
  # for n in some_nums:
  #   squares.append(n**2)
  # return  squares

  return [n**2 for n in some_nums]

squares = do_squares(nums)

print(squares)





