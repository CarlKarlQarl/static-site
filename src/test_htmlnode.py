import unittest
from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()