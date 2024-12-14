import os
import fitz
import faiss
from sentence_transformers import SentenceTransformer

class PDFApp:
    def __init__(self,filePath):
        """
        Init Functions helps to define a filepath and File Format check Validation.

        """
        self.filePath = filePath
        print(self.filePath)
        self.fileFormatValStatus = self.fileFormatCheck(self.filePath)
        self.text = self.extractText(self.filePath,self.fileFormatValStatus)
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
        self.embed = self.generateEmbeddings(self.text,self.model)
        self.vs = self.create_faiss_index(self.embed)
        

    def fileFormatCheck(self,filePath):
        if filePath is not None:
            _, fileExtension = os.path.splitext(self.filePath)
        else:
            return False
        if fileExtension =='.pdf':
            print(f"File format Valid {fileExtension}")
            return True
        else:
            print(f"File format not Valid{fileExtension}")
            return False
    
    def extractText(self,filePath,fileFormatValStatus):
        self.text = []
        if fileFormatValStatus:
            doc = fitz.open(self.filePath)
            for pageNum in range(len(doc)):
                page = doc.load_page(pageNum)
                self.text.append(page.get_text())

            return self.text
        else:
            return None
        
    def generateEmbeddings(self,text,model):
        self.text = text
        self.model=model
        embeddings = self.model.encode(self.text)
        return embeddings
    
    def create_faiss_index(self,embeddings):
        self.embeddings = embeddings
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(self.embeddings)
        return index

    
def retrieve_text(query, index, text, model):
    query_vector = model.encode([query])[0]
    D, I = index.search(query_vector.reshape(1, -1), k=5)
    return [text[i] for i in I[0]]
    

        
    

