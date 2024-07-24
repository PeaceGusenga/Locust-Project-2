from locust import HttpUser, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpUser
import json

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.post("/my_messages.php", json={"username": "admin", "password": "123"})
        if response.status_code == 200:
            self.token = response.json().get("token")
            self.client.headers.update({"Authorization": f"Bearer {self.token}"})

    @task
    def load_protected_page(self):
        self.client.get("/my_messages.php")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://test.k6.io"
