import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_a_eq_a(self):
        node = LeafNode("p", "hello", {"href": "https://www.google.com"})
        node2 = LeafNode("p", "hello", {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_b_eq_b(self):
        node = LeafNode("a", "world", {"href": "https://www.youtube.com"})
        node2 = LeafNode("a", "world", {"href": "https://www.youtube.com"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_a_not_b(self):
        node = LeafNode("p", "hello", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "world", {"href": "https://www.youtube.com"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()