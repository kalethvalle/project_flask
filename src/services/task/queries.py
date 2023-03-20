from src.database.sqlite import get_db

def getTaskAll():
    db = get_db()

    try:
        res = []
        query = '''
            SELECT
                id, 
                title,
                task_description,
                created
            FROM task
        '''
        rows = db.execute( query ).fetchall()
        for row in rows:
            res.append({ 
                "id": row['id'],
                "tittle": row['title'],
                "task_description": row['task_description'],
                "created": row['created']
            })
        return res
    except db.DatabaseError as err:
        raise err

def getTaskById(id):
    db = get_db()
    try:
        query = '''
            SELECT
                id, 
                title,
                task_description,
                created
            FROM task
            WHERE id = ?
        '''
        row = db.execute( query, ( id, ) ).fetchone()
        res = {
                "id": row['id'],
                "tittle": row['title'],
                "task_description": row['task_description'],
                "created": row['created']
        }
        return res
    except db.DatabaseError as err:
        raise err

def insertTask(title, description):
    db = get_db()
    try:
        query =  '''
            INSERT INTO task (
                title,
                task_description
            ) VALUES (?, ?)
        '''
        row = db.execute( query, (title, description) )
        db.commit()
        task = getTaskById(row.lastrowid)
        return task
    except db.IntegrityError as err:
        raise err

def updateTask(id, title, description):
    db = get_db()
    try:
        query = '''
            UPDATE task SET 
                title = ?,
                task_description = ?
            WHERE id = ?
        '''
        db.execute( query, (title, description, id) )
        db.commit()
        task = getTaskById(id)
        return task
    except db.IntegrityError as err:
        raise err
    