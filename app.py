from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/about")
# def about():
#     return "toto je super prva stranka"
#
# if __name__ == "__main__":
#     app.run()

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return f"profil uzivatela {username}"

@app.route("/post/<int:post_id>")
def showpost(post_id):
    return f"Zobrazujem prispevok s ID {post_id}"

@app.route("/user/<username>/<projekt>/<nazov>/<priecinok>/<py>")
def metoda(username, projekt, nazov, priecinok, py):
    return (f"<p ><b>Profil uzivatela: </b>{username}</p>"
            f"<p><br><b>Projekt: </b>{projekt}</p>"
            f"<p><br><b>Nazov: </b>{nazov}</p>"
            f"<p><br><b>Priecinok: </b>{priecinok}</p>"
            f"<p><br><b>Subor: </b>{py}</p>")

if __name__ == "__main__":
    app.run()

