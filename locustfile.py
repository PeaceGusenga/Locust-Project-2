from locust import HttpUser, TaskSet, task, between 

class UserBehaviour(TaskSet):
    @task
    def load_homepage (self):
        self.client.get("/")

    @task
    def load_contacts (self):
        self.client.get("/contacts.php")  

class WebsiteUser(HttpUser):
    tasks = [UserBehaviour]  
    wait_time = between (1, 5)
    host = "http://test.k6.io"