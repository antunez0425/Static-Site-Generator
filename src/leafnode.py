from htmlnode import HTMLNode


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