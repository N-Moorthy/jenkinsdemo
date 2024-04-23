from flask import Flask

app = Flask(__name__)

def colorful_header(text):
    # ANSI escape sequences for colors
    HEADER = '<h1 style="color: #00ff00;">'
    END = '</h1>'
    return f"{HEADER}{text}{END}"

@app.route('/')
def index():
    header = colorful_header("Welcome....!")
    details = '<h2>Here is My Basic Details</h2><p>Name: Narasimmamoorthy</p><p>Email: bala21.10moorthy@gmail.com</p><p>Role :DevOps</p>'
    return f"{header}\n{details}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
