from django.urls import reverse


class TestApi:

    def test_empty_response(self, client):
        url = reverse('api')
        response = client.post(url, data=None)

        assert response.status_code == 200
        assert response.json == {}

    def test_prefix_response(self, client):
        url = reverse('api')
        response = client.post(url, data={'expression': '+ 1 2'})

        assert response.status_code == 200
        assert response.json['result'] == 3

    def test_infix_response(self, client):
        url = reverse('api')
        response = client.post(url + '?infix=true', data={'expression': '1 + 2'})

        assert response.status_code == 200
        assert response.json['result'] == 3
