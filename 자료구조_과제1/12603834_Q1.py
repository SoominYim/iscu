# 문제 - 원형큐 이동하며 삭제하기

# 작성부분 (작성부분 외 나머지 수정불가)
# - 한번에 이동할 칸(1~3)을 입력받아 원형큐 이동하며 삭제

class Node:				                    
    def __init__ (self, elem, link=None):	
        self.data = elem 			        
        self.link = link			        

class CircularLinkedQueue:
    def __init__( self ):		
        self.tail = None			

    def isEmpty( self ): return self.tail == None 
    def clear( self ): self.tail = None		
    def peek( self ):				        
        if not self.isEmpty():			    
            return self.tail.link.data		

    def enqueue( self, item ):	
        node = Node(item, None)	
        if self.isEmpty() :		
           node.link = node		
           self.tail = node		
        else :				           
            node.link = self.tail.link	
            self.tail.link = node	   
            self.tail = node		   

    def dequeue( self ):
        if not self.isEmpty():
            data = self.tail.link.data		   
            if self.tail.link == self.tail :
                self.tail = None		               
            else:			                	
                self.tail.link = self.tail.link.link
            return data			

        
    def size( self ):
        if self.isEmpty() : return 0	
        else :				            
            count = 1			        
            node = self.tail.link   	
            while not node == self.tail:
                node = node.link        
                count += 1		        
            return count		        

    def display( self, msg='원형연결큐:' ):
        print(msg, end='')
        if not self.isEmpty() :
            node = self.tail.link		    
            while not node == self.tail :	
                print(node.data, end=' ')	
                node = node.link		    
            print(node.data, end=' ')		
        print()					            


def Q2_ds():
    hw_list=CircularLinkedQueue()
    while True :
        com_1 = input("연결 리스트 크기를 '숫자'로 입력하세요 - ")
        if com_1.isdigit()== True :
            list_sz=int(com_1)
            break
    for i in range(list_sz, 0, -1):
        k=i*i + i
        hw_list.enqueue(k)

    print('리스트가 다음과 같이 만들어졌습니다.\n')
    hw_list.display()
            
    while True :
        com_1 = input("\n한번에 이동할 칸을 숫자 1,2,3 중 입력하세요 - ")
        if (com_1.isdigit()==True) :
            ins_num=int(com_1)
            if(ins_num<1 or ins_num>3):
                print('숫자가 1,2,3 중 하나가 아닙니다.\n')
            else:    break
            
    while True :
        #작성부분 - ins_num 만큼 건너뛰면서 삭제하는 부분 작성

        move_cnt = 1
        while move_cnt < ins_num:
            hw_list.tail = hw_list.tail.link
            move_cnt += 1
        del_data = hw_list.dequeue()
        print(f'\n{del_data} 을(를) 리스트에서 삭제')

        ########
        hw_list.display()
        if(hw_list.isEmpty()):
            break

Q2_ds()

