import json

def parse_json_to_separate_files(json_line):
    """Parse a single-line JSON and create separate JSON files for each key-value pair"""
    data = json.loads(json_line)
    
    for key, value in data.items():
        filename = f"{key}.json"
        with open(filename, 'w') as f:
            json.dump({key: value}, f, indent=2)
        print(f"Created {filename}")
        

if __name__ == "__main__":
    with open('./predictions.json', 'r') as f:
        for line in f:
            parse_json_to_separate_files(line.strip())