# Implementation of trie, prefix tree that stores string keys in tree. It is used for information retrieval.
# 

class TrieNode:
    def __init__(self):
        self.children = [None] *26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, letter):
        # return index value of character to be assigned in array
        return ord(letter) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def startsWith(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None

def main():
    keys = ["the","a","there","anaswe","any","by","their"]
    output = ["Not present in trie","Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} --{}-- {}".format("the","search",output[t.search("the")]))
    print("{} --{}-- {}".format("these","search",output[t.search("these")]))
    print("{} --{}-- {}".format("their","search",output[t.search("their")]))
    print("{} --{}-- {}".format("thaw","startsWith",output[t.startsWith("th")]))
    print("{} --{}-- {}".format("anyw","startsWith",output[t.startsWith("anyw")]))

if __name__ == "__main__":
    main()
