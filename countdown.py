import time
n=10
while n>0:
      print(n, flush=True)
      time.sleep(1)
      n-=1
print("Blastoff!",flush=True)

s = "Tenochtitlan"
index = 0 
while index < len(s):
    index += 1 
    print(s[:index])

x = "abracadabra"
position = len(x)
while position > 0:
      position -= 1
      print(x[position:])

        

