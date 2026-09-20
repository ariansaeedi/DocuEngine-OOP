from abc import ABC, abstractmethod



class Basesearchengine(ABC):
    def __init__(self):
        self.documents = []

    def add_document(self,doc):
        self.documents.append(doc)

    def add_documents(self,docs):
        self.documents.extend(docs)

    def __len__(self) ->int :
        return len(self.documents)
    
    @abstractmethod
    def search(self,query:str):
        pass
    
class SimpleKeywordSearch(Basesearchengine):
    def __init__(self):
        super().__init__()
    def search(self,query:str):
        if not query or not query.strip() :
            raise ValueError('query is empty')
        results =[]
        query_words = query.split()

        for doc in self.documents:
            for word in query_words:
                if word.lower() in doc.content.lower() and doc not in results:
                    results.append(doc)
        return results
    def __contains__(self, keyword:str) -> bool:
        found_docs = self.search(keyword)
        return len(found_docs) > 0

    