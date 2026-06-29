class HTMLNode():
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list["HTMLNode"] | None = None, 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        props_str: str = ""
        if self.props is None:
            return props_str
        copy_props: dict[str, str] = self.props.copy()
        sorted(copy_props)
        for key, value in copy_props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] | None = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("LeafNode value is None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
