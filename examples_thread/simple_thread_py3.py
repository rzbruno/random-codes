import threading

def f(id):
    print('thread function '+str(id))
    return

if __name__ == '__main__':
    for i in range(3):
        threading.Thread(target=f, args=(i,)).start()
