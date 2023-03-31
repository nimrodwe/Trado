from locust import HttpUser, task, between

# run the command in terminal: locust -f .\Locust\locustfile.py --host http://localhost:3000 --users 50 --spawn-rate 20
# it might change you to a different port if it says "http://0.0.0.0:8089" then type "http://localhost:8089"
class MyLocust(HttpUser):
    wait_time = between(1, 5)

    @task
    def TradoWebsite(self):
        self.client.get(url="https://qa.trado.co.il/")