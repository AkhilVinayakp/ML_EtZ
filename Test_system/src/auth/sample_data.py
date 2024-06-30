# the file is used to insert the sample data into db.
import os
from pymongo import MongoClient

# Read the connection URL and database/collection names from environment variables
mongo_url = os.getenv("MONGO_URL", "mongodb://Alioth.local")
db_name = os.getenv("DATABASE", "dev-db")
collection_name = os.getenv("COLLECTION_NAME", "dev-user-data")
print("configurations ", mongo_url, db_name, collection_name)

# Connect to MongoDB
client = MongoClient(mongo_url)
db = client[db_name]
collection = db[collection_name]
# Sample documents to insert
documents = [
    {"name": "John Doe", "password": "334@@wew"},
    {"name": "Jane Smith", "password": "334@@afgg"},
    {"name": "Alice Johnson", "password": "334@@asda"},
    {"name": "Bob Brown", "password": "334@@yghf"},
    {"name": "admin", "password": "admin123"},
]

# Insert documents
insert_result = collection.insert_many(documents)

# Output the inserted document IDs
print(f"Inserted document IDs: {insert_result.inserted_ids}")

# Optionally: Verify insertion by printing all documents in the collection
for doc in collection.find():
    print(doc)
