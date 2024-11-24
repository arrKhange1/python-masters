import dataclasses
import json
import os
from typing import Generic, List, TypeVar

JsonType = TypeVar('JsonType')

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JsonType):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class JsonManager(Generic[JsonType]):

    def __init__(self, file_name):
        self._file_name = file_name

    def export_json(self, list_of_obj: List[JsonType]):
        jsonedTasks = json.dumps([dataclasses.asdict(obj) for obj in list_of_obj], sort_keys=True, indent=4)
        with open(self._file_name, 'w') as file:
            file.write(jsonedTasks)

    def import_json(self) -> List[JsonType]:
        if not os.path.isfile(self._file_name): return []
        with open(self._file_name, 'r') as file:
            return [JsonType(**obj) for obj in json.load(file)]