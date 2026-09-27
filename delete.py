def  delete(self,data):
  if self.head is None:
    return
  if self.head.data==data:
    self.head=self.head.next
  cn=self.head
  while cn.next.next is not None:
    if cn.next.data==data:
      break
    cn=cn.next
  cn.next=cn.next.next

  li.delete

  def delAt(self,pos):
    if pos<0 or pos>self.length():
      print('invalid position')
      return
    if self.head is None:
      return
    if pos==0:
      self.head=self.head.next
      self.size-=1
      return
    cn=self.head
    ind=0
    while cn.next.next.next is not None:
      if ind+1==pos:
        break
      cn=cn.next
      ind+=1
      cn.next=cn.next.next
      self.size-=1
def  deleteall(self,data):
  if self.head is None:
    return
  if self.head.data==data:
    self.head=self.head.next
  cn=self.head
  while cn.next.next is not None:
    if cn.next.data==data:
      break
    cn=cn.next
  cn.next=cn.next.next
  