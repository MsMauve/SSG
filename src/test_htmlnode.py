import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode("h1", "Website Header", ["BodyNode", 'BodyNode2'],)
        result = node.props_to_html()
        self.assertEqual(result, "")

        
    def test_props_to_html_one_prop(self):
        node = HTMLNode("h1", "Website Header", ["BodyNode", 'BodyNode2'], {"id": "about-me"})
        result = node.props_to_html()
        self.assertEqual(result, ' id="about-me"')
        
    def test_props_to_html_multiple_props(self):
        node = HTMLNode("h1", "Website Header", ["BodyNode", 'BodyNode2'], {"id": "about-me", "class": "header-text"})
        result = node.props_to_html()
        self.assertEqual(result, ' id="about-me" class="header-text"')