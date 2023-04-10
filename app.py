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
        

        try:
            result = nx.shortest_path(G, source=source, target = target)

            weights = [0] * (len(result)-1)
            for i in range(len(result)-1):
                u = result[i]
                v = result[i+1]
                edge_data = G.get_edge_data(u, v)
                weight = edge_data['Field']
                weights[i] = [weight]
            
            return render_template('sol.html', result = result, weights = weights)

        except (nx.NetworkXNoPath, nx.NodeNotFound) as e:
            return render_template("Chatgpt.html")
        
    return render_template("index.html")


@app.route('/sol/')
def sol():
    return render_template('sol.html')

@app.route('/chatgpt/')
def chatgpt():
    return render_template('Chatgpt.html')
