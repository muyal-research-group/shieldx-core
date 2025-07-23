from pydantic import BaseModel,Field
from typing import Any, Optional,Dict
from datetime import datetime,timezone

class MessageWithIDDTO(BaseModel):
    message: str
    id: str


class EventDTO(BaseModel):
    
    service_id: str
    microservice_id: str
    function_id: str
    event_type: str
    payload: Optional[Any] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True  # <- permite convertir desde EventModel sin usar .dict()
    }

class EventTypeDTO(BaseModel):
    event_type: str

    model_config = {
        "populate_by_name": True,
        "serialization_config": {
            "use_aliases": True
        }
    }
class EventsTriggersDTO(BaseModel):
    event_type_id: str
    trigger_id: str

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class RuleDTO(BaseModel):
    target: str
    parameters: Dict[str, Any]

    model_config = {
        "populate_by_name": True
    }


class RulesTriggerDTO(BaseModel):
    rule_id: str
    trigger_id: str


class TriggerDTO(BaseModel):
    name: str

    model_config = {
        "populate_by_name": True
    }
class TriggersTriggersDTO(BaseModel):
    trigger_parent_id: str
    trigger_child_id: str