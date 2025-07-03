from locust import HttpUser, task, between

class LoadUser(HttpUser):
    wait_time = between(1, 2)  # simulate user wait time between requests

    @task
    def get_tickets(self):
        self.client.get("/api/v1/tickets")




#To Run:
#locust -f performance_tests/load_test.py --headless -u 100 -r 10 -t 60s --host=http://localhost:8000