import json, csv, random
from pprint import pprint

csv_data = []

with open("task_3_file", "r") as users_file:
    file_data = users_file.read()
    json_data = json.loads(file_data)

#pprint(json_data)

users_data_csv = [("id", "name", "age", "phone")]
for i in json_data.keys():
    users_data_csv.append((i, *json_data[i], f"+375 (29) {random.randint(1000000, 9999999)}"))
#print(users_data_csv)


with open('users.csv', 'w') as csv_file:
    wr = csv.writer(csv_file)
    for user_inf in users_data_csv:
        wr.writerow(user_inf)

with open('users.csv', 'r') as csv_file:
    rr = csv.reader(csv_file)
    for user_info in users_data_csv:
        print(user_info)
