

def faculty(k):
  if k < 0:
    raise ValueError

  if k == 0:
    return 1
  return k * faculty(k-1)

try:
    print(faculty(-1))
except ValueError:
    print("Invalid Input!")

# print(faculty(0))
# print(faculty(1))
# print(faculty(2))
# print(faculty(3))
# print(faculty(4))

