from warcraftlogs.models.base import BaseMeta
from warcraftlogs.models.characters import Character
from warcraftlogs.models.zones import Encounter

class Fight(metaclass=BaseMeta):
    pk = ('id', 'encounter', 'duration')
    id = 'fightID'
    encounter = 'encounter'
    character = 'character'
    duration = 'duration'
    size = 'size'
    total = 'total'

    @classmethod
    def _get_character_from_dict(cls, data, default=None):
        if default is None:
            default = {}
        return Character.from_dict(data, **default)

    @classmethod
    def _get_encounter_from_dict(cls, data, default=None):
        return Encounter(id = data.get("encounterID",default), name = data.get("encounterName",default))

class Report(metaclass=BaseMeta):
    pk = ('id','title')
    id = 'id'
    title = 'title'
    owner = 'owner'
    zone = 'zone'
    startTime = 'startTime'
    endTime = 'endTime'
