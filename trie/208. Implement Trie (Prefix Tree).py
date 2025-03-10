class Node:
    char: str

    children: dict

    def __init__(self, char):
        self.char = char
        self.children = {}

    def add_child(self, char):
        if self.children.get(char) is not None:
            return self.children[char]
        else:
            child = Node(char)
            self.children[char] = child
            return child

    def get_child(self, char):
        if self.children.get(char) is not None:
            return self.children[char]
        else:
            return None


class Trie:
    root: Node

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        # dissect the word into characters
        curr = self.root
        for char in word:
            child = curr.add_child(char)
            # print(curr.char, curr.children)
            curr = child

        curr.add_child("")  # This is to signify that there is an end

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            child = curr.get_child(char)
            # print(child)
            if child is None:
                return False
            curr = child

        if curr.get_child("") is not None:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            child = curr.get_child(char)
            if child is None:
                return False
            curr = child
        return True


if __name__ == "__main__":
    t_1 = Trie()
    t_1.insert("apple")
    assert t_1.search("apple") == True
    assert t_1.search("app") == False
    assert t_1.startsWith("app") == True
    t_1.insert("app")
    assert t_1.search("app") == True
