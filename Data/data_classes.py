from dataclasses import dataclass

@dataclass
class RequestData:
    cookies: dict
    params: dict