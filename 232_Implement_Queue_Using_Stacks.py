
class MyQueue:
    def __init__(self):
        self.queue = []
        self.val = 0
    
    def push(self, x: int) -> None:
        self.queue.append(x)
    
    def pop(self) -> int:
        if not self.empty():
            return self.queue.pop(0)
    
    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]
    
    def empty(self) -> bool:
        return len(self.queue) == 0

print("Running test cases for MyQueue...")
myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2]
print(f"Peek at the front: {myQueue.peek()}")   # should return 1
print(f"Pop from the front: {myQueue.pop()}")      # should return 1, queue is now [2]
print(f"Is the queue empty? {myQueue.empty()}") # should return False

myQueue.push(3) # queue is: [2, 3]
print(f"Pop from the front: {myQueue.pop()}")      # should return 2, queue is now [3]
print(f"Pop from the front: {myQueue.pop()}")      # should return 3, queue is now []
print(f"Is the queue empty? {myQueue.empty()}") # should return True
print("Test cases finished.")
