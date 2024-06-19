import sqlite3
import jinja2
import webbrowser

# рендерит таблицу из sqlite в html табличку

def render(db, table: str):
    db = sqlite3.connect(db)
    cur = db.cursor()

    cur.execute(f"pragma table_info(\"{table}\")")
    n = cur.fetchall()
    
    info = [i[1] for i in n]
    cur.execute(f"SELECT * FROM {table}")
    all = cur.fetchall()
    
    template = open("templates/table.html", "r")
    with open("dbwebrender_rendered.html", "w") as f: f.write(jinja2.Template(template.read()).render(info=info, all=all))
    template.close()

    webbrowser.open("dbwebrender_rendered.html")
