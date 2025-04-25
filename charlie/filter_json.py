"""Super quick script to filter some stuff in a JSON so I don't have to spend a billion years scrolling"""

import json

with open('osf-release/post-study-survey/user_study_data.json', 'r') as f:
    data = json.load(f) 

filtered_data = [
    {k: v for k, v in entry.items() if 'entered' in k}
    for entry in data
]

with open('filtered_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)