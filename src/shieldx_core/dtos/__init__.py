from pydantic import BaseModel,Field
from typing import Any, Optional,Dict
from datetime import datetime,timezone

class MessageWithIDDTO(BaseModel):
    message: str
    id: str


class EventCreateDTO(BaseModel):
    service_id: str
    microservice_id: str
    function_id: str
    event_type: str
    payload: Optional[Any] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True  # <- permite convertir desde EventModel sin usar .dict()
    }

class EventResponseDTO(BaseModel):
    Event_id: str = Field(alias="_id")
    service_id: str
    microservice_id: str
    function_id: str
    event_type: str
    payload: Optional[Any] = None
    timestamp: datetime

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class EventUpdateDTO(BaseModel):
    service_id: Optional[str] = None
    microservice_id: Optional[str] = None
    function_id: Optional[str] = None
    event_type: Optional[str] = None
    payload: Optional[Any] = None

    model_config = {
        "populate_by_name": True
    }

class EventTypeCreateDTO(BaseModel):
    event_type: str

    model_config = {
        "populate_by_name": True,
        "serialization_config": {
            "use_aliases": True
        }
    }

class EventTypeResponseDTO(BaseModel):
    event_type_id: str = Field(alias="_id")
    event_type: str
    timestamp: datetime

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class EventsTriggersDTO(BaseModel):
    event_type_id: str
    trigger_id: str

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class RuleCreateDTO(BaseModel):
    target: str
    parameters: Dict[str, Any]

    model_config = {
        "populate_by_name": True
    }

class RulesTriggerDTO(BaseModel):
    rule_id: str
    trigger_id: str

class RuleUpdateDTO(BaseModel):
    target: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None

    model_config = {
        "populate_by_name": True
    }

class RuleResponseDTO(BaseModel):
    rule_id: str = Field(alias="_id")
    target: str
    parameters: Dict[str, Any]

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }


class TriggerCreateDTO(BaseModel):
    name: str

    model_config = {
        "populate_by_name": True
    }

class TriggerResponseDTO(BaseModel):
    trigger_id: str = Field(alias="_id")
    name: str

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class TriggerUpdateDTO(BaseModel):
    name: Optional[str] = None

    model_config = {
        "populate_by_name": True
    }

class TriggersTriggersDTO(BaseModel):
    trigger_parent_id: str
    trigger_child_id: str