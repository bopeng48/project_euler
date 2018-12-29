# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

VALUE_TO_FIND =   1000

def is_multiple_three(num):
  return num % 3 == 0

def is_multiple_five(num):
  return num % 5 == 0

def find_sum(input_value):
  sum = 0
  for i in range(0,input_value):
    if is_multiple_three(i):
      sum += i
    elif is_multiple_five(i):
      sum += i
  return sum

print(find_sum(VALUE_TO_FIND))