from binary_tree import *

class BinarySearchTree(BinaryTree):
    def insert(self, data):
        #삽입할 노드 생성 및 데이터 설정
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()
        #루트 노드가 없을 때
        if cur == None:
            self.set_root(new_node)
            return

        #삽입할 노드의 위치를 찾아 삽입
        while True:
            #삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < self.get_node_data(cur):
                #왼쪽 자식 노드 존재하면
                if self.get_left_sub_tree(cur):
                    cur = self.get_left_sub_tree(cur)
                #존재하지 않으면 노드 삽입
                else:
                    self.make_left_sub_tree(
                        cur, new_node)
                    break
            #삽입할 데이터가 현재 노드 데이터보다 클 때
            elif data > self.get_node_data(cur):
                #오른쪽 자식 노드 존재하면
                if self.get_right_sub_tree(cur):
                    cur = self.get_right_sub_tree(cur)
                #존재하지 않으면 노드 삽입
                else:
                    self.make_right_sub_tree(
                        cur, new_node)
                    break

    def search(self, target):
        cur = self.get_root()
        
        while cur != None:
            #target 데이터를 찾으면 노드를 반환
            if target == self.get_node_data(cur):
                return cur
            #target 데이터가 노드 데이터보다 작으면
            #왼쪽 자식 노드로 이동
            elif target < self.get_node_data(cur):
                cur = self.get_left_sub_tree(cur)
            #target 데이터가 노드 데이터보다 크면
            #오른쪽 자식 노드로 이동
            elif target > self.get_node_data(cur):
                cur = self.get_right_sub_tree(cur)
        return cur
    
    #리프 노드일 때
    def remove_leaf(self, parent, del_node):
        #삭제 노드가 루트 노드일 때
        if del_node == self.get_root():
            self.set_root(None)
            return del_node

        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, None)
        else:
            self.make_right_sub_tree(parent, None)
            
        return del_node  
    
    #자식 노드가 하나일 때
    def remove_one_child(self, parent, del_node):
        #삭제 노드가 루트 노드일 때
        if del_node == self.get_root():
            if self.get_left_sub_tree(del_node):
                self.set_root(
                    self.get_left_sub_tree(del_node))
            else:
                self.set_root(
                    self.get_right_sub_tree(del_node))

            return del_node
        
        #삭제 노드의 자식 노드를 받아와서 
        del_child = None
        if self.get_left_sub_tree(del_node):
            del_child = \
            self.get_left_sub_tree(del_node)
        else:
            del_child = \
            self.get_right_sub_tree(del_node)

        #삭제 노드의 부모 노드에 연결
        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, del_child)
        else:
            self.make_right_sub_tree(parent, del_child)

        return del_node

    #자식 노드가 두 개일 때
    def remove_two_children(self, del_node):
        #루트 노드를 실제로 삭제하는 게 아니므로
        #루트 노드에 대한 경우가 필요 없다.

        rep_parent = del_node
        #삭제 노드의 왼쪽 서브 트리에서
        replace = \
        self.get_left_sub_tree(rep_parent)

        #가장 큰 데이터를 가진 노드를 찾는다.        
        while self.get_right_sub_tree(replace):
            rep_parent = replace
            replace = \
            self.get_right_sub_tree(replace)

        #삭제 노드와 대체 노드의 데이터 교환
        temp_data = \
        self.get_node_data(replace)
        self.set_node_data(replace,
                    self.get_node_data(del_node))
        self.set_node_data(del_node, temp_data)

        #대체 노드에 왼쪽 서브 트리가 있는 경우
        if self.get_left_sub_tree(rep_parent) == replace:
            self.make_left_sub_tree(rep_parent,
                self.get_left_sub_tree(replace))
        else:
            self.make_right_sub_tree(rep_parent,
                self.get_left_sub_tree(replace))

        return replace    

    def remove(self, target):
        #삭제 노드를 찾는다.
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            #target이 존재하지 않는다.
            if del_node == None:
                return None

            if target == \
               self.get_node_data(del_node):
                break
            
            elif target < \
                 self.get_node_data(del_node):
                del_parent = del_node
                del_node = \
                self.get_left_sub_tree(del_node)
                
            elif target > \
                 self.get_node_data(del_node):
                del_parent = del_node
                del_node = \
                self.get_right_sub_tree(del_node)
                
        #삭제 노드가 리프 노드일 때
        if self.get_left_sub_tree(del_node) == None and \
           self.get_right_sub_tree(del_node) == None:
            return self.remove_leaf(del_parent, del_node)
        #삭제 노드의 자식 노드가 하나일 때
        elif self.get_left_sub_tree(del_node) == None or \
             self.get_right_sub_tree(del_node) == None:
            return self.remove_one_child(del_parent, del_node)
        #삭제 노드의 자식 노드가 두 개일 때
        else:
            return self.remove_two_children(del_node)  

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    #insert
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f = lambda x: print(x, end = '  ')
    #전위 순회
    bst.preorder_traverse(bst.get_root(), f)
    print("")
    
    #search
    print("searched data : {}".format(bst.search(8).data))

    #remove - 1 : 리프 노드일 때
    bst.remove(9)

    #remove - 2 : 자식 노드 하나일 때
    #bst.remove(8)

    #remove - 3: 자식 노드 두 개일 때
    #bst.remove(6)
    
    bst.preorder_traverse(bst.get_root(), f)


    
    
