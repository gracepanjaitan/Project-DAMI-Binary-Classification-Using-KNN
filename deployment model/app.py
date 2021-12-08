from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np
import pandas as pd

app = Flask(__name__, template_folder='template')

model_file = open('BPJSFraudClassifier.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html')
['kdkc', 'umur', 'los', 'dx2_p00_p96', 'proc39_45', 'typeppk_C ', 'typeppk_SC', 'typeppk_D ', 'cmg_H', 'cmg_O']
@app.route('/predict', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        dx2_p00_p96 = float(request.form['dx2_p00_p96'])
        kdkc = float(request.form['kdkc'])
        umur = float(request.form['umur'])
        los = float(request.form['los'])
        proc39_45 = float(request.form['proc39_45'])
        typeppk_SC = float(request.form['typeppk_SC'])
        typeppk_D = float(request.form['typeppk_D'])
        typeppk_C = float(request.form['typeppk_C'])
        cmg_H = float(request.form['cmg_H'])
        cmg_O = float(request.form['cmg_O'])

        data = {'dx2_p00_p96' : [dx2_p00_p96],
        'kdkc' : [kdkc],
        'umur' : [umur],
        'los' : [los],
        'proc39_45' : [proc39_45],
        'typeppk_SC' : [typeppk_SC],
        'typeppk_D ' : [typeppk_D],
        'typeppk_C ' : [typeppk_C],
        'cmg_H' : [cmg_H],
        'cmg_O' : [cmg_O]
        }
        datas = pd.DataFrame(data)
        isFraud = model.predict(datas)

        dx2_p00_p96 = int(dx2_p00_p96)
        kdkc = int(kdkc)
        umur = int(umur)
        los = int(los)
        proc39_45 = int(proc39_45)
        typeppk_SC = int(typeppk_SC)
        typeppk_D = int(typeppk_D)
        typeppk_C = int(typeppk_C)
        cmg_H = int(cmg_H)
        cmg_O = int(cmg_O)
        return render_template('result.html', finalData = isFraud[0], cmg_O = cmg_O, cmg_H = cmg_H, typeppk_C = typeppk_C, typeppk_D = typeppk_D, typeppk_SC = typeppk_SC, proc39_45 = proc39_45, los = los, umur = umur, kdkc = kdkc, dx2_p00_p96 = dx2_p00_p96)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)