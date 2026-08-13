from packages.core.engine import Engine
from packages.utils.logging import log_info
class Orchestrator:
    def __init__(self, engine: Engine):
        self.engine = engine
    def start(self):
        log_info('Starting orchestrator')
        self.engine.start()
    def stop(self):
        log_info('Stopping orchestrator')
        # implement engine stop logic