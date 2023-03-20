from src.services.task.queries import ( getTaskAll, getTaskById, insertTask, updateTask)

def getAllTask():
    try:
        return getTaskAll()
    except Exception as err:
        raise err

def getByIdTask(id):
    try:
        return getTaskById(id)
    except Exception as err:
        raise err

def putTask(id, title, description):
    try:
        return updateTask(id, title, description)
    except Exception as err:
        raise err

def postTask(title, description):    
    try:
        return insertTask(title, description)        
    except Exception as err:
        raise err
