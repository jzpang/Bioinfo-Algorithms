'''
Function:
    generate a suffic tree from a trie of target sequence
Input:
    a file containing target sequence
Output:
    a file with the edge lables of suffix tree of input sequence
Run:
    python suffixtree.py input_file output_file
'''

import sys

class Node:
    def __init__(self):
        self.num=None #position of a word in sequence
        self.word=None #word
        self.child={}  #store all children from Node
        self.lable=None #start position of a whole substring(path)
        self.length=None #length of substring(path)

class Trie:
    def __init__(self):
        self.root=Node()
        self.root.num=0
        self.root.length=0
    
    #add a new string in trie
    def addstring(self, string,n):
        node=self.root
        lable=n
        for c in string:
            if c in node.child.keys():
                node=node.child[c]
            else:
                child=Node()
                node.child[c]=child               
                #n=n+1
                child.num=n
                child.word=c               
                node=child
            n=n+1
        if node.child=={}:
            node.lable=lable
    
    #find if text match the pattern in trie
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

    #show the word of all node in trie
    def show(self,file):
        node=self.root
        self.printnode(node,file)
        
    def printnode(self,node,file):
        
        if (node.child=={}):
            return
        else:
            for c in node.child.keys():
                file.write(c)
                file.write("\n")
                self.printnode(node.child[c],file)

#generate suffix tree from trie
def suffixTree(trie):
    node=trie.root
    trie=findTree(trie,node)
    return trie

def findTree(trie,node):  
    trie=findNonBranchingPath(trie,node)
    if node.child !={}:
        for c in node.child.keys(): 
            trie=findTree(trie,node.child[c])  
    return trie


#return trie that all path starting from node is non-branching 
def findNonBranchingPath(trie,node):
    if node.child !={}:
        for c in node.child.keys():

            if node.child[c].child !={}:
                if len((node.child[c]).child.keys())>1:
                    node.length=1
                elif len((node.child[c]).child.keys())==1:
                    path=[]
                    orinode=node
                    node=node.child[c]
                    path.append(c)
                    while len(node.child.keys())==1:
                        for j in node.child.keys():
                            node=node.child[j]
                            path.append(j)
                    node.word="".join(path)
                    node.length=len(node.word)
                    #for j in orinode.child.keys():
                    orinode.child.pop(c)
                    orinode.child[node.word]=node
                    node=orinode
                else:
                    node.length=1
            else:
                node.length=1

    else:
        return trie
            
    return trie


#get target sequence from input file
def getsequences(file):
    f=open (file, "r")
    seq=[]
    s=f.readline()
    s=s.strip()
    return s

#generate trie with input sequence
def getTrie(seq):
    trie=Trie()
    for i in range(0,len(seq)):
        s=seq[i:]
        trie.addstring(s,i)
    return trie


def main():
    file=sys.argv[1]
    seq=getsequences(file)
    trie=getTrie(seq)   
    out=sys.argv[2]
    f2=open(out,"w")
    tree=suffixTree(trie)
    tree.show(f2)

main()
