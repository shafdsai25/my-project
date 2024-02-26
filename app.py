import zipfile
import os
import chromadb

class SemanticSearch:
    def __init__(self, collection_name):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection(collection_name)

    def index_documents(self, folder_path):
        file_data = self.read_files_from_folder(folder_path)
        documents = []
        metadatas = []
        ids = []

        for index, data in enumerate(file_data):
            documents.append(data['content'])
            metadatas.append({'source': data['file_name']})
            ids.append(str(index + 1))

        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def search(self, query, n_results=10):
        results = self.collection.query(query_texts=[query], n_results=n_results)
        return results

    @staticmethod
    def read_files_from_folder(folder_path):
        file_data = []

        for file_name in os.listdir(folder_path):
            if file_name.endswith(".json"):
                with open(os.path.join(folder_path, file_name), 'r') as file:
                    content = file.read()
                    file_data.append({"file_name": file_name, "content": content})

        return file_data

# Define the paths
zip_path = "C:/Users/pakbo/Downloads/PA-Assignment/patent_jsons_ML Assignment.zip"
extract_path = "C:/Users/pakbo/Downloads/PA-Assignment/data"  # Change this to your desired extraction path
folder_path = "C:/Users/pakbo/Downloads/PA-Assignment/data/patent_jsons"  # Change this to your extracted data folder

# Extract only the 'patent_jsons' folder
def extract_folder(zip_path, folder_name, extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            if member.startswith(folder_name) and not member.endswith('/'):
                zip_ref.extract(member, extract_path)

extract_folder(zip_path, 'patent_jsons', extract_path)

# Initialize and index documents
search_service = SemanticSearch("semantic_collection")
search_service.index_documents(folder_path)

# Perform a search
results = search_service.search("processor", n_results=1)
print("Query Result:\n", results)

# Print the first 5 file names
print("\nFirst 5 File Names:")
for data in search_service.read_files_from_folder(folder_path)[:5]:
    print(data['file_name'])


from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')  # Get the query parameter from the URL
    if not query:
        return jsonify({'error': 'Query parameter is missing'}), 400

    results = search_service.search(query, n_results=10)  # Use your existing search_service

    # Format the results for better readability
    formatted_results = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        doc_content = json.loads(doc)  # Assuming the document content is a JSON string

        # Extracting information from the document
        formatted_doc = {
            'patent_number': doc_content.get('patent_number', 'N/A'),
            'title': doc_content.get('titles', [{}])[0].get('text', 'No title available'),
            'abstract': doc_content.get('abstracts', [{}])[0].get('paragraph_markup', 'No abstract available'),
            'publication_date': doc_content.get('publication_date', 'No date available'),
            'inventors': ', '.join([f"{inv.get('first_name', '')} {inv.get('last_name', '')}" for inv in doc_content.get('inventors', [])]),
            'assignees': ', '.join([asn.get('name', 'No name') for asn in doc_content.get('assignees', [])])
        }

        formatted_results.append(formatted_doc)

    return jsonify(formatted_results)

if __name__ == '__main__':
    app.run(debug=True, port=5005)


