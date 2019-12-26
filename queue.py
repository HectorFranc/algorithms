class Queue:
    def __init__(self, queueList=[]):
        self.queueList = queueList

    def enQueue(self, element):
        self.queueList.append(element)

    def deQueue(self):
        if len(self.queueList) != 0:
            element = self.queueList[0]
            self.queueList = self.queueList[1:]

            return element
        else:
            raise IndexError('Queue is empty')
