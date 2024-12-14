import os

UPLOAD_DIR=os.path.realpath('docs')
print(UPLOAD_DIR)

def save_uploaded_file(uploaded_file):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)  # Create directory if it does not exist
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def delete_uploaded_files():
    if os.path.exists(UPLOAD_DIR):
        for filename in os.listdir(UPLOAD_DIR):
            file_path = os.path.join(UPLOAD_DIR, filename)
            os.remove(file_path)
