from typing import Callable, Dict

from loguru import logger

from app.schemas.iris.methods import IrisDutyEventMethod


class Route:
    def __init__(self):
        self.handlers: Dict[str, Callable] = {}

    def method_handler(self, method: IrisDutyEventMethod):
        def decorator(func: Callable):
            if method in self.handlers:
                logger.warning(f"Handler for method '{method}' is already registered.")
            self.handlers[method] = func
            return func

        return decorator

    def get_handler(self, method: IrisDutyEventMethod) -> Callable:
        """Return the handler based on the IrisDutyEventMethod."""
        return self.handlers.get(method, None)


route = Route()
