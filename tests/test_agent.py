import unittest
from agent_core import SmartAgent

class TestSmartAgent(unittest.TestCase):
    def test_initialization(self):
        agent = SmartAgent(config="test_config.yaml")
        self.assertIsNotNone(agent)

    def test_run(self):
        agent = SmartAgent(config="test_config.yaml")
        result = agent.run()
        self.assertEqual(result, "Agent running")

if __name__ == "__main__":
    unittest.main()
