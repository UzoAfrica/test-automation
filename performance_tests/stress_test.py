from locust import HttpUser, task, constant_pacing

class StressUser(HttpUser):
    wait_time = constant_pacing(0.1)  # simulate high pressure (10 req/sec)

    @task
    def post_chat_message(self):
        payload = {"message": "Load testing message", "user_id": "test_user"}
        self.client.post("/api/v1/support/chat", json=payload)



#To Run:

#locust -f performance_tests/stress_test.py --headless -u 200 -r 20 -t 2m --host=http://localhost:8000
