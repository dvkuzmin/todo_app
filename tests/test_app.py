from flask import Flask, g

from app import create_app
from todo_app.api import bp

def test_create_app():
    app = create_app()
    assert isinstance(app, Flask)

def test_blueprint_registration():
    app = create_app()
    assert 'tasks' in app.blueprints

def test_before_request(session):
    app = create_app()
    with app.test_request_context('/'):
        app.preprocess_request()
        assert g.session is not None

def test_teardown_request(session):
    app = create_app()
    with app.test_request_context('/'):
        app.preprocess_request()
        g.session = session
        app.process_response(app.response_class())
    assert g.get('session') is None
