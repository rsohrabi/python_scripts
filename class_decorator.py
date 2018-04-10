#class_decorator
class Prefixer:
  def __init__(self, prefix):
    self.prefix = prefix
  def __call__(self, message):
    return self.prefix + message
