from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.children = children
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Instance must contain a tag")
        if self.children is None:
            raise ValueError("Object has no children")
        child_html = ""
        for child in self.children:
            child_html = child_html + child.to_html()
        return f"<{self.tag}>{child_html}</{self.tag}>"
        
    def props_to_html(self):
        finished_html = ""
        if self.props:
            for key, value in self.props.items():
                finished_html += f' {key}="{value}"'
        return finished_html
        