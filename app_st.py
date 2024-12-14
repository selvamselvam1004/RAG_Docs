import streamlit as st
from base_line import PDFApp,retrieve_text
from Helpers.FileHelpers import save_uploaded_file,delete_uploaded_files
import os

def main():
    st.title("PDF Chat Interface")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    # delete_uploaded_files()
    if uploaded_file:
        filepath=save_uploaded_file(uploaded_file)


    
    if uploaded_file is not None:
        app=PDFApp(filepath)
        text1=app.extractText(app.filePath,app.fileFormatValStatus)
        app.generateEmbeddings(app.text,app.model)
        index=app.create_faiss_index(app.embed)

        st.session_state["pdf_text"] =  "text" # Store text in session state for later use
        st.subheader("Extracted Text")
        st.text_area("PDF Content", value='text', height=300)

        # Chat interface to ask questions about the PDF
        st.subheader("Ask me anything about the PDF:")
        user_input = st.text_input("Type your question here...")

        if st.button("Submit"):
            # Here you can implement your logic to answer the questions
            # For this demonstration, we'll just show the input text
            
            if user_input:
                # result=retrieve_text(query,index,text1,app.model)
                response = f"You asked: {retrieve_text(user_input,index,text1,app.model)}\nCan I help with anything else?"
                st.text_area("Response", value=response, height=150)

if __name__ == "__main__":
    main()