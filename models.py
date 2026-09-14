class Document:
    def __init__(self,content:str,doc_id:int,source:str='manual'):
        self.content = content
        self.doc_id=doc_id
        self.source = source
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self,value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError('متن سند نمی تواند خالی باشد.')
        self._content = value

    @classmethod
    def from_file(cls,filepath,doc_id):
        with open(filepath,'r') as f:
            text = f.read()
        return cls(text,doc_id,filepath)

    def __len__(self) -> int:
        return len(self._content)
    def __repr__(self) -> str:
        short_text = self._content[:30]+'...' if len(self._content) > 30 else self._content
        return f'document_id:{self.doc_id},len:{len(self)},text:{short_text}'
