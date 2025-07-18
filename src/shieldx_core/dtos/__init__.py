from pydantic import BaseModel,Field
from typing import Any, Optional,Dict
from datetime import datetime,timezone

class DeleteResultDTO(BaseModel):
    deleted: bool


class IDResponseDTO(BaseModel):
    id: str

class MessageWithIDDTO(BaseModel):
    message: str
    event_id: str

class MessageDTO(BaseModel):
    message: str


class EventDTO(BaseModel):
    
    service_id: str
    microservice_id: str
    function_id: str
    event_type: str
    payload: Optional[Any] = None
    timestamp: datetime

    model_config = {
        "populate_by_name": True,
        "from_attributes": True  # <- permite convertir desde EventModel sin usar .dict()
    }

class EventTypeDTO(BaseModel):
    event_type_id: str = Field(alias="_id")
    event_type: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

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
    rule_id: str = Field(..., alias="_id")
    target: str
    parameters: Dict[str, Any]

    model_config = {
        "populate_by_name": True
    }


class RulesTriggerDTO(BaseModel):
    rule_id: str
    trigger_id: str


class TriggerDTO(BaseModel):
    trigger_id: Optional[str] = Field(default=None, alias="_id")
    name: str


    model_config = {
        "populate_by_name": True
    }
class TriggersTriggersDTO(BaseModel):
    trigger_parent_id: str
    trigger_child_id: str