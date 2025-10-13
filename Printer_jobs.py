# Task: Mini‑Project: Printer Jobs (FCFS)

# ---- Printer Job Simulation ----

class CircularQueue:
  def __init__(self, size):
    self.size = size
    self.a = [None] * size
    self.front = 0
    self.rear = -1
    self.count = 0
 
  def is_empty(self):
    return self.count == 0
 
  def is_full(self):
    return self.count == self.size
 
  def enqueue(self, x):
    if self.is_full():
      print("Overflow")
      return False
    self.rear = (self.rear + 1) % self.size
    self.a[self.rear] = x
    self.count += 1
    return True
 
  def dequeue(self):
    if self.is_empty():
      print("Underflow")
      return None
    val = self.a[self.front]
    self.front = (self.front + 1) % self.size
    self.count -= 1
    return val
  
  def front_val(self):
    if self.is_empty():
      return None
    return self.a[self.front]
 
  def to_list(self):
    # return logical order of elements from front, length = count
    res = []
    idx = self.front
    for _ in range(self.count):
      res.append(self.a[idx])
      idx = (idx + 1) % self.size
      return res

def run_printer_sim(jobs, capacity=8):
   q = CircularQueue(capacity)
   print("Incoming jobs:", jobs)
   for j in jobs:
     if not q.enqueue(j):
       print("Queue full, job dropped:", j) # simple handling
   serviced = []
   while not q.is_empty():
     serviced.append(q.dequeue())
   print("Serviced order:", serviced)
   return serviced

# demo
jobs = ["J1","J2","J3","J4","J5"]
serviced = run_printer_sim(jobs, capacity=4)