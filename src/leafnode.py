from htmlnode import HTMLNode
from textnode import *


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None,props)

        if hasattr(self, "children"):
            del self.children

        if self.value is None:
            raise ValueError


    def to_html(self):
        if self.tag is not None:
            return f"<{self.tag}{self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"

        return self.value

    def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)
        elif text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        elif text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url})
        elif text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)
        elif text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)
        elif text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        raise ValueError("Text node passed has no valid TextType.")