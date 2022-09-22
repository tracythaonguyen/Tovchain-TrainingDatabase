from training_db import TrainingMongoDB

if __name__ == '__main__':
    training_db = TrainingMongoDB()

    # Create operations
    doc = {
        "address": "So 1 Dai Co Viet",
        "borough": "Hai Ba Trung",
        "cuisine": "Lau nuong",
        "grades": "One Star",
        "name": "Lau nuong Bach Khoa",
        "restaurant_id": "00000001"
    }
    # Task1: Insert one document
    training_db.insert_one_restaurant(doc)
    docs = [
        {"address": "So 2 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000002"},
        {"address": "So 3 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000003"},
        {"address": "So 4 Dai Co Viet", "borough": "Hai Ba Trung", "restaurant_id": "00000004"}
    ]
    # Task2: Insert many documents
    training_db.insert_many_restaurants(docs)

    # Read operations
    # Task3: Get all documents in restaurants collection.
    all_restaurants = training_db.get_all_restaurants()
    print("There are all restaurants:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task4: display the field restaurant_id, name, borough and cuisine
    # for all the documents in the collection restaurant
    fields = {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}
    all_restaurants = training_db.get_all_restaurants_somefield(fields)
    print("There are all restaurants with the field restaurant_id, name, borough and cuisine:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task5: display the field restaurant_id, name, borough and cuisine,
    # but exclude the field _id for all the documents in the collection restaurant
    fields = {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1, "_id": 0}
    all_restaurants = training_db.get_all_restaurants_somefield(fields)
    print("There are all restaurants with the field restaurant_id, name, borough and cuisine but exclude _id:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task6: display all the restaurant which is in the borough Bronx
    filters = {"borough": "Bronx"}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("There are all restaurants in the borough Bronx:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task7: display the first 5 restaurant which is in the borough Bronx
    all_restaurants = training_db.restaurants_col.find({"borough": "Bronx"}).limit(5)
    print("The first 5 restaurant which is in the borough Bronx")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task8: display the next 5 restaurants after skipping first 5 which are in the borough Bronx
    all_restaurants = training_db.restaurants_col.find({"borough": "Bronx"}).limit(5).skip(5)
    print("The next 5 restaurants after skipping first 5 which are in the borough Bronx")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task9: find the restaurants who achieved a score more than 90
    filters = {"grades": {"$elemMatch": {"score": {"$gt": 90}}}}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("There are all restaurants who achieved a score more than 90:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task10: find the restaurants that achieved a score, more than 80 but less than 100
    filters = {"grades": {"$elemMatch": {"score": {"$gt": 80, "$lt": 100}}}}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("There are all restaurants who achieved a score, more than 80 but less than 100:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task11: find the restaurants that do not prepare any cuisine of 'American' and
    # their grade score more than 70 and latitude less than -65.754168
    # no using $and
    filters = {"cuisine": {"$ne": "American "}, "grades.score": {"$gt": 70}, "address.coord": {"$lt": -65.754168}}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("There are all restaurants satisfying the conditions:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task12: find the restaurants which belong to the borough Bronx
    # and prepared either American or Chinese dish
    filters = {"borough": "Bronx", "$or": [{"cuisine": "American "}, {"cuisine": "Chinese"}]}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("There are all restaurants satisfying the conditions:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task13: find the restaurant Id, name, borough and cuisine for those restaurants
    # which belong to the borough Staten Island or Queens or Bronx or Brooklyn
    filters = {"borough": {"$in": ["Staten Island", "Queens", "Bronx", "Brooklyn"]}}
    fields = {"restaurant_id": 1, "name": 1,"borough": 1, "cuisine": 1}
    all_restaurants = training_db.get_all_restaurants_field(filters, fields)
    print("There are all restaurants satisfying the conditions:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task14: find the restaurant Id, name, borough and cuisine for those restaurants
    # which are not belonging to the borough Staten Island or Queens or Bronx or Brooklyn.
    filters = {"borough": {"$nin": ["Staten Island", "Queens", "Bronx", "Brooklyn"]}}
    fields = {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}
    all_restaurants = training_db.get_all_restaurants_field(filters, fields)
    print("There are all restaurants satisfying the conditions:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task15: find the restaurant Id, name, address and geographical location for those restaurants
    # where 2nd element of coord array contains a value which is more than 42 and up to 52
    filters = {"address.coord.1": {"$gt": 42, "$lte": 52}}
    fields = {"restaurant_id": 1, "name": 1, "address": 1, "coord": 1}
    all_restaurants = training_db.get_all_restaurants_field(filters, fields)
    print("There are all restaurants satisfying the conditions:")
    for restaurant in all_restaurants:
        print(restaurant)
    # Task16: to know whether all the addresses contains the street or not
    filters = {"address.street": {"$exists": "true"}}
    all_restaurants = training_db.get_all_restaurants_filter(filters)
    print("Test whether all the addresses contains the street or not:")
    for restaurant in all_restaurants:
        print(restaurant)

    # Update operations
    # Task17: Update one document with restaurant_id is "00000001"
    # Change field grades from "One Star" to "Five Star".
    training_db.update_one_restaurant()
    # Task18: Update many documents: "borough" from "Hai Ba Trung" to "Hanoi"
    training_db.update_many_restaurants()

    # Delete operations
    # Task19: Delete one document has id 00000001
    training_db.delete_one_restaurant("00000001")
    # Task20: Delete many documents have borough is Hanoi
    borough = "Hanoi"
    training_db.delete_many_restaurants(borough)
