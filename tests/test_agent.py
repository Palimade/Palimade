import unittest
from agent_core import SmartAgent
from integrations import IntegrationManager
from utils import Logger
import os
import time

class TestSmartAgent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.agent = SmartAgent(config="test_config.yaml")
        cls.integration_manager = IntegrationManager()
        cls.logger = Logger("logs/test_agent.log")
        print("Setting up test environment...")
    
    def test_agent_initialization(self):
        """Test if the agent initializes correctly with the given configuration."""
        self.assertIsNotNone(self.agent)
        self.assertEqual(self.agent.config['agent']['name'], "TestAgent")
        self.assertTrue(self.agent.config['agent']['logging'])
    
    def test_agent_run_cycle(self):
        """Test if the agent runs and stops without errors."""
        try:
            self.agent.run()
            status = self.agent.status()
            self.assertEqual(status, "running")
            time.sleep(2)  # Simulate processing time
        finally:
            self.agent.stop()
            status = self.agent.status()
            self.assertEqual(status, "stopped")
    
    def test_integration_connection(self):
        """Test if the agent can successfully connect to Slack integration."""
        self.integration_manager.connect("slack", {"token": "fake-token"})
        integrations = self.integration_manager.list_integrations()
        self.assertIn("slack", integrations)
        self.integration_manager.disconnect("slack")
        integrations = self.integration_manager.list_integrations()
        self.assertNotIn("slack", integrations)

    def test_data_processing(self):
        """Test agent's ability to process data correctly."""
        sample_data = {"input": [1, 2, 3, 4, 5]}
        processed_data = self.agent.process_data(sample_data)
        self.assertIsInstance(processed_data, dict)
        self.assertIn("result", processed_data)

    def test_logging_functionality(self):
        """Test if logging works correctly during agent operations."""
        log_path = "logs/agent.log"
        self.agent.run()
        self.agent.stop()
        self.assertTrue(os.path.exists(log_path))
        with open(log_path, "r") as log_file:
            logs = log_file.read()
            self.assertIn("Agent started", logs)
            self.assertIn("Agent stopped", logs)
    
    def test_error_handling(self):
        """Test agent's ability to handle errors gracefully."""
        with self.assertRaises(ValueError):
            self.agent.process_data(None)  # Passing invalid data
    
    def test_multiple_integrations(self):
        """Test agent's ability to handle multiple integrations simultaneously."""
        services = [
            {"name": "slack", "token": "fake-slack-token"},
            {"name": "database", "host": "localhost", "port": 5432}
        ]
        for service in services:
            self.integration_manager.connect(service["name"], service)
        integrations = self.integration_manager.list_integrations()
        self.assertIn("slack", integrations)
        self.assertIn("database", integrations)
        for service in services:
            self.integration_manager.disconnect(service["name"])
    
    def test_concurrent_agent_execution(self):
        """Test if multiple agents can run concurrently without conflict."""
        agent_two = SmartAgent(config="test_config.yaml")
        try:
            self.agent.run()
            agent_two.run()
            self.assertEqual(self.agent.status(), "running")
            self.assertEqual(agent_two.status(), "running")
        finally:
            self.agent.stop()
            agent_two.stop()
            self.assertEqual(self.agent.status(), "stopped")
            self.assertEqual(agent_two.status(), "stopped")
    
    @classmethod
    def tearDownClass(cls):
        print("Cleaning up test environment...")
        if os.path.exists("logs/test_agent.log"):
            os.remove("logs/test_agent.log")

if __name__ == '__main__':
    unittest.main()
