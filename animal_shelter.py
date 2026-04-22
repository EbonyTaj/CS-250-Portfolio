from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD operations for the Grazioso Salvare animal shelter database."""

    def __init__(self, username, password):
        """Initialize MongoDB connection using provided credentials."""
        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@localhost:27017/?authSource=aac"
            )
            self.database = self.client["aac"]
            self.collection = self.database["animals"]
        except PyMongoError as e:
            print(f"Connection error: {e}")

    def create(self, data):
        """Insert a document into the collection."""
        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print(f"Create error: {e}")
                return False
        print("Create error: data parameter is empty.")
        return False

    def read(self, query):
        """Read documents and return them as a list."""
        try:
            results = self.collection.find(query)
            return list(results)
        except PyMongoError as e:
            print(f"Read error: {e}")
            return []

    def update(self, query, new_values):
        """Update documents and return number modified."""
        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except PyMongoError as e:
                print(f"Update error: {e}")
                return 0
        print("Update error: query or new values are empty.")
        return 0

    def delete(self, query):
        """Delete documents and return number deleted."""
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"Delete error: {e}")
                return 0
        print("Delete error: query parameter is empty.")
        return 0