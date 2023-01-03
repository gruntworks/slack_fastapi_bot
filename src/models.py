from enum import IntEnum, Enum
from typing import Optional
from pydantic import BaseModel

class Priority(IntEnum, Enum):
    normal = 0,
    high = 1,
    fatal = 2,
    success = 3

class Attachment(BaseModel):
    content: str
    pretext: str

class Message(BaseModel):
    channel_id: str
    title: str
    text: str
    link: Optional[str] = None
    link_title: Optional[str] = None
    image_link: Optional[str] = None
    attachment: Optional[Attachment] = None
    priority: Optional[Priority] = None
