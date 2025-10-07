from pydantic import BaseModel,Field, ValidationInfo, field_validator
from typing import Any, Optional,Dict,List
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
    event_id: str = Field(alias="_id")
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

class TargetDTO(BaseModel):
    alias: Optional[str] = None
    bucket_id: Optional[str] = None
    key: Optional[str] = None
    method: str = "run"

    model_config = {
        "populate_by_name": True
    }

class ParameterDetailDTO(BaseModel):
    ref: Optional[str] = None
    ref_dollar: Optional[str] = Field(default=None, alias="$ref")
    value: Optional[Any] = None
    type_: Optional[str] = Field(default=None, alias="type")
    name: Optional[str] = None
    description: Optional[str] = None

    model_config = {
        "populate_by_name": True
    }

class ParametersBlockDTO(BaseModel):
    init: Dict[str, ParameterDetailDTO] = Field(default_factory=dict)
    call: Dict[str, ParameterDetailDTO] = Field(default_factory=dict)

    model_config = {
        "populate_by_name": True
    }

class RuleCreateDTO(BaseModel):
    target: TargetDTO
    parameters: ParametersBlockDTO

    model_config = {
        "populate_by_name": True
    }

class RulesTriggerDTO(BaseModel):
    rule_id: str
    trigger_id: str

class RuleUpdateDTO(BaseModel):
    target: Optional[TargetDTO] = None
    parameters: Optional[ParametersBlockDTO] = None

    model_config = {
        "populate_by_name": True
    }

class RuleResponseDTO(BaseModel):
    rule_id: str = Field(alias="_id")
    target: TargetDTO
    parameters: ParametersBlockDTO

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }


class TriggerCreateDTO(BaseModel):
    name: str
    depends_on: Optional[str] = None

    model_config = {
        "populate_by_name": True
    }

class TriggerResponseDTO(BaseModel):
    trigger_id: str = Field(alias="_id")
    name: str
    depends_on: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "from_attributes": True
    }

class TriggerUpdateDTO(BaseModel):
    name: Optional[str] = None
    depends_on: Optional[str] = None
    
    model_config = {
        "populate_by_name": True
    }


class TriggersTriggersDTO(BaseModel):
    trigger_parent_id: str
    trigger_child_id: str

class DeploymentInfoDTO(BaseModel):
    """Información de red necesaria para ejecutar un objeto activo."""
    host: str
    req_res_port: int
    pubsub_port: int

class RuleTargetDTO(BaseModel):
    alias: str
    axo_bucket_id: str
    axo_endpoint_id: str

class RuleDTO(BaseModel):
    target: RuleTargetDTO

class ParamsDTO(BaseModel):
    init: Optional[Dict[str, str]] = None
    call: Optional[Dict[str, str]] = None

class NodeDTO(BaseModel):
    id: str
    type: str  # "ActiveObject" | "Bucket"
    name: Optional[str] = None
    rule: Optional[RuleDTO] = None
    params: Optional[ParamsDTO] = None
    deployment_info: Optional[DeploymentInfoDTO] = None
    sink_bucket_id: Optional[str] = None

    @field_validator("sink_bucket_id")
    def validate_sink_id(cls, v, info: ValidationInfo):
        node_type = info.data.get("type") if info.data else None
        if node_type == "ActiveObject" and v is not None:
            raise ValueError("sink_bucket_id solo es válido para nodos tipo 'Bucket'")
        return v

class EdgeDTO(BaseModel):
    from_: str = Field(..., alias="from")
    to: str


class EnrichedGraphSpecDTO(BaseModel):
    
    vertices: List[NodeDTO]
    edges: List[EdgeDTO] = []