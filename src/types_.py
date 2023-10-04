from typing import NotRequired, TypedDict

class _HistoryData(TypedDict):
    query: str
    result: float

class SessionData(TypedDict):
    user_id: str
    history:NotRequired[_HistoryData]
    error_msg:NotRequired[str]
