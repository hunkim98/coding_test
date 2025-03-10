class Node:
    char: str
    children: dict["Node"]
    # parent: "Node"
    parents: dict["Node"]

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.parents = {}

    def addChild(self, char):
        if self.children.get(char) is None:
            self.children[char] = Node(char)
        return self.children[char]

    def getChild(self, char):
        return self.children.get(char)


class WordDictionary:
    root: Node

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            child = curr.addChild(char)
            curr = child

        curr.addChild("")  # add an end node

    def search(self, word: str) -> bool:
        dot_locations = []

        min_char_int = ord("a")
        max_char_int = ord("z")

        for i in range(len(word)):
            char = word[i]
            if char == ".":
                dot_locations.append(i)

        does_exist = False

        if len(dot_locations) == 0:
            does_exist = self.findExact(word)

        elif len(dot_locations) == 1:
            for i in range(min_char_int, max_char_int + 1):
                candidate = list(word)
                candidate[dot_locations[0]] = chr(i)
                candidate = "".join(candidate)
                does_exist = self.findExact(candidate)
                if does_exist:
                    return does_exist

        elif len(dot_locations) == 2:
            for i in range(min_char_int, max_char_int + 1):
                for j in range(min_char_int, max_char_int + 1):
                    candidate = list(word)
                    candidate[dot_locations[0]] = chr(i)
                    candidate[dot_locations[1]] = chr(j)
                    candidate = "".join(candidate)
                    does_exist = self.findExact(candidate)
                    if does_exist:
                        return does_exist

        else:
            raise Exception()

        return does_exist

    def findExact(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if curr.children.get(char) is not None:
                curr = curr.children.get(char)
            else:
                return False
        if curr.children.get("") is not None:
            return True
        return False


if __name__ == "__main__":
    wd_1 = WordDictionary()
    wd_1.addWord("bad")
    wd_1.addWord("dad")
    wd_1.addWord("mad")
    assert wd_1.search("pad") == False  # return False
    assert wd_1.search("bad") == True  # return True
    assert wd_1.search(".ad") == True  # return True
    assert wd_1.search("b..") == True  # return True
