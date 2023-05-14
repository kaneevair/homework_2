import json
import csv

from files import CSV_FILE_PATH
from files import JSON_FILE_PATH


with open(CSV_FILE_PATH) as f:
    data_books = []
    books_list = csv.DictReader(f)
    for row in books_list:
        book_dict = {
            "title": row['Title'],
            "author": row['Author'],
            "pages": row['Pages'],
            "genre": row['Genre']
        }
        data_books.append(book_dict)


with open(JSON_FILE_PATH, 'r') as json_file:
    data_users = []
    users_list = json.load(json_file)
    for user in users_list:
        user_dict = {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": []
        }
        data_users.append(user_dict)

for i in range(len(data_users)):
    if len(data_books) == 0:
        break
    iteration = data_books.pop(0)
    data_users[i]['books'].append(iteration)


with open('../files/reference.json', 'w') as f:
    json.dump(data_users, f, indent=4)
    f.writelines([])
