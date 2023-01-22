def test_post_legal_status(test_app):
    response = test_app.post(
        "/legal-status/",
        json={
            "name": "SARL",
        },
    )
    assert response.status_code == 201
