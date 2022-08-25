from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)
