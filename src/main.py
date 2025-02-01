from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode


def main():
    #text = TextNode("This is a test", TextType.BOLD, "http://www.google.com")

    #print(text)

    node = (HTMLNode
    (
        tag="div",
        value=None,
        children=[
            HTMLNode(tag="p", value="Hello, World!", props={"class": "text"}),
            HTMLNode(tag="img", props={"src": "image.png", "alt": "Sample Image"})
        ],
        props={"href": "https://www.google.com", "target": "_blank"}
    ))

    print(node)
    print(node.props_to_html())

    print(LeafNode("p", "This is a paragraph of text.").to_html())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
    print(LeafNode(None, "This is a test").to_html())




if __name__ == "__main__":
    main()