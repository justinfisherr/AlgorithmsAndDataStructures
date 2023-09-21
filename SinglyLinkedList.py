class Node:
   def __init__(self,val=0,nextNode =None):
      self.val = val
      self.next = nextNode

class LinkedList:
   def __init__(self):
      self.head = Node()
      self.count = 0
   def add(self, val):
      curr = self.head.next
      if(curr == None):
         self.head.next = Node(val)
      else:
         while(curr.next):
            curr = curr.next
         curr.next = Node(val)
      self.count = self.count+1
   def print(self):
      curr = self.head.next
      if(curr == None):
         print("Empty List")
      else:
         while(curr):
            print(curr.val)
            curr = curr.next
   def insertAt(self, index, val):
      if(index < 0):
         print("INVALID INDEX")
      else:
         curr = self.head.next
         iter = 0
         #Stop if out of bounds or if iterations == index
         while(curr.next and iter != index):
            curr = curr.next
            iter = iter+1
         # if end
         if(curr.next == None):
            curr.next = Node(val)
         else:
            store = curr.next
            addedNode = Node(val,store)
            curr.next = addedNode
         self.count = self.count + 1
   def insertAtBeg(self,val):
      head = self.head.next
      if(head):
         self.head.next = Node(val,head)
      else:
         self.head.next = Node(val)
      self.count = self.count + 1
   #removes end
   def remove(self):
      if(self.count):
         curr = self.head.next
         prev = self.head
         while(curr.next):
            prev = curr
            curr = curr.next
         del curr
         prev.next = None
         self.count = self.count -1
   def removeAt(self, index):
      if(index > self.count-1): return print("ERROR, INDEX Out Of Bounds")
      if (self.count):
         if(index == 0):
            #New head will be old head's next
            head = self.head.next
            self.head.next = head.next
            self.count = self.count - 1
            del head
         elif(index == self.count-1):
            self.remove()
         else:
            curr = self.head.next
            prev = self.head
            iter = 0
            while (iter != index):
               iter += 1
               prev = curr
               curr = curr.next
           # at this point we are somewhere in the middle of the list. There exists
            # a previous node that needs its next updated
            prev.next = curr.next
            del curr
            self.count = self.count - 1
   def removeVal(self,val):
      if(self.count):
         curr = self.head.next
         index = 0
         while(curr and curr.val != val):
            curr = curr.next
            index +=1
         self.removeAt(index)

myList = LinkedList()
myList.add(5)
myList.print()





















