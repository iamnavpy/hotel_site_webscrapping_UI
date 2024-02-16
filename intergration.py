import pymongo
from unit_info import extract_unit_details

def store_data_in_mongodb(data):
    """Stores the given data in a MongoDB collection."""

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["chapter_db"]
    collection = db["unit_info"]

    collection.insert_many(data)

if __name__ == "__main__":
    url = 'https://chapterkingscross.prospectportal.global/Apartments/module/application_unit_info/'
    unit_details = extract_unit_details(url)
    store_data_in_mongodb(unit_details)
