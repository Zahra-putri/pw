from flask import Flask, render_template
import os

# kasih tau Flask folder template secara eksplisit
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # print lokasi file template buat ngecek
    print("Looking for templates in:", os.path.abspath('templates'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)