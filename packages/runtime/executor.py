import logging
import threading
from typing import Dict
from ..core.types import Task, Agent
from ..core.exceptions import EngineError


class Executor:
    def __init__(self, engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def execute_task(self, task: Task):
        try:
            agent = self.engine.agents.get(task.agent_id)
            if agent is None:
                raise EngineError(f"Agent {task.agent_id} not registered")
            agent.execute_task(task)
            self.logger.info(f"Executed task {task.id}")
        except EngineError as e:
            self.logger.error(f"Error executing task {task.id}: {e}")
