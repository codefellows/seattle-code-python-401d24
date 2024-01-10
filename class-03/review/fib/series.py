
cache = {}

def sum_series(n, primary=0, secondary=1):

  # check if we've done "the" work before
  key = (n, primary, secondary)

  cached_value = cache.get(key)

  if cached_value is not None:
    return cached_value

  # if primary time then return primary value
  if n == 0:
    return primary

  # if secondary time then return secondary value
  if n == 1:
    return secondary

  value = sum_series(n-1, primary, secondary) + sum_series(n-2, primary, secondary)

  cache[key] = value

  return value



# 0 1 1 2 ...
print("fibonacci", sum_series(25))

# # 2 1 3 4 ...
# print("lucas", sum_series(3, 2, 1))

# # 3 4 7 11 ...
# print("dominique", sum_series(3, 3, 4))

# If you had some requirement to keep the named functions then can still do with minimal work
def fibonacci(n):
  return sum_series(n)

def lucas(n):
  return sum_series(n, 2, 1)

def dominique(n):
  return sum_series(n, 3, 4)


