import unittest

from parentnode import ParentNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from unittest import TestCase

class TestParentNode(unittest.TestCase):

    def test_init(self):
        try:
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )

            self.assertIsNotNone(node)
        except Exception as e:
            self.fail()

