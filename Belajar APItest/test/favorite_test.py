import requests
from assertpy import assert_that

def test_create_favorite_airport():
    response = requests.post("https://airportgap.dev-tester.com/api/favorites", data={
        "airport_id": "KJK",
        "note": "Saya suka airport ini"
    }, headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'})
    assert_that(response.status_code).is_equal_to(201)
    airport = response.json()["data"]["attributes"]["airport"]
    assert_that(airport["name"]).is_equal_to("Wevelgem Airport")
    assert_that(airport["country"]).is_equal_to_ignoring_case("Belgium")
    print(response.text)

def test_get_favorite():
    response = requests.get("https://airportgap.dev-tester.com/api/favorites",
                            headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'})
    assert_that(response.status_code).is_equal_to(200)
    print(response.text)
    assert_that(len(response.json().get("data"))).is_greater_than_or_equal_to(1)

def test_update_favorite_notes():
    response_id = requests.get("https://airportgap.dev-tester.com/api/favorites",
                            headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'})
    airport_id = response_id.json().get("data")[0].get("id")
    response = requests.patch(f"https://airportgap.dev-tester.com/api/favorites/{airport_id}", headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'}, data={
        "note": "Diubah dengan seksama dalam tempo singkat"
    })
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()["data"]["attributes"]["note"]).is_equal_to("Diubah dengan seksama dalam tempo singkat")

def test_delete_favorite():
    response_id = requests.get("https://airportgap.dev-tester.com/api/favorites",
                                   headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'})
    airport_id = response_id.json().get("data")[0].get("id")
    response = requests.delete(f"https://airportgap.dev-tester.com/api/favorites/{airport_id}",
                              headers={'Authorization': 'Bearer token=E7JRFopaT3ScWg1AdguB6aVk'})
    assert_that(response.status_code).is_equal_to(204)

