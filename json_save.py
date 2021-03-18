import json


class Container:
    def __init__(self, container_id, data):
        self.id = container_id
        self.data = data
        self.save_data = {f"{self.id}": [th.id for th in self.data]}

    def __str__(self):
        text = ""
        return text


class Thing:
    def __init__(self, thing_id):
        self.id = thing_id

    def __str__(self):
        text = ""
        return text


def save(objec):
    # 1 dumps
    json_obj = json.dumps(objec, indent=2)

    with open("json_data.json", 'w') as out:
        out.write(json_obj)

    # 2 dump (no s)
    # with open("json_data.json", 'a+') as out:
    #     # out.write('\n')
    #     json.dump(objec, out)


l = []
for i in range(3):
    l.append(Thing(f"cookie{i+1}"))


c1 = Container("cookie jar1", l)
c2 = Container("jar2", l)
c3 = Container("jar3", l)

# For saving one
# save(c1.save_data)

# To save a bunch
new_list = [c1.save_data, c2.save_data, c3.save_data]

save(new_list)

