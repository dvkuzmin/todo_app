import pydantic
from flask import Blueprint, request, jsonify, abort,g
from sqlalchemy.exc import NoResultFound

from todo_app.database import Task
from todo_app.schemas import TaskIn

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=["POST"])
def create_task():
    data = request.get_json()
    session = g.session
    try:
        task = TaskIn(**data)
        new_task = Task(**task.dict())
        session.add(new_task)
        session.commit()
        return jsonify(new_task.to_dict()), 201
    except pydantic.ValidationError:
        abort(400, 'Wrong data')

@bp.route('/tasks', methods=["GET"])
def get_tasks():
    session = g.session
    tasks = session.query(Task).all()
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    return jsonify(task_list), 201


@bp.route('/tasks/<int:id>', methods=['GET'])
def get_task(id: int):
    session = g.session
    try:
        task = session.query(Task).filter_by(id=id).one()
        return jsonify(task.to_dict()), 200
    except NoResultFound:
        abort(404)

@bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id: int):
    session = g.session
    try:
        task = session.query(Task).filter_by(id=id).one()
        data = request.get_json()
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        session.commit()
        return jsonify(task.to_dict()), 200
    except NoResultFound:
        abort(404)


@bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id: int):
    session = g.session
    try:
        task = session.query(Task).filter_by(id=id).one()
        session.delete(task)
        session.commit()

        return jsonify({'message': 'Task deleted successfully'}), 200
    except NoResultFound:
        abort(404)
