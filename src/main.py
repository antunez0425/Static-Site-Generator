from textnode import TextNode, TextType


def main():
    text = TextNode("This is a test", TextType.BOLD, "http://www.google.com")

    print(text)



if __name__ == "__main__":
    main()