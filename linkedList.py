
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    
    def insert_end(self, data):
        
        if self.head is None: 
            self.insert_beginning(data)
            return        
        
        el = self.head
        
        while el:
            
            if el.next is None:
                
                node = Node(data, None)
                el.next = node
                break
                        

            el = el.next
            
    
    
    def insert_elements(self, arr): #This allows to insert an array
        
        for els in arr:
            self.insert_end(els)
            
    
    
    
    
    def remove_first(self): # O(1) complexity
        
        
        if self.head is None:
            print('The list is empty')
            return
                
        self.head = self.head.next

        
    
    def remove_last(self):
        
        if self.head is None:
            print('The list is empty')
            return
        
        
        el = self.head
        
        while el:
                    
            if el.next.next is None:
                el = el.next
                break
        
            el = el.next
            




    def insert_after(self, name, data):
        
        if self.head is None:
            print('The list is empty')
            return
            
        
        el = self.head
        
        while el:
            
            if el.data == name:
                
                node = Node(data, el.next)
                el.next = node
                
                
            
            el = el.next
        
            
            
    
    def remove(self, data):
        
        if self.head is None:
            return
        
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        
        el = self.head
        
        while el:
            
            if el.next.data == data:
                el.next = el.next.next
                break
                            
            
            el = el.next
        
        
    
    
   

    def print(self):

        if self.head is None:
            print('The list is empty')
            return

        el = self.head
        lstr = ''

        while el:

            lstr += str(el.data) + ' --> ' if el.next is not None else str(el.data)
                

            

            el = el.next

        print(lstr)
        

    
    
            


if __name__ == '__main__':

    ll = LinkedList()
    ll.insert_elements(['abacaxi', 'mango', 'strawberry'])
    ll.insert_end('pineapple')
    ll.insert_after('mango', 'grape')
    ll.remove('mango')
    ll.remove_last()
    ll.print()
 
