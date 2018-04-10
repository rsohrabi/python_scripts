#decorators

def printlog(func):
  def wrapper(*arg, **kwargs):
    print('CALLING: {}'.format(func.__name__))
    return func(*arg, **kwargs)
  return wrapper

@printlog
def foo(x):
  print(x + 2)
  
@printlog
def baz(x, y):
  print(x ** y)


def running_average(func):
  data = {"total": 0, "count" : 0}
  def wrapper(*args, **kwargs):
    val = func(*args, **kwargs)
    data["total"] += val
    data["count"] += 1
    print("Average of {} so far: {:.01f}".format(
      func.__name__, data["total"] / data["count"]))
    return func(*args, **kwargs)
  return wrapper

@running_average
def foo(z):
  return z * 2
