from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def index(self):
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/showSummary", {"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task(2)
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces", {"competition": "Spring Festival", "club": "Simply Lift", "places": 5}
        )

    @task
    def list_clubs(self):
        self.client.get("/list_clubs")

    @task
    def logout(self):
        self.client.get("/logout")