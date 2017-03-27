

class Node:
    def __init__(self):
        self.num=None
        self.word=None
        self.child={}
        
class Trie:
    def __init__(self):
        self.root=Node()
        self.root.num=0
    
    def addstring(self, string,n):
        node=self.root
        for c in string:
            if c in node.child.keys():
                node=node.child[c]
            else:
                child=Node()
                n=n+1
                child.num=n
                child.word=c
                node.child[c]=child
                node=child
        return n
    
    def searchtext(self,text):
        node=self.root
        for i in text:
            #print i
            if node.child=={}:
                return True
            elif i in node.child.keys():
                #print node.child[i].num
                node=node.child[i]
            else:
                return False

    def show(self,file):
        node=self.root
        self.printnode(node,file)
        
    def printnode(self,node,file):
        
        if (node.num == None):
            return
        else:
            for c in node.child.keys():
                s= str(node.num)+"->"+ str(node.child[c].num)+":"+str(c)
                file.write(s)
                file.write("\n")
                self.printnode(node.child[c],file)