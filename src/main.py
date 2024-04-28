from inline_markdown import split_nodes_link
from textnode import TextNode, text_type_text


def main():
    node = TextNode(
        "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
        text_type_text,
    )
    new_nodes = split_nodes_link([node])
    print(new_nodes)


main()
