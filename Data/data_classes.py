from dataclasses import dataclass

if __name__ == "__main__":
    raise Exception("Нужно запускать wb_parser.py")

@dataclass
class RequestData:
    cookies: dict
    params: dict