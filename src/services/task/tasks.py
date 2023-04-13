from src.services.task.queries import ( getTaskAll, getTaskById, insertTask, updateTask)

def getAllTask():
    return getTaskAll()

def getByIdTask(id):
    return getTaskById(id)

def postTask(title, description):    
    return insertTask(title, description)        

def putTask(id, title, description):
    return updateTask(id, title, description)
