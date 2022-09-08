from os.path import exists
import json

data_dict: dict[int, tuple[str, int]] = {}

data_file = "task_3_file"
if exists(data_file):
    print("File exist")
else:
    data_dict[123456] = ("anton", 20)
    data_dict[234567] = ("ksusha", 14)
    data_dict[345678] = ("ira", 19)
    data_dict[456789] = ("natasha", 22)
    data_dict[567890] = ("dasha", 17)

    # with open(data_file, "w") as file_name:
    #     for item in data_dict.items():
    #         file_name.write(json.dumps(item))

    with open(data_file, "w") as file_name:
        file_name.write(json.dumps(data_dict))
