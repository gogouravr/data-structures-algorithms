class Node:
    def __init__(self,val,endHere = False):
        self.val = val
        self.endHere = endHere
        self.children = {}
       
class PrefixTree:
    def __init__(self):
        self.root = Node('0')

    def __insertRec(self,i,word,parentNode):
        if i == len(word):
            parentNode.endHere = True
            return
        # print(i,word[i],parentNode.val,parentNode.children)

        if word[i] not in parentNode.children:
            parentNode.children[word[i]] = Node(word[i])
        
        self.__insertRec(i+1,word,parentNode.children.get(word[i]))

    def __searchRec(self,word,parentNode, i=0):
        if not parentNode:
            return (False, False)
        # print('search',parentNode.val,parentNode.children)

        if len(word) == i:
            return (True, parentNode.endHere)

        return self.__searchRec(word,parentNode.children.get(word[i],None),i+1)    

    def insert(self, word: str) -> None:
        self.__insertRec(0,word,self.root)

    def search(self, word: str) -> bool:
        return self.__searchRec(word,self.root)[1]

    def startsWith(self, prefix: str) -> bool:
        return self.__searchRec(prefix,self.root)[0]
        
        