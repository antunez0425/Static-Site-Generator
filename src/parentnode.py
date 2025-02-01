from leafnode import LeafNode
from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("Tag cannot be None")
        if children is None:
            raise ValueError("Children cannot be None")


        super().__init__(tag, None, children, props)

    def to_html(self):
        html = ""
        for child in self.children:
            html += child.to_html()

        return html