from textnode import TextNode
from textnode import TextType

def main():
    test_textnode: TextNode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_textnode)

if __name__ == "__main__":
    main()