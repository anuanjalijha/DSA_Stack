class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    def __init__(self):
        self.__head = None 
        self.__count = 0 


    #Define data members and __init__()





    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        #Implement the getSize() function
        return self.__count



    def isEmpty(self) :
        return self.getSize()==0
        #Implement the isEmpty() function



    def push(self, data) :
        newNode = Node(data)
        newNode.next = self.__head   
        self.__head = newNode
        self.__count= self.__count+1
        #Implement the push(element) function



    def pop(self) :
        if self.isEmpty():
            return -1
        data=self.__head.data
        self.__head = self.__head.next 
        self.__count = self.__count-1
        return data
        #Implement the pop() function



    def top(self) :
        if self.isEmpty():
            return -1
        data = self.__head.data
        return data
        #Implement the top() function
        

