from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_participant():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert email not in activities[activity_name]["participants"]

    # Restore state for subsequent tests
    activities[activity_name]["participants"].append(email)
