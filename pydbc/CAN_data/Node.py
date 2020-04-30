from dataclasses import dataclass


@dataclass()
class Node:
    name: str = None
    messages: list = None
