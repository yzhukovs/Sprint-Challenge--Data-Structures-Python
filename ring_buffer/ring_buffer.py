class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item #o(1)
    self.current += 1 
    if self.current == self.capacity:
      self.current = 0
#o(1)
    #pass

  def get(self):
    result = self.storage[0:self.current] + self.storage[self.current:self.capacity]
    result = [e for e in result if e != None]
    return result
    #pass