import unittest
from packages.core.engine import Engine
from packages.core.types import Task, Agent, Registry
class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        registry = Registry({}, {})
        engine = Engine(registry)
        agent = Agent('agent-1')
        engine.register_agent(agent)
        task = Task('task-1', 'agent-1')
        engine.assign_task(task)
        engine.execute_task(task.id)
        self.assertEqual(task.status, TaskStatus.COMPLETED)