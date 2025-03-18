class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""
        items = [f' {key}="{value}"' for key, value in self.props.items()]
        return "".join(items)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, n_tag, n_value, n_props = None):
        super().__init__(n_tag, n_value, props = n_props)
    def to_html(self):
        if not self.value and not self.value == "":
            raise ValueError
        # Returns raw string if nothing is provided
        if not self.tag:
            return self.value
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children = children, props = props)
    def to_html(self):
        if not self.tag:
            raise ValueError("Missing Tag")
        if not self.children:
            raise ValueError("Missing children")
#         '''
#             wrapper Tag
#             insert into wrapper tag all the children (to_html)
#             recurse

#             tag[nodeA, nodeB, tag[nodeC, nodeD]]
#             -we need to wrap all those iterated on in the tags of the parent
#               -check if the object is a parent (whether we need to make)
#         '''
        open_tag = f"<{self.tag}{super().props_to_html()}>"
        end_tag = f"</{self.tag}>"
        new_tag = open_tag
        for child in self.children:
            new_tag += child.to_html()
        return new_tag + end_tag
