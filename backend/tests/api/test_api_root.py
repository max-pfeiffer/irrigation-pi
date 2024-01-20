from httpx import Response
from starlette import status


def test_root(test_client):
    response: Response = test_client.get("/")

    assert response.status_code == status.HTTP_200_OK
