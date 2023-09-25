from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re,requests,csv
import gcpDeploymentFinalFinal as gcp


app = Flask(__name__,template_folder='../static',static_folder='../static')

@app.route('/')
def index():
    return render_template('initial.html')

@app.route('/home.html')
def html4():
    return render_template('home.html')

@app.route('/threads.html')
def html1():
    return render_template('threads.html')


if __name__ == '__main__':
    app.run(debug=False)
