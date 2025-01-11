# Palimade API Reference

This document provides a detailed reference for the core classes, methods, and modules in **Palimade**. Use this guide to understand how to interact with and extend the platform.

---

## 📦 Modules

### `agent_core`
Handles the creation and management of autonomous agents.

### `integrations`
Manages integrations with third-party platforms and services.

### `utils`
Provides helper functions and utilities for the platform.

---

## 🧩 Classes & Methods

### **`SmartAgent`**
Located in: `agent_core.smart_agent`

#### **Description:**
The core class for creating and running autonomous agents.

#### **Initialization:**
```python
SmartAgent(config: str)
```
- **config** (`str`): Path to the configuration YAML file.

#### **Methods:**
- `run()` → Starts the agent.
- `stop()` → Stops the agent.
- `train(data: Any)` → Trains the agent with custom data.
- `status()` → Returns the current status of the agent.

#### **Example:**
```python
from agent_core import SmartAgent

agent = SmartAgent(config="config.yaml")
agent.run()
print(agent.status())
agent.stop()
```

---

### **`IntegrationManager`**
Located in: `integrations.integration_manager`

#### **Description:**
Manages connections between agents and third-party platforms.

#### **Initialization:**
```python
IntegrationManager()
```

#### **Methods:**
- `connect(service_name: str, credentials: dict)` → Connects to a platform.
- `disconnect(service_name: str)` → Disconnects from a platform.
- `list_integrations()` → Lists all active integrations.

#### **Example:**
```python
from integrations import IntegrationManager

manager = IntegrationManager()
manager.connect("Slack", {"token": "xoxb-1234"})
print(manager.list_integrations())
manager.disconnect("Slack")
```

---

### **`Logger`**
Located in: `utils.logger`

#### **Description:**
Provides logging functionality for tracking agent behavior and errors.

#### **Initialization:**
```python
Logger(log_file: str)
```
- **log_file** (`str`): Path to the log file.

#### **Methods:**
- `info(message: str)` → Logs informational messages.
- `error(message: str)` → Logs error messages.
- `debug(message: str)` → Logs debug messages.

#### **Example:**
```python
from utils import Logger

logger = Logger("agent.log")
logger.info("Agent started successfully.")
logger.error("Failed to connect to API.")
```

---

## 🛠️ Utilities

### **Helper Functions**
- `load_config(path: str)` → Loads configuration files.
- `validate_data(data: Any)` → Validates input data for agents.

#### **Example:**
```python
from utils import load_config, validate_data

config = load_config("config.yaml")
validate_data(config)
```

---

For more advanced usage, refer to the [Usage Guide](usage.md) and explore the source code in the `src/` directory.

**Palimade: Intelligent Agents, Seamless Solutions.**
