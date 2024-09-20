from typing import Callable, Dict, List

from loguru import logger


class Route:
    def __init__(self):
        self.handlers: Dict[str, Callable] = {}

    def message_handler(self, commands: List[str]):
        def decorator(func: Callable):
            for command in commands:
                if command in self.handlers:
                    logger.warning(
                        f"Handler for command '{command}' is already registered."
                    )
                self.handlers[command] = func
            return func

        return decorator

    def get_handler(self, message_text: str) -> Callable:
        for command, handler in self.handlers.items():
            if command in message_text.lower():
                return handler
        return None


route = Route()
