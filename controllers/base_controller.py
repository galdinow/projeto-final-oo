import json
from pathlib import Path
class BaseController:
    
    #mudar o path, e arrumar a identacao
    @staticmethod
    def create_json_file(filename):
        json_list = []
        with open(filename,mode="w") as file:
            json.dump(json_list, file)

    

    @staticmethod
    def create_path():
        script_dir = Path(__file__).parent
        print(script_dir)