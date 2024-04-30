from HuffmanTree import *

class HuffmanDecoder:
    def __init__(self, encoded_text, zip_path, decoder_path):
        self.encoded_text = encoded_text
        self.zip_path = zip_path
        self.decoder_path = decoder_path
        self.tree , self.i, self.length = self.reshape_huffman_tree()

    def reshape_huffman_tree(self):
        nodes = []
        i = 0
        with open(self.encoded_text, 'r') as f:
            length = int(f.readline())
            while True:
                b = f.readline().split()
                if not b:
                    break 
                if b[0] != 'None':
                    nodes.append(HuffmanTreeNode(name=int(b[0])))
                    nodes[i].weight = int(b[1])
                    nodes[i].parent = int(b[2])
                    nodes[i].lchild = int(b[3])
                    nodes[i].rchild = int(b[4])
                else:
                    nodes.append(HuffmanTreeNode(name = None))
                    nodes[i].weight = int(b[1])
                    nodes[i].parent = int(b[2])
                    nodes[i].lchild = int(b[3])
                    nodes[i].rchild = int(b[4])
                del b  
                i += 1   
        return nodes, i, length      

    def Huffman_Decoding(self):
        with open(self.zip_path, 'rb') as fr:
            data = fr.read()
            binstr = "".join(["{:08b}".format(char) for char in data])
            binstr = binstr[:self.length]
            i = self.i-1
            b = []
            for c in binstr:
                if c == '0' or c == '1':
                    if c == '0' and self.tree[i].lchild != -1:
                        i = self.tree[i].lchild
                    if c == '1' and self.tree[i].rchild != -1:
                        i = self.tree[i].rchild
                    if self.tree[i].lchild == -1 and self.tree[i].rchild == -1:
                        b.append(self.tree[i].name)
                        i = self.i-1
            b = bytes(b)
            with open(self.decoder_path, 'wb+') as fw:
                fw.write(b)

    def Huffman_Decoding_main(self):
        self.Huffman_Decoding()

if __name__ == '__main__':
    encoded_text = "server\\src\\Journal\\hfmTree.txt"
    zip_path = "server\\src\\Journal\\hfmzip.zip"
    decoder_path = "server\\src\\Journal\\hfmDecoder.txt"

    decoder = HuffmanDecoder(encoded_text, zip_path, decoder_path)
    decoder.Huffman_Decoding_main()