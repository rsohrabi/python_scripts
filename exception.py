###exception
##def check_except():
##  #raise ValueError
##  #raise LookupError
##  return
##
##try:
##  check_except()
##
##except ValueError as VE:
##  print("got value error exception")
##
##else:
##  print("hit else case of try")
##finally:
##  print("hit finally of try")

  
##def append_if_even(x, lst=None):
##  if lst is None:
##    lst = []
##  if x% 2 == 0:
##    lst.append(x)
##  return lst
##
##def append_if_even2(x, lst=None):
##  lst = [] if lst is None else lst
##  if x %2 == 0:
##    lst.append(x)
##  return lst
##import math
##def heron2(a,b,c,*, units="square meters"):
##  s = (a + b + c) / 2
##  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
##  return "{0} {1}".format(area, units)
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
def ignore0(e):
  return e[2].lower()
