import json

def get_json_file(json_file_name:str) -> str:
    try:
        with open(json_file_name, 'r') as f:
            data = json.loads(f.read())
        return data
    except Exception as ex:
        print(f"Error: {str(ex)}")


def write_csv(csv_file_name: str, data):
    try:
        with open(csv_file_name, 'w') as f:
            f.write(data)
    except Exception as ex:
        print(f'Error: {str(ex)}')

if __name__ == "__main__":
    data = get_json_file('D:\\practice\\25_projects\\json_file.json')
    output = ' | '.join([*data[0]])
    for obj in data:
        output += f'\n{obj["name"]} {obj["age"]}'
    
    write_csv("D:\\practice\\25_projects\\output.csv", output)