# from langchain_pinecone import PineconeVectorStore
# # from langchain_community import OpenAIEmbeddings, ChatOpenAI
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain.chains import RetrievalQA
# from langchain_community.document_loaders import DirectoryLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import os
# from dotenv import load_dotenv
# from pinecone import Pinecone
# from langchain_community.vectorstores import FAISS
# from typing import List, Optional
# import logging
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# class AskMyDocService:
#     def __init__(self, doc_path: str, openai_api_key: str, pinecone_api_key: Optional[str] = None,
#                  use_pinecone: bool = False):
#         logger.info("Initializing AskMyDocService")
#         self.doc_path = doc_path
#         self.openai_api_key = openai_api_key
#         self.pinecone_api_key = pinecone_api_key
#         self.use_pinecone = use_pinecone
#         self.embeddings = OpenAIEmbeddings(api_key=self.openai_api_key, model="text-embedding-ada-002")
#         self.llm = ChatOpenAI(api_key=self.openai_api_key, model="gpt-4o", temperature=0)
#         self.vector_store = None
#
#         self.setup_vector_store()
#         self.setup_qa_chain()
#
#     def setup_vector_store(self):
#         logger.info("Setting up vector store")
#         loader = DirectoryLoader(self.doc_path, glob="*.docx", use_multithreading=True)
#         docs = loader.load()
#         text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#         split_docs = text_splitter.split_documents(docs)
#         doc_texts = [doc.page_content for doc in split_docs]
#
#         if self.use_pinecone:
#             self.setup_pinecone_vector_store(split_docs)
#         else:
#             self.vector_store = FAISS.from_texts(doc_texts, self.embeddings)
#         logger.info("Vector store setup completed")
#
#     def setup_pinecone_vector_store(self, split_docs: List):
#         logger.info("Setting up Pinecone vector store")
#         if not self.pinecone_api_key:
#             raise ValueError("Pinecone API Key is required to use Pinecone Vector Store")
#
#         pc = Pinecone(api_key=self.pinecone_api_key, environment="us-east-1-aws")
#         index_name = "pinecone-chatbot"
#         if index_name not in pc.list_indexes().names():
#             pc.create_index(index_name, dimension=1536, metric="cosine", spec={"engine": "faiss"})
#         self.vector_store = PineconeVectorStore.from_documents(split_docs, self.embeddings, index_name=index_name)
#         logger.info("Pinecone vector store setup completed")
#
#     def setup_qa_chain(self):
#         logger.info("Setting up QA chain")
#         retriever = self.vector_store.as_retriever()
#         self.qa_chain = RetrievalQA.from_chain_type(llm=self.llm, chain_type="stuff", retriever=retriever)
#         logger.info("QA chain setup completed")
#
#     def query(self, query: str) -> str:
#         try:
#             logger.info(f"Processing query: {query}")
#             # Retrieve relevant documents using similarity search
#             retrieved_docs = self.vector_store.similarity_search(query)
#
#             if not retrieved_docs:
#                 logger.info("No relevant documents found")
#                 return "The answer to your query is not available in the document."
#
#             # Combine the retrieved documents into a single context
#             context = "\n\n".join([doc.page_content for doc in retrieved_docs])
#             # print('context:', context)
#             system_prompt = (
#                 "Use the given context to answer the question. "
#                 "If the answer is not covered in the provided document, dont answer! say you don't know. "
#                 "Use 3 sentences maximum and keep the answer concise. "
#                 f"Context: {context}"
#             )
#
#             # Prepare the query with the system prompt
#             # Simplifies the workflow by handling both retrieval and generation in a single chain.
#             response = self.qa_chain.invoke({"query": query, "context": system_prompt})
#
#             # response = self.llm.invoke([
#             #     {"role": "system", "content": system_prompt},
#             #     {"role": "user", "content": query}
#             # ])
#
#             # print('response:', response['choices'][0]['message']['content'])
#             # return response.content
#             # logger.info(f"Query processed successfully. Answer: {response['result']}")
#             return response['result']
#         except Exception as e:
#             logger.error(f"An error occurred: {e}")
#             return f"An error occurred: {e}"
#
#
# def main():
#     doc_path = "data"
#     load_dotenv(override=True)
#     openai_api_key = os.getenv("OPENAI_API_KEY")
#     pinecone_api_key = os.getenv("PINECONE_API_KEY")
#
#     logger.info('OpenAI API Key: %s', openai_api_key)
#     logger.info('Pinecone API Key: %s', pinecone_api_key)
#     doc_qa = AskMyDocService(doc_path, openai_api_key, pinecone_api_key, use_pinecone=True)
#
#     logger.info("Document loaded. You can now ask questions about its content.")
#
#     while True:
#         query = input("Enter your question (or type 'exit' to quit): ")
#         if query.lower() == 'exit':
#             break
#         answer = doc_qa.query(query)
#         print("Answer:", answer)
#
#
# if __name__ == "__main__":
#     main()


