import random

from locust import FastHttpUser, task, between

"""
HttpUser : 코어당 850 RPS 성능
FastHttpUser : 코어당 5000 RPS 성능
"""

class WebsiteUser(FastHttpUser):
    # 1 ~ 3초 사이 작업이 랜덤하게 수행
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def transliteration(self):
        input_text = "transformer"
        self.client.post("/predict", json={"text" : input_text})
