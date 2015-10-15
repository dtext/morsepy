__author__ = 'dt'

class Leaf:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def append(self, left, right):
        self.left = Leaf(left)
        self.right = Leaf(right)

class MorseTree:
    def __init__(self):
        root = Leaf(None)
        root.append('E', 'T')
        
        root.left.append('I', 'A')
        root.right.append('N', 'M')

        root.left.left.append('S', 'U')
        root.left.right.append('R', 'W')
        root.right.left.append('D', 'K')
        root.right.right.append('G', 'O')

        root.left.left.left.append('H', 'V')
        root.left.left.right.append('F', None)
        root.left.right.left.append('L', None)
        root.left.right.right.append('P', 'J')
        root.right.left.left.append('B', 'X')
        root.right.left.right.append('C', 'Y')
        root.right.right.left.append('Z', 'Q')

        self.root = root

    def __decode_rec(self, seq, leaf):
        if len(seq) == 0:
            return leaf.val
        elif seq[0] == '.':
            return self.__decode_rec(seq[1:], leaf.left)
        else:
            return self.__decode_rec(seq[1:], leaf.right)

    def decode(self, seq):
        return self.__decode_rec(seq, self.root)

    def parse(self, morsestr):
        result = ""
        words = morsestr.split('/')
        for word in words:
            word = word.split(' ')
            for seq in word:
                result += self.decode(seq)
            result += ' '
        return result

m = MorseTree()
print(m.parse("... --- .../... --- ..."))