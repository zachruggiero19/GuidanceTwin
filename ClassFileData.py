from dataclasses import dataclass

@dataclass
class BuildItem:
    id: str
    response: int

@dataclass
class Scenario:
    id: str
    choice: str
    explanation: str

@dataclass
class WritingSample:
    id: str
    text: str
