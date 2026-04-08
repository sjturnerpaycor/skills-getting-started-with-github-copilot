from urllib.parse import quote


def test_signup_adds_student_to_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/signup", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body["message"] == f"Signed up {email} for {activity_name}"


def test_signup_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/signup", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 404
    assert body["detail"] == "Activity not found"


def test_signup_returns_400_when_already_registered(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/signup", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 400
    assert body["detail"] == "Student already signed up for this activity"
