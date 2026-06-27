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