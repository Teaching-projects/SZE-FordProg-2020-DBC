from dataclasses import dataclass, field


@dataclass()
class Node:
    name: str = None
    messages: list = field(default_factory=list)
