from threading import Thread, Lock

lock = Lock()
i = 0

def baller():
    while True:
        with lock:
            i += 1
     
            print(f'Reported - #{i}')
        
def ballin():
    while True:
        Thread(target=baller).Start()
     
while True:
    Thread(target=ballin).Start()
      
  
