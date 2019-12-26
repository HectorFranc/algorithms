class Queue:
    def __init__(self, queueList=[]):
        self.queueList = queueList

    def enQueue(self, element):
        self.queueList.append(element)
