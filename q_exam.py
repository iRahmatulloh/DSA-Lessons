# class Queue:
#     '''
# binary(num : int) -> str degan funksiya yarating va u berilgan qiymatdagi barcha raqamlarni queue yordamida binaryga aylantirishi kerak. Funksiyaning vazifasi string qaytarish.

# Input: binary(587)
# Output: "101 1000 111"

# Tushuntirish: 
# 5 ni binarga o'girsangiz 101 qaytadi
# 8 ni o'girsangiz 1000 qaytadi
# 7 ni o'girsangiz 111 qaytadi'''
# # Bu yeradgi kodni o'zgartirmang!


class MyQueue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.q[0]

    def rear(self):
        if self.is_empty():
            return None
        return self.q[-1]

    def size(self):
        return len(self.q)
    
    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.q.remove(self.front())
        return front

# Yechimni bu yerdan yozing
def find_bin(n : int) -> list:
    my = MyQueue()




find_bin(5)


