class Queue:
    def __init__(self):
        self.elements = []


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        index = len(self.elements)
        self.elements.append(element)
        while index > 0:
            if self.elements[index] < self.elements[index // 2]:
                self.elements[index], self.elements[index // 2] = \
                    self.elements[index // 2], self.elements[index]
            index //= 2

    def __repr__(self):
        size = len(self.elements)
        width = 1
        result = ''
        while width <= size // 2 + 1:
            for i in range(0, width):
                if width - 1 + i >= size:
                    break
                result += str(self.elements[width - 1 + i]) + ', '
            result += '\n'
            width *= 2
        return result


if __name__ == '__main__':
    priority_queue = PriorityQueue()
    priority_queue.push(10)
    priority_queue.push(9)
    priority_queue.push(1)
    priority_queue.push(8)
    priority_queue.push(2)
    priority_queue.push(7)
    priority_queue.push(3)
    priority_queue.push(6)
    priority_queue.push(5)
    priority_queue.push(4)
    print(priority_queue)
