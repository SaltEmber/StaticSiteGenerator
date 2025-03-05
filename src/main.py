from textnode import TextNode, TextType
def main():
    node = TextNode("Hello mister beef man.", TextType.NORMAL, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
