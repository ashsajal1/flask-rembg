from flask import Flask, request, render_template, send_file
import random
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    blobs = [{'width': random.randint(50, 150),
              'height': random.randint(50, 150),
              'top': random.randint(0, 100),
              'left': random.randint(0, 100)} for _ in range(10)]
    if request.method == 'GET':
        return render_template('index.html', blobs=blobs)

if __name__ == '__main__':
    app.run(debug=True)
