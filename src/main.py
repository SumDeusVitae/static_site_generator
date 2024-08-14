from textnode import TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode
def main():
    x = TextNode('This is a text node','bold')
    y = TextNode('This is a text node','bold')

    print(x)
    print(x == y)
main()

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode(tag='b',value=text_node.text)
        case "italic":
            return HTMLNode(tag = 'i', value= text_node.text)
        case "code":
            return HTMLNode(tag="code", value= text_node.text)
        case "link":
            return HTMLNode(tag="a", value= text_node.text, props = {"href" : text_node.url})
        case "image":
            return HTMLNode(tag="img", value = "", props= {"src":text_node.url,"alt":text_node.text})
        case _:
            raise ValueError("Wrong text_type")


    