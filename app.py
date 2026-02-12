from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    # 🔥 Cambiá esta fecha por la que quieras
    fecha_inicio = datetime(2025, 10, 12, 21, 10, 0)

    # La enviamos en formato ISO para que JS la entienda
    return render_template(
        "index.html",
        fecha_inicio=fecha_inicio.isoformat()
    )

if __name__ == "__main__":
    app.run(debug=True)
