class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]->{self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        return str(self.head)
    def leng(self): #длина списка
        count = 0
        a = self.head
        while a:
            count += 1
            a = a.next
        return count
    def max(self): #макс элемент
        maxi = 0
        a = self.head
        while a:
            if maxi < a.data:
                maxi = a.data
            a = a.next
        return maxi

    def otric(self): #есть ли отрицательный
        flag = 0
        a = self.head
        while a:
            if a.data < 0:
                flag = 1
                break
            a = a.next
        if flag == 1:
            return "Yes"
        else:
            return 'No'

    def delete(self,k): # Удалить из списка первый встретившийся элемент, равный k
        a = self.head
        if a:
            if a.data == k:
                self.head = a.next
                a = None
                return
        while a:
            if a.data == k:
                break
            c = a
            a = a.next
        if a == None:
            return
        c.next = a.next
        a = None

    def deleteall(self,k): # Удалить из списка все элемент, равный k
        a = self.head
        c = a
        if self.head.data == k:
            self.head = self.head.next
        while a:
            if a.data == k:
                c.next = a.next
            c = a
            a = a.next
        if a == None:
            return
        c.next = a.next
        a = None

    def deletehead(self): #Удаляет голову списка
        a = self.head
        c = a
        self.head = self.head.next
        while a:
            c = a
            a = a.next
        if a == None:
            return
        c.next = a.next
        a = None
















if __name__ == '__main__':
    linlist = LinkedList()
    node1 = Node(2)
    linlist.head = node1
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(linlist)
    print(linlist.leng())
    print(linlist.max())
    print(linlist.otric())
    linlist.delete(2)
    print(linlist)
    linlist.deleteall(2)
    print(linlist)
    linlist.deletehead()
    print(linlist)


