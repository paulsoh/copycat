import os
from PyInquirer import prompt, print_json

questions = [
    {
        'type': 'input',
        'name': 'dest_hostname',
        'message': 'Destination username/hostname (ex: linewalks@192.168.0.32)',
        'default': 'linewalks@192.168.0.32',
    },
    {
        'type': 'input',
        'name': 'source_path',
        'message': 'Path to folder to copy (ex: /usr/share/data)',
        'default': os.getcwd(),
    },
    {
        'type': 'input',
        'name': 'dest_path',
        'message': 'Path to folder to copy to (ex: /usr/share/data)',
        'default': '/home/',
    },
]

def get_answers():
    return prompt(questions)
