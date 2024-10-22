import json
import pandas as pd
from pathlib import Path

# get dir of this script
dir_project = Path(__file__).parent

# set paths
dir_source = dir_project.joinpath(r'data\sourcedata')
dir_root_bids =  dir_project.joinpath(r'data\bids')

# Sample participant data
data = {
    'participant_id': ['sub-1', 'sub-2'],
    'age': [25, 30],
    'sex': ['M', 'F'],
    'group': ['control', 'patient']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a .tsv file
df.to_csv(dir_root_bids.joinpath('participants.tsv'), sep='\t', index=False)

# Sample .json description for the participants.tsv columns
json_description = {
    "participant_id": {
        "Description": "Unique participant identifier"
    },
    "age": {
        "Description": "Age of the participant",
        "Units": "years"
    },
    "sex": {
        "Description": "Sex of the participant",
        "Levels": {
            "M": "Male",
            "F": "Female"
        }
    },
    "group": {
        "Description": "Group to which the participant belongs",
        "Levels": {
            "control": "Control participant",
            "patient": "Patient participant"
        }
    }
}

# Save the .json description to a file
with open(dir_root_bids.joinpath('participants.json'), 'w') as f:
    json.dump(json_description, f, indent=4)
    print(f'Created participants.tsv and participants.json in {dir_root_bids}')
