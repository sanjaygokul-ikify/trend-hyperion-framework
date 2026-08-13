import logging
import threading
from typing import List, Dict
from .types import Agent, Task, Registry
from .exceptions import EngineError, InvalidAgentError, InvalidTaskError


class Engine:
    def __init__(self, registry: Registry):
        self.registry = registry
        self.agents: Dict[str, Agent] = {}
        self.tasks: Dict[str, Task] = {}
        self.lock = threading.Lock()
        self.logger = logging.getLogger(__name__)

    def register_agent(self, agent: Agent):
        with self.lock:
            if agent.id in self.agents:
                raise InvalidAgentError(f"Agent {agent.id} already registered")
            self.agents[agent.id] = agent
            self.logger.info(f"Registered agent {agent.id}")

    def unregister_agent(self, agent_id: str):
        with self.lock:
            if agent_id not in self.agents:
                raise InvalidAgentError(f"Agent {agent_id} not registered")
            del self.agents[agent_id]
            self.logger.info(f"Unregistered agent {agent_id}")

    def assign_task(self, task: Task):
        with self.lock:
            if task.id in self.tasks:
                raise InvalidTaskError(f"Task {task.id} already assigned")
            self.tasks[task.id] = task
            self.logger.info(f"Assigned task {task.id}")

    def execute_task(self, task_id: str):
        with self.lock:
            if task_id not in self.tasks:
                raise InvalidTaskError(f"Task {task_id} not assigned")
            task = self.tasks[task_id]
            agent = self.agents.get(task.agent_id)
            if agent is None:
                raise InvalidAgentError(f"Agent {task.agent_id} not registered")
            agent.execute_task(task)
            self.logger.info(f"Executed task {task_id}")

    def update_registry(self):
        with self.lock:
            self.registry.update(self.agents, self.tasks)
            self.logger.info("Updated registry")

    def start(self):
        self.logger.info("Starting engine")
        threading.Thread(target=self.run).start()

    def run(self):
        while True:
            with self.lock:
                for task in list(self.tasks.values()):
                    if task.status == Task.Status.PENDING:
                        self.execute_task(task.id)
            self.update_registry()
            self.logger.info("Engine running")