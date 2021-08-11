class Node:
  def __init__(self,value ):
    self.value = value 
    self.next = None
  
  def __str__(self):
    return str(self.value)
  

class LinkedList:
    def __init__(self):
      self.head = None
    
    def __str__(self):
      string = ""
      current = self.head
      while current:
        string += f"{current.value} ->"
        current = current.next
      string += "None"
      return string

def rever_k_groups(ll,k):
  dummy = Node(0) 
  dummy.next  = ll.head 
  prev_group = dummy
  
  while True:
    kth = get_kth(prev_group, k)

    if not kth:
      break

    next_group = kth.next 
		
		#reverse the group
    prev, curr = kth.next, prev_group.next 

    while curr!= next_group:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    
    temp = prev_group.next
    prev_group.next= kth
    prev_group = temp
  return dummy.next


def get_kth(curr, k):
	while curr and k > 0: 
		curr = curr.next 
		k -= 1 
	return curr 

def reverseKGroup(head, k):
    if not head or k < 2:
        return head
    cursor = head
    prev = head
    temp = None
    i = 0
    while i < k and cursor:
        cursor = cursor.next
        i += 1
    if i == k:
        cursor = reverseKGroup(cursor, k)
        while i > 0: # 2, 1 
            temp = prev.next # 2,3
            prev.next = cursor # 1 -> 3, 2-> 1 -> 3
            cursor = prev # 1,2
            prev = temp # 2,3
            i -= 1
        prev = cursor
    return prev

if __name__ == '__main__':

  ll = LinkedList()
  ll2 = LinkedList()
  node = Node(1)
  node2 = Node(1)
  ll.head = node
  node.next = Node(2)
  node.next.next = Node(3)
  node.next.next.next = Node(4)
  node.next.next.next.next = Node(5)

  ll2.head = node2
  node2.next = Node(2)
  node2.next.next = Node(3)
  node2.next.next.next = Node(4)
  node2.next.next.next.next = Node(5)

  print(ll)
  ll_r = LinkedList()
  ll2_r = LinkedList()
  
  ll_r.head = reverseKGroup(ll2.head,2)
  ll2_r.head = rever_k_groups(ll,2)

  print(ll2_r)
  print(ll_r)