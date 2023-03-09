from markupsafe import escape
import networkx as nx
import pickle as pickle
from flask import Flask, request, render_template, abort

app = Flask(__name__)


#G = nx.read_gpickle('parts.gpickle')

# open a file, where you stored the pickled data
file = open('parts.gpickle', 'rb')

# dump information to that file
G = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')

        result = nx.shortest_path(G, source=source, target = target)

        return render_template('sol.html', result = result)

    return render_template("index.html")


@app.route('/sol/')
def sol():
    return render_template('sol.html')
