class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: object = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        
        reply: str = ''
        for prop in self.props:
            reply += f' {prop}="{self.props[prop]}"'
        return reply

    def __repr__(self) -> str:
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self,tag: str, value: str, props: dict = None) -> None:
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: object, props: dict = None) -> None:
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"