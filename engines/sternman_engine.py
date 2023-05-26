from engines.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_on = warning_light_on

    def need_service(self):
        return self.warning_light_on