from dataclasses import dataclass
from typing import List

import marshmallow


@dataclass
class GetUpdatesResponse:
    ok: bool
    # result: List[UpdateObj]

    class Meta:
        unknown = marshmallow.EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    # result: Message

    class Meta:
        unknown = marshmallow.EXCLUDE