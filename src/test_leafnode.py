import unittest

from htmlnode import LeafNode


class Test_LeafNode(unittest.TestCase):
    def renderTag(self):
        leaf = LeafNode("p", "This is a paragraph of text.", None, None)
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text</p>")

    def renderLinks(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}, None)
        self.assertEqual(
            leaf.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
