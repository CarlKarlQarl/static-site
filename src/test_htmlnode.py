import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode(tag="p", value="This is a text node", children=[], props={"class": "text"})
        node2 = HTMLNode(tag="p", value="This is a text node", children=[], props={"class": "text"})
        self.assertEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_not_eq1(self):
        node = HTMLNode(tag="p", value="This is a text node", children=[], props={"class": "text"})
        node2 = HTMLNode(tag="p", value="This is a text node", children=[], props={"class": "link"})
        self.assertNotEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_eq_multiple_props(self):
        node = HTMLNode(tag="a", value="link", children=[], props={"href": "https://example.com", "class": "nav-link"})
        node2 = HTMLNode(tag="a", value="link", children=[], props={"href": "https://example.com", "class": "nav-link"})
        self.assertEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_not_eq_multiple_props(self):
        node = HTMLNode(tag="a", value="link", children=[], props={"href": "https://example.com", "class": "nav-link"})
        node2 = HTMLNode(tag="a", value="link", children=[], props={"href": "https://different.com", "class": "nav-link"})
        self.assertNotEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_eq_empty_props(self):
        node = HTMLNode(tag="div", value="content", children=[], props={})
        node2 = HTMLNode(tag="div", value="content", children=[], props={})
        self.assertEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_not_eq_one_empty_props(self):
        node = HTMLNode(tag="div", value="content", children=[], props={})
        node2 = HTMLNode(tag="div", value="content", children=[], props={"id": "main"})
        self.assertNotEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))
    
    def test_eq_different_tag_same_props(self):
        node = HTMLNode(tag="p", value="text", children=[], props={"class": "para"})
        node2 = HTMLNode(tag="div", value="text", children=[], props={"class": "para"})
        self.assertEqual(HTMLNode.props_to_html(node), HTMLNode.props_to_html(node2))

    def test_tag_equal_and_not_equal(self):
        n1 = HTMLNode(tag="span", value="x", children=[], props={})
        n2 = HTMLNode(tag="span", value="y", children=[], props={})
        n3 = HTMLNode(tag="strong", value="x", children=[], props={})
        self.assertEqual(n1.tag, n2.tag)
        self.assertNotEqual(n1.tag, n3.tag)

    def test_value_equal_and_not_equal(self):
        n1 = HTMLNode(tag="p", value="hello", children=[], props={})
        n2 = HTMLNode(tag="p", value="hello", children=[], props={})
        n3 = HTMLNode(tag="p", value="world", children=[], props={})
        self.assertEqual(n1.value, n2.value)
        self.assertNotEqual(n1.value, n3.value)

    def test_children_equal_and_not_equal(self):
        child1 = HTMLNode(tag="em", value="a", children=[], props={})
        child2 = HTMLNode(tag="strong", value="b", children=[], props={})
        a = HTMLNode(tag="div", value="", children=[child1, child2], props={})
        b = HTMLNode(tag="div", value="", children=[child1, child2], props={})
        c = HTMLNode(tag="div", value="", children=[child2, child1], props={})
        d = HTMLNode(tag="div", value="", children=[child1], props={})
        self.assertEqual(a.children, b.children)
        self.assertNotEqual(a.children, c.children)
        self.assertNotEqual(a.children, d.children)

    def test_props_field_and_props_to_html(self):
        p1 = {"id": "x", "class": "c"}
        p3 = {"id": "y", "class": "c"}
        n1 = HTMLNode(tag="a", value="link", children=[], props=p1)
        n3 = HTMLNode(tag="a", value="link", children=[], props=p3)
        # dicts with same keys/values compare equal
        self.assertNotEqual(n1.props, n3.props)
        self.assertNotEqual(n1.props_to_html(), n3.props_to_html())

    #LeafeNode tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    #ParentNode tests
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()