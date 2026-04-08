from urllib.parse import quote


def test_unregister_removes_student_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/unregister", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert body["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_returns_404_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/unregister", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 404
    assert body["detail"] == "Activity not found"


def test_unregister_returns_404_when_not_registered(client):
    # Arrange
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"
    encoded_activity = quote(activity_name, safe="")

    # Act
    response = client.post(f"/activities/{encoded_activity}/unregister", params={"email": email})
    body = response.json()

    # Assert
    assert response.status_code == 404
    assert body["detail"] == "Student is not signed up for this activity"
