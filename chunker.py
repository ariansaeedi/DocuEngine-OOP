from models import Document


class TextChunker:
    def __init__(self,chunk_size:int=10,overlap:int=2):
        if overlap >= chunk_size:
            raise ValueError("مقدار overlap باید کمتر از chunk_size باشد!")
        
        self.chunk_size = chunk_size
        self.overlap = overlap
    
    def split(self,doc:Document)->list[Document]:
        words = doc._content.split()
        step = self.chunk_size - self.overlap
        chunks = []

        chunk_id = 0
        for i in range(0,len(words),step):
            chunked_words = words[i:i+self.chunk_size]
            chunk_text = ' '.join(chunked_words)
            chunk_doc = Document(chunk_text, chunk_id, source = f'doc_{doc.doc_id}_chunk')
            chunks.append(chunk_doc)
            chunk_id += 1
            
        return chunks