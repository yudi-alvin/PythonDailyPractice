# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  #can just use l to capture the list
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options