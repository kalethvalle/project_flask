from flask import (
    Blueprint, jsonify, request, 
)
from http import HTTPStatus
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
            if not data['title']:
                return jsonify({ "Error": "title is required" }), HTTPStatus.BAD_REQUEST
            elif not data['task_description']:
                return jsonify({ "Error": "description is required" }), HTTPStatus.BAD_REQUEST
            
            response = postTask(data['title'], data['task_description'])
            return jsonify(response), HTTPStatus.OK
        except Exception as err:
            print(f'Error creatting task, {err}')
            return jsonify ({"Error": f" Error creatting task"}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/api/task/<int:id>', methods=['GET', 'PATCH'])
def taskId(id):    
    if request.method == 'GET':
        try:
            response = getByIdTask(id)
            return jsonify(response), HTTPStatus.OK
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
            return jsonify ({"Error": f" Error updatting task"}), HTTPStatus.INTERNAL_SERVER_ERROR
