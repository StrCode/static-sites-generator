from textnode import TextNode, split_nodes_delimiter, text_type_code, text_type_text


def main():
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(new_nodes)


main()
