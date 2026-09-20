from chunker import TextChunker
from models import Document
from search import SimpleKeywordSearch , EmptyQueryError

doc = [
    'hi AI my forname is Arian',
    'hi my cername is Saeedi',
    'I love AI and programing'
]
doc = " ".join(doc)
main_doc = Document(doc,1,'My_self')

chunk_doc = TextChunker()
chunk_list = chunk_doc.split(main_doc)

search = SimpleKeywordSearch()
search.add(chunk_list)

print("arian" in search)

try:
    search.search("   ")  # کوئری خالی با فاصله
except EmptyQueryError as e:
    print(f"✅ ارور سفارشی با موفقیت فعال شد: {e}")

file_doc = Document.from_file('sample.txt',10)
print(file_doc)