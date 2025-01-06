class HTMLNode():

    def  __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        return NotImplementedError("to_html method yet to be implemented")
    
    def props_to_html(self):
        result = ''
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
            return result

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"