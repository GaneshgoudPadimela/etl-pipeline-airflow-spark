import json
def load_summary(summary, path='daily_summary.json'):
    with open(path, 'w') as f: json.dump(summary, f, indent=2)
    return path
