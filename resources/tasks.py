from flask import request, jsonify, Blueprint
from datetime import datetime
from database.tasks import insert_task, select_task_by_id, select_all_tasks, update_task, delete_task, complete_task


tasks_bp = Blueprint('routes-tasks',__name__)


"""ENDPOINT POST----------------------------------------------------------"""
@tasks_bp.route('/api/tasks',methods=['POST'])
def add_task():
    title = request.json['title']
    created_date = datetime.now().strftime("%x")   # el formato es de tipo --> mes/día/año
    
    data = (title,created_date)
    task_id = insert_task(data)
    
    if task_id:
        return_register = select_task_by_id(task_id)
        return jsonify({'message': return_register})
    return jsonify({'message':'Internal Error'})

"""ENDPOINT GET----------------------------------------------------------"""
@tasks_bp.route('/api/data-tasks')
def get_tasks():
    data = select_all_tasks()
    
    if data:
        return jsonify({'Tareas': data})
    elif data == False:
        return jsonify({'message':'Internal Error'})
    else:
        return jsonify({'tasks': {}})

"""ENDPOINT PUT----------------------------------------------------------"""
"""En la url del cliente se escribe el argumento de ?id=valor"""
@tasks_bp.route('/api/update-task',methods=['PUT'])
def change_task():
    title = request.json['title']
    id_arg = request.args.get('id')
    
    if update_task(id_arg,(title,)):
        task = select_task_by_id(id_arg)
        return jsonify(task)    
    
    return jsonify({'message':'Internal Error'})

"""ENDPOINT DELETE----------------------------------------------------------"""
@tasks_bp.route('/api/delete-task',methods=['DELETE'])
def del_task():
    id_arg = request.args.get('id')
    
    if delete_task(id_arg):
        return jsonify({'message':'Tarea eliminada'})
    return jsonify({'message':'Internal Error'})

"""Completar tareas"""
"""En la url del cliente se escribe el argumento de ?id=valor&completed=valor"""
@tasks_bp.route('/api/completed-task',methods=['PUT'])
def save_task():
    id_args = request.args.get('id')
    completed_args = request.args.get('completed')
    
    if complete_task(id_args,completed_args):
        return jsonify({'message':'Tarea completada exitosamente'})
    
    return jsonify({'message':'Internal Error'})
