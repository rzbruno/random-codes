import os

nodes = {
  'NT-Node-1' : '1.1.1.1',
  'NT-Node-2' : '8.8.8.8',
  'NT-Node-3' : '8.8.8.8',
  'NT-Node-4' : '8.8.8.8',
  'NT-Node-5' : '8.8.8.8',
  'NT-Node-6' : '8.8.8.8',
  'NT-Node-7' : '8.8.8.8',
  'NT-Node-8' : '8.8.8.8',
  'NT-Node-9' : '8.8.8.8'
}

up=[]
down=[]
for node in nodes:
   address = nodes.get(node)
   response = os.system("ping -c 1 " + address)
   if response == 0:
      up.append(node + ' is up!')
   else:
      down.append(node + ' is down!')

os.system('clear')

for node in up:
   print(node)

for node in down:
   print(node)
