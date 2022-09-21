#solution for 24.2 Practice, Python Data Structures, sololearn
#without using while

class CallCenter:
    def __init__(self):
      self.customers = []

#     def is_empty(self):
#       return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

#     def nextt(self):
#       return self.customers.pop()
    
    def name(self):
        return ['{}'.format(elm) for elm in self.customers]
           

c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

time=0
for i in c.name():
    if i == 'general':
        time +=5
    elif i == 'technical':
        time +=10 


print(time)
