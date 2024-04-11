from HuffmanTree import *

class HuffmanCoder:
    def __init__(self, input_file, output_tree_file, output_code_file):
        self.input_file = input_file
        self.output_tree_file = output_tree_file
        self.output_code_file = output_code_file
        self.char_weights = self.read_file_data()
        self.tree = []
        self.codes = {}
        self.length = 0

    def read_file_data(self):
        with open(self.input_file, "rb") as f:
            bytes = f.read()
        char_weights = {}
        for b in bytes:
            char_weights[b] = char_weights.get(b, 0) + 1
        return char_weights

    def select(self, nodes, n):
        s1 = s2 = -1
        for i in range(n+1):
            if nodes[i].parent == -1:
                if s1 == -1 or nodes[i].weight < nodes[s1].weight:
                    s2 = s1
                    s1 = i
                elif s2 == -1 or nodes[i].weight < nodes[s2].weight:
                    s2 = i
        return s1, s2

    def build_huffman_tree(self):
        num_chars = len(self.char_weights)
        if num_chars == 0: 
            return []
        nodes = [HuffmanTreeNode(name) for name in self.char_weights.keys()]

        for i in range(num_chars):
            nodes[i].weight = self.char_weights[nodes[i].name]

        for i in range(num_chars, 2 * num_chars - 1):
            nodes.append(HuffmanTreeNode(name=None))
            s1, s2 = self.select(nodes, i - 1)
            nodes[i].lchild = s1
            nodes[i].rchild = s2
            nodes[s1].parent = nodes[s2].parent = i
            nodes[i].weight = nodes[s1].weight + nodes[s2].weight

        self.tree = nodes

    def huffman_coding(self):
        for i in range(len(self.tree)):
            code = ""
            cur = i
            parent = self.tree[cur].parent
            while parent != -1:
                if self.tree[parent].lchild == cur:
                    code = "0" + code
                else:
                    code = "1" + code
                cur = parent
                parent = self.tree[cur].parent
            if self.tree[i].name is not None:
                self.codes[self.tree[i].name] = code

        with open(self.input_file, "rb") as fr, open(self.output_code_file, "wb+") as fw:
            data = ""
            while True:
                c = fr.read(1)
                if not c:
                    break
                int_value = int.from_bytes(c, byteorder='big')
                data += self.codes.get(int_value, "")
            self.length = len(data)
            if r := self.length % 8:
                data += "0"*(8-r)
            b = bytes([int(data[i:i+8], 2) for i in range(0, len(data), 8)])
            fw.write(b)

    def export_bit_length(self):
            with open(self.output_tree_file, "w+", encoding='utf-8') as f:
                f.write(f"{self.length}\n")
                for node in self.tree:
                    f.write(f"{node.name} {node.weight} {node.parent} {node.lchild} {node.rchild}\n")

    def Huffman_coding_main(self):
        self.build_huffman_tree()
        self.huffman_coding()
        self.export_bit_length()

if __name__ == "__main__":
    input_file = "server\\src\\Journal\\Journal.txt"
    output_tree_file = "server\\src\\Journal\\hfmTree.txt"
    output_code_file = "server\\src\\Journal\\hfmzip.zip"
    
    huffman_coder = HuffmanCoder(input_file, output_tree_file, output_code_file)
    huffman_coder.Huffman_coding_main()