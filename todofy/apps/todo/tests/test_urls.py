from django.urls import reverse


def test_todo_url(client, live_server):
    response = client.get(reverse('todo_index'))

    assert response.status_code == 200
