import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app import create_app
from todo_app.database import Base

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    return app

@pytest.fixture(scope='function')
def db(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    Base.metadata.create_all(bind=engine)
    session_maker = sessionmaker(engine)
    app.session_maker = scoped_session(session_maker)
    yield app.session_maker
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function', autouse=True)
def session(db):
    session = db()

    yield session

    session.close()


@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def create_response(client):
    response = client.post('/tasks', json={
        'title': 'Test Title',
        'description': 'Test Description'
    })
    return response
