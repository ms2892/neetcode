from collections import defaultdict

from queue import Queue

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        adjList=defaultdict(list)
        for i in wordList:
            for j in range(len(i)):
                adjList[i[:j]+'*'+i[j+1:]].append(i)
        q=Queue()
        # q.put([beginWord,0])
        for j in range(len(beginWord)):
            q.put([beginWord[:j]+'*'+beginWord[j+1:],1])
            # adjList[beginWord[:j]+'*'+beginWord[j+1:]].append(beginWord)
        
        # print(adjList)
        # for i in adjList:
            # print(i,adjList[i])
        
        visitNode=set()
        visitNode.add(beginWord)
        # print(adjList)
        while(not q.empty()):
            # print(q)
            curr = q.get()
            print(curr)
            words = adjList[curr[0]]
            print(words)
            for child in words:
                if child==endWord:
                    return curr[1]
                if child not in visitNode:
                    print(child)
                    visitNode.add(child)
                    for j in range(len(child)):
                        q.put([child[:j]+'*'+child[j+1:],curr[1]+1])

        return 0
    
solution = Solution()

beginWord="hit"
endWord="cog"
wordList=["hot","dot","dog","lot","log","cog"]



print(solution.ladderLength(beginWord,endWord,wordList))