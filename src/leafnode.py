from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        elif self.tag is None:
            return f"{self.value}"
        else:
            props_string = ""
            if self.props:
                props_string = self.props_to_html()
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
    def props_to_html(self):
        finished_html = ""
        if self.props:
            for key, value in self.props.items():
                finished_html += f' {key}="{value}"'
        return finished_html