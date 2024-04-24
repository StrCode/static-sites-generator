from htmlnode import LeafNode, ParentNode


def main():

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    result = node.to_html()
    print(result)


main()
