import logging

from flask import Flask, g
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from todo_app.config import Settings

from todo_app.api import bp



def create_app():
    """Функция создания Flask приложения, добавления конфигурации и создание сесссий"""
    logger = logging.getLogger(__name__)

    app = Flask(__name__)

    app.register_blueprint(bp)

    settings = Settings()
    engine = create_engine(settings.db_uri, echo=True)
    session_maker = sessionmaker(engine, expire_on_commit=False)
    app.session_maker = scoped_session(session_maker)
    logger.info('Todo application started...')

    @app.before_request
    def before_request():
        g.session = app.session_maker()

    @app.teardown_request
    def teardown_request(exception=None):
        session = g.pop('session', None)
        if session:
            session.close()

    return app

def main():
    """Создание и запуск приложения"""
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    main()
