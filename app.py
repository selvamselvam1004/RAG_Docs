import streamlit as st
from base_line import App,retrieve_text

#### Streamlit Application
def main():
    st.title("PDF Query Application")
    
    # Upload file
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    st.write(uploaded_file)

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("temp_file.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Initialize the App with the file path
        app = App("temp_file.pdf")

        # Show extracted text
        st.subheader("Extracted Text:")
        
        # Input for query
        query = st.text_input("Enter your query:")
        
        if query:
            results = retrieve_text(query, app.vs, app.text, app.model)
            st.subheader("Query Results:")
            for idx, result in enumerate(results):
                st.write(f"{idx + 1}: {result}")

if __name__ == "__main__":
    main()