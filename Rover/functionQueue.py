from queue import * #use dequeue to be able to schedule tasks to happen immediately?

q = Queue()

def addToQueue(call):
    q.put(call)

def mainQueue():
    while  not q.empty():
        call = q.get()
        function = call[0]
        args = call[1:]
        function(*args)

if __name__ == '__main__':
    def aFunction(arg):
        print(arg)
    print("start")
    q.put((aFunction, "henlo python"))
    q.put((aFunction, "hello you STINKY snake"))
    q.put((aFunction, "go eat a java ugly"))
    mainQueue()
    print("stop")
