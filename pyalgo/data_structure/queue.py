class Queue:
    def __init__(self):
        self.elements = []


class PriorityQueue:
    def __init__(self, comparator):
        self.elements = []
        self.comparator = comparator

    def push(self, element):
        index = len(self.elements)
        self.elements.append(element)
        while index > 0:
            # if self.elements[index] < self.elements[index // 2]:
            if self.comparator(self.elements[index], self.elements[(index - 1) // 2]):
                # TODO: How to find such kind of problematic code effectively and exhaustively? By coverage test?
                self.elements[index], self.elements[(index - 1) // 2] = \
                    self.elements[(index - 1) // 2], self.elements[index]
            index //= 2

    def pop(self):
        size = len(self.elements)
        self.elements[0] = self.elements[size - 1]
        size -= 1
        self.elements.pop()
        index = 0
        while index <= size // 2 - 1:
            left = index * 2 + 1
            right = index * 2 + 2
            smallest = index
            # if self.elements[left] < self.elements[smallest]:
            if self.comparator(self.elements[left], self.elements[smallest]):
                smallest = left
            if right <= size - 1 and self.comparator(self.elements[right], self.elements[smallest]):
                # if right <= size - 1 and self.elements[right] < self.elements[smallest]:
                smallest = right
            if smallest != index:
                self.elements[smallest], self.elements[index] = \
                    self.elements[index], self.elements[smallest]
            else:
                break
            index = smallest

    def top(self):
        return self.elements[0]

    def make(self, elements: list):
        return 0

    def __repr__(self):
        size = len(self.elements)
        width = 1
        result = ''
        while 2 * width - 1 <= size:
            for i in range(0, width):
                # print('current: ', size, width, i)
                # if width - 1 + i >= size:
                #     break
                result += str(self.elements[width - 1 + i]) + ', '
            result += '\n'
            width *= 2
        for i in range(0, size - width + 1):
            result += str(self.elements[width - 1 + i]) + ', '
        result += '\n'
        return result


if __name__ == '__main__':
    priority_queue = PriorityQueue(lambda x_, y_: x_ < y_)
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

    for x in range(0, 8):
        priority_queue.pop()
        print(priority_queue)

    B = PriorityQueue(lambda x: x + 3)

    C = PriorityQueue(lambda x_, y_: x_ < y_)
    C.push(1)
    print(C)
    C.push(4)
    print(C)
    C.push(3)
    print(C)
    C.push(2)
    print(C)
