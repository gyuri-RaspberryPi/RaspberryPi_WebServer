def add(self, content):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("insert into todo (content) values (%s)", (content,))
        conn.commit()
    finally:
        conn.close()

def toggle(self, todo_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("update todo set is_done = 1 - is_done where id = %s", (todo_id,))
        conn.commit()
    finally:
        conn.close()

def delete(self, todo_id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("delete from todo where id = %s", (todo_id,))
        conn.commit()
    finally:
        conn.close()
