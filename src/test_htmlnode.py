import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(tag = "h1", value = "hi", children = None, props = {"href": "https://www.google.com", "target": "_blank",})
        expected = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), expected)

    def test_values(self):
        node = HTMLNode("div", "zug zug",)

        self.assertEqual(node.tag, "div",)
        self.assertEqual(node.value, "zug zug",)
        self.assertEqual(node.children, None,)
        self.assertEqual(node.props, None,)

    def test_repr(self):
        node = HTMLNode("p", "lake", None, {"class": "primary"})

        self.assertEqual(node.__repr__(), "HTMLNode(p, lake, children: None, {'class': 'primary'})",)

if __name__ == "__name__":
    unittest.main()