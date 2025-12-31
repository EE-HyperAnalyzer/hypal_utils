from pydantic import BaseModel, ConfigDict


class ProtocolMessage(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Ok(ProtocolMessage):
    pass


class Error(ProtocolMessage):
    reason: str
