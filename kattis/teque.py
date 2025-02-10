class Teque:
    def __init__(self):
        self.front = []
        self.back = []

    def _balance(self):
        if len(self.front) > len(self.back) + 1:
            self.back=[self.front.pop()]+self.back
        elif len(self.back) > len(self.front):
            self.front.append(self.back.pop(0))

    def push_back(self, x):
        self.back.append(x)
        self._balance()

    def push_front(self, x):
        self.front=[x]+self.front
        self._balance()

    def push_middle(self, x):
        if len(self.front) > len(self.back):
            self.back=[x]+self.back
        else:
            self.front.append(x)

    def get(self, i):
        if i < len(self.front):
            return self.front[i]
        return self.back[i - len(self.front)]

    def __len__(self):
        return len(self.front) + len(self.back)

def main():
    n = int(input())
    teque = Teque()
    
    for _ in range(n):
        command, x = input().split()
        x = int(x)
        
        if command == "push_back":
            teque.push_back(x)
        elif command == "push_front":
            teque.push_front(x)
        elif command == "push_middle":
            teque.push_middle(x)
        elif command == "get":
            print(teque.get(x))

if __name__ == "__main__":
    main()