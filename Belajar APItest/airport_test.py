import requests

def test_get_all_airports():
    response = requests.get('https://airportgap.dev-tester.com/api/airports')
    assert response.status_code == 200
    assert len(response.json().get("data")) == 30


def test_get_id_airport():
    aiprort_id = "CGK"
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{aiprort_id}')
    assert response.status_code == 200
    print(response.text)
    data = response.json().get("data")
    assert data["id"] == "CGK"
    assert data["attributes"]["latitude"] == "-6.12557"
    assert data["attributes"]["longitude"] == "106.655998"


def test_get_one_airport_not_found():
    aiprort_id = "SOETA"
    response = requests.get(f'https://airportgap.dev-tester.com/api/airports/{aiprort_id}')
    assert response.status_code == 404
    assert "The page you requested could not be found" not in response.text
