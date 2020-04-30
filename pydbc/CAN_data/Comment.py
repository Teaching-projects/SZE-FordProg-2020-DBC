from dataclasses import dataclass


@dataclass()
class Comment:
    type: str = None
    node_name: str = None
    message_id: int = None
    signal_name: str = None
    env_var_name: str = None
    comment: str = None
