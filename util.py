import json, os, glob
from typing import List, Tuple, Dict, TypedDict, Optional, Union, Any

app_name : str = 'Soul Sanctum'
app_version : str = '2024/02/14'

current_directory : str = os.path.dirname(os.path.abspath(__file__))
model_directory : str = os.path.join(current_directory, 'models')
asset_directory : str = os.path.join(current_directory, 'static')
character_directory : str = os.path.join(current_directory, 'characters')
model_json_path : str = os.path.join(current_directory, 'models', 'models.json')

class CharacterCard(TypedDict):
    name : str
    gender : str
    language : str
    origin : str
    author : str
    system_template : str
    prompt_template : str
    description : str
    model : str
    path : str
    image : str
    index : int

class ModelCard(TypedDict):
    name : str
    file : str
    link : str

def get_character_data() -> Tuple[List[CharacterCard], List[ModelCard]]:
    character_json_list : List[str] = glob.glob(character_directory + '/*/character.json', recursive=True)
    if not character_json_list:
        print('No characters')
        exit()
    if not os.path.isfile(model_json_path):
        print('No models')
        exit()
    model_data : List[ModelCard] = []
    try:
        with open(model_json_path, 'r') as file:
            model_data = json.load(file)
    except Exception as exception:
        print(f'Error reading {model_json_path}: {str(exception)}')
        exit()
    character_list : List[CharacterCard] = []
    for index, json_file in enumerate(character_json_list):
        try:
            with open(json_file, 'r') as file:
                json_data : CharacterCard = json.load(file)
                json_data['path'] = os.path.dirname(json_file)
                json_data['index'] = index
                user_string : str = 'User'
                match json_data['language']:
                    case 'Spanish':
                        user_string = 'Usuario'

                json_data['prompt_template'] = user_string + ': {0}\n' + json_data['name'] + ': '

                system_template_file_path : str = os.path.join(json_data['path'], 'character.txt')
                with open(system_template_file_path) as system_template_file:
                    json_data['system_template'] = system_template_file.read()

                description_file_path : str = os.path.join(json_data['path'], 'description.txt')
                with open(description_file_path) as description_file:
                    json_data['description'] = description_file.read()

                character_list.append(json_data)
        except Exception as exception:
            print(f'Error reading {json_file}: {str(exception)}')
    return (character_list, model_data)
