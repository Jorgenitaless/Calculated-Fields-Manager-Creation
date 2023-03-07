from markupsafe import escape
from flask import Flask, request, render_template, abort

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')
        result = source + ' --> ' + target
        return render_template('sol.html', result = result)
    return render_template("Chatgpt.html")


@app.route('/sol/')
def sol():
    return render_template('sol.html')

        
def find_path(G, source, target):
    nx.shortest_path(G, source='Worker', target = 'Dependent')