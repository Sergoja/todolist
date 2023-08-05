from datetime import date

import pytest

from goals.models import Goal


@pytest.mark.django_db
def test_goals_list(client):
    goal = Goal.objects.create(
        title="test",
        description="test"
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": goal.pk,
            "user": {
                "id": 0,
                "username": "h_x60oNU74kdlm.KS6Nf21b1Ffmblyt8vf99Or4U8XovZ-qippqUS+TjdU9r.xOAuT4Xi",
                "first_name": "string",
                "last_name": "string",
                "email": "user@example.com"
            },
            "created": date.today().strftime("%Y-%m-%d"),
            "updated": date.today().strftime("%Y-%m-%d"),
            "title": "test",
            "description": "test",
            "due_date": None,
            "status": 1,
            "priority": 2,
            "category_id": None
        }]
    }

    response = client.get("/goals/goal/list/")

    assert response.status_code == 200
    assert response.data == expected_response
