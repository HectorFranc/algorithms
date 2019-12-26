class Queue:
    def __init__(self, queueList=[], maxElements=None):
        self.queueList = queueList
        self.maxElements = maxElements

    def enQueue(self, element):
        if not self._queueIsFull():
            self.queueList.append(element)
        else:
            raise IndexError('Queue is full')

    def deQueue(self):
        if not self._queueIsEmpty():
            element = self.queueList[0]
            self.queueList = self.queueList[1:]
            return element
        else:
            raise IndexError('Queue is empty')

    def _queueIsFull(self):
        if self.maxElements is not None:
            return len(self.queueList) < self.maxElements
        else:
            return False

    def _queueIsEmpty(self):
        return len(self.queueList) == 0
