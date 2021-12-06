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

@app.route('/predict', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        visit_id = float(request.form['visit_id'])
        kdkc = float(request.form['kdkc'])
        umur = float(request.form['umur'])
        los = float(request.form['los'])
        proc39_45 = float(request.form['proc39_45'])
        typeppk_SC = float(request.form['typeppk_SC'])
        typeppk_D = float(request.form['typeppk_D'])
        typeppk_KJ = float(request.form['typeppk_KJ'])
        cmg_H = float(request.form['cmg_H'])
        cmg_O = float(request.form['cmg_O'])

        data = {'visit_id' : [visit_id],
        'kdkc' : [kdkc],
        'umur' : [umur],
        'los' : [los],
        'proc39_45' : [proc39_45],
        'typeppk_SC' : [typeppk_SC],
        'typeppk_D ' : [typeppk_D],
        'typeppk_C ' : [typeppk_KJ],
        'cmg_H' : [cmg_H],
        'cmg_O' : [cmg_O]
        }
        datas = pd.DataFrame(data)
        isFraud = model.predict(datas)

        visit_id = int(visit_id)
        kdkc = int(kdkc)
        umur = int(umur)
        los = int(los)
        proc39_45 = int(proc39_45)
        typeppk_SC = int(typeppk_SC)
        typeppk_D = int(typeppk_D)
        typeppk_KJ = int(typeppk_KJ)
        cmg_H = int(cmg_H)
        cmg_O = int(cmg_O)
        return render_template('result.html', finalData = isFraud[0], cmg_O = cmg_O, cmg_H = cmg_H, typeppk_KJ = typeppk_KJ, typeppk_D = typeppk_D, typeppk_SC = typeppk_SC, proc39_45 = proc39_45, los = los, umur = umur, kdkc = kdkc, visit_id = visit_id)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)