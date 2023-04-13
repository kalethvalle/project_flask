from flask import (
    Blueprint, jsonify, request, 
)
from http import HTTPStatus
from src.core.errors.errors import (InvalidEntity, EntityNotFound)
from src.services.task.tasks import ( getAllTask, getByIdTask, postTask, putTask )

bp = Blueprint('', __name__)

@bp.route('/api/task', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        try:
            response = getAllTask()
            return jsonify(response), HTTPStatus.OK
        except Exception as err:
            print(f'Error getting task, {err}')
            return jsonify ({"Error": f" Error getting task"}), HTTPStatus.INTERNAL_SERVER_ERROR
    elif request.method == 'POST':
        try:
            data = request.get_json()

            if not data.get('title'):
                raise InvalidEntity("title is required")
            elif data.get('task_description') is None:
                raise InvalidEntity('description is required')
            
            response = postTask(data['title'], data['task_description'])
            return jsonify(response), HTTPStatus.OK
        except InvalidEntity as err:
            print(f'Error creatting task, {err}')
            return jsonify ({"Error": f"Error creatting task, {err}"}), HTTPStatus.BAD_REQUEST
        except Exception as err:
            print(f'Error creatting task, {err}')
            return jsonify ({"Error": f"Error creatting task"}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/api/task/<int:id>', methods=['GET', 'PATCH'])
def taskId(id):    
    if request.method == 'GET':
        try:
            response = getByIdTask(id)
            return jsonify(response), HTTPStatus.OK
        except EntityNotFound as err:
            print(f'Error getting by id task, {err}')
            return jsonify ({"Error": f" Error getting by id task"}), HTTPStatus.NOT_FOUND
        except Exception as err:
            print(f'Error getting by id task, {err}')
            return jsonify ({"Error": f" Error getting by id task"}), HTTPStatus.INTERNAL_SERVER_ERROR
    elif request.method == 'PATCH':
        try:
            data = request.get_json()
            response = putTask(id, data['title'], data['task_description'])
            return jsonify(response), HTTPStatus.OK
        except Exception as err:
            print(f'Error updatting task, {err}')
            return jsonify ({"Error": f"Error updatting task"}), HTTPStatus.INTERNAL_SERVER_ERROR
