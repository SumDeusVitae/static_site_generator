from textnode import TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode
def main():
    x = TextNode('This is a text node','bold')
    y = TextNode('This is a text node','bold')

    print(x)
    print(x == y)
main()

