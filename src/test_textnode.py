import unittest
from textnode import TextNode
from textnode import TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a banana", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a google link", TextType.BOLD, "wwww.google.com")
        node2 = TextNode("This is a google link", TextType.BOLD, "wwww.google.com")
        self.assertEqual(node, node2)
    
    def test_not_eq2(self):
        node = TextNode("This is a google link", TextType.BOLD, "wwww.google.com")
        node2 = TextNode("This is a google link", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.italics.gov")
        node2 = TextNode("This is a text node", TextType.ITALIC, "www.italics.gov")
        self.assertEqual(node, node2)

    def test_not_eq3(self):
        node = TextNode("This is a text node", TextType.ITALIC, "www.italics.gov")
        node2 = TextNode("This is a text node", TextType.TEXT, "www.italics.gov")
        self.assertNotEqual(node, node2)

    def test_not_eq4(self):
        node = TextNode("This is a google link", TextType.CODE, "wwww.butter.com")
        node2 = TextNode("Just a savage amount of butter", TextType.CODE, "wwww.butter.com")
        self.assertNotEqual(node, node2)

    def test_not_eq5(self):
        node = TextNode("Visit the docs", TextType.LINK, "https://example.com/docs")
        node2 = TextNode("Visit the docs", TextType.LINK, "https://example.com/guide")
        self.assertNotEqual(node, node2)
    
    #TextNode to HTMLNode
class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")


if __name__ == "__main__":
    unittest.main()