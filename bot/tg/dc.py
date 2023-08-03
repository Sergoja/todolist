from dataclasses import dataclass, field
from typing import List, Optional

import marshmallow
import marshmallow_dataclass


@dataclass
class Chat:
    id: int
    first_name: str
    last_name: Optional[str]
    username: str
    type: str

    class Meta:
        unknown = marshmallow.EXCLUDE


ChatSchema = marshmallow_dataclass.class_schema(Chat)


@dataclass
class Entities:
    offset: int
    length: int
    type: str

    class Meta:
        unknown = marshmallow.EXCLUDE


EntitiesSchema = marshmallow_dataclass.class_schema(Entities)


@dataclass
class FromMessage:
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str]
    username: str
    language_code: Optional[str]

    class Meta:
        unknown = marshmallow.EXCLUDE


FromMessageSchema = marshmallow_dataclass.class_schema(FromMessage)


@dataclass
class Message:
    message_id: int
    message_from: FromMessage = field(metadata={"data_key": "from"})
    chat: Chat
    date: int
    text: str
    entities: List[Entities] = None

    class Meta:
        unknown = marshmallow.EXCLUDE


MessageSchema = marshmallow_dataclass.class_schema(Message)


@dataclass
class UpdateObj:
    update_id: int
    message: Message

    class Meta:
        unknown = marshmallow.EXCLUDE


UpdateObjSchema = marshmallow_dataclass.class_schema(UpdateObj)


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]

    class Meta:
        unknown = marshmallow.EXCLUDE


GetUpdatesResponseSchema = marshmallow_dataclass.class_schema(GetUpdatesResponse)


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message

    class Meta:
        unknown = marshmallow.EXCLUDE


SendMessageResponseSchema = marshmallow_dataclass.class_schema(SendMessageResponse)
