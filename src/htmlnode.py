class HTMLNode:

    def HTMLNode(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementdError()
    
    def props_to_html(self):
        html = ""
        for prop, value in self.props.items:
            html += f" {prop}={value}"
        
        return html
