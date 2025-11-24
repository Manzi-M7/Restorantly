from website import app
from website import create_app
app.secret_key = 'make this hard to guess!'
app.run(debug=True)

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
