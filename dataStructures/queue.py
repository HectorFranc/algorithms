class Queue:
    def __init__(self, queueList=[], maxElements=None):
        '''
        Queue creator
        - queueList: List (optional). Creates a queue with elements of provided list
        - maxElements: Number (optional). Max elements that queue can contain.
        '''
        self.queueList = queueList
        self.maxElements = maxElements

    def enQueue(self, element):
        '''
        Adds an element to queue
        - element: Any. Element that is added
        '''
        if not self._queueIsFull():
            self.queueList.append(element)
        else:
            raise IndexError('Queue is full')

    def deQueue(self):
        '''
        Returns an element from queue
        '''
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
