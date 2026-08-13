import unittest
from packages.core.engine import Engine, TaskStatus
from packages.core.types import Task, Agent, Registry
class TestCore(unittest.TestCase):
    def test_task_status(self):
        task = Task('task-1', 'agent-1')
        self.assertEqual(task.status, TaskStatus.PENDING)
    def test_agent_registration(self):
        registry = Registry({}, {})
        engine = Engine(registry)
        agent = Agent('agent-1')
        engine.register_agent(agent)
        self.assertIn(agent.id, engine.agents)