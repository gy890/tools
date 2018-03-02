import json
from locust import HttpLocust, TaskSet, task

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json'}

class WebsiteTasks(TaskSet):
    def on_start(self):
        payload = {
            'action': 'login',
            'request': {
                'username': 'gui.yun@e-ports.com',
                'password': 'password'
            }

        }
        res = self.client.post("/api/", data=json.dumps(payload), headers=headers)
        print('*' * 64)
        print(self.client)
        print('req.headers: {}'.format(self.client.headers))
        print('req.headers: {}'.format(res.request.headers))
        print('res.headers: {}'.format(res.headers))
        # print('res: {}'.format(res.json()['status']))
        print('[{}]{}'.format(res.status_code, res.elapsed))
        print('*' * 64)

    @task(2)
    def api_findMyFavShips(self):
        payload = {
            "action": "findMyFavShips",
            "request": {
                "params": {
                    "searchKey": ""
                }
            }
        }
        res1 = self.client.post('/api/', data=json.dumps(payload), headers=headers)
        print('{}[findMyFavShips][{}]{}'.format(self.client, res1.status_code, res1.elapsed))
        print(res1.json())
        print('res: {}'.format(res1.json()['status']))

    # @task(1)
    # def api_getFavoriteShips(self):
    #     payload = {"action": "getFavoriteShips",
    #                "request": {}}
    #     res2 = self.client.post('/api/', data=payload, headers=headers)
    #     print('{}[getFavoriteShips][{}]{}'.format(self.client, res2.status_code, res2.elapsed))
    #     print('res: {}'.format(res2.json()['status']))
    #     # print('[getFavoriteShips]req.headers: {}'.format(self.client.headers))


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://dev.e-ports.com/api/"
    min_wait = 1000
    max_wait = 5000
