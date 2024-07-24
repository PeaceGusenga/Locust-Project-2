# Locust Load Testing Example

This project demonstrates how to use Locust to perform load testing on a free-to-use site (`http://test.k6.io`).

## Prerequisites

- macOS
- Homebrew (Package Manager)
- Python 3.7 or higher

## Installation

1. **Install Homebrew**: If you don't have Homebrew installed, run:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Install Python**:
    ```sh
    brew install python
    ```

3. **Install Locust**:
    ```sh
    pip3 install locust
    ```

## Project Setup

1. **Create a New Directory for Your Project**:
    ```sh
    mkdir locust-k6-load-testing
    cd locust-k6-load-testing
    ```

2. **Create a Locustfile**:
    ```sh
    touch locustfile.py
    ```

3. **Define Your Load Test**: Open `locustfile.py` in a text editor and add the following code:

    ```python
    from locust import HttpUser, TaskSet, task, between

    class UserBehavior(TaskSet):
        @task
        def load_homepage(self):
            self.client.get("/")

        @task
        def load_contacts(self):
            self.client.get("/contacts.php")

    class WebsiteUser(HttpUser):
        tasks = [UserBehavior]
        wait_time = between(1, 5)
        host = "http://test.k6.io"
    ```

## Running Locust

1. **Navigate to Your Project Directory**:
    ```sh
    cd locust-k6-load-testing
    ```

2. **Run Locust**:
    ```sh
    locust -f locustfile.py
    ```

3. **Open the Locust Web Interface**: Open your web browser and go to:
    ```
    http://localhost:8089
    ```

4. **Configure Your Test**:
    - Enter the number of total users to simulate (e.g., 100).
    - Enter the spawn rate (users per second, e.g., 10).

5. **Start the Test**: Click the "Start swarming" button.

## Monitoring Results

- The Locust web interface provides real-time statistics including the number of requests, response times, and failure rates.
- Use this data to analyze the performance and behavior of `http://test.k6.io` under load.

## Example Locustfile

Here is the complete content of `locustfile.py` for reference:

```python
from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_contacts(self):
        self.client.get("/contacts.php")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://test.k6.io"
