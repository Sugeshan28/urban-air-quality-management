from flask import Flask, render_template, url_for, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('urbanmodel.pkl')

def get_aqi_bucket(aqi):
    if aqi <= 50:
        return 'Good'
    elif aqi <= 100:
        return 'Satisfactory'
    elif aqi <= 200:
        return 'Moderate'
    elif aqi <= 300:
        return 'Poor'
    elif aqi <= 400:
        return 'Very Poor'
    else:
        return 'Severe'
    
def model_predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    aqi = model.predict(input_df)[0]
    bucket = get_aqi_bucket(aqi)
    return {'AQI': round(aqi, 1), 'AQI_Bucket': bucket}

@app.route('/', methods= ['POST', 'GET'])
def home():
    graded = ''
    predicted = 0
    if request.method == 'POST':
        pm2 = request.form.get('pm2_5')
        pm1 = request.form.get('pm10')
        no = request.form.get('no')
        no2 = request.form.get('no2')
        o3 = request.form.get('o3')
        nh3 = request.form.get('nh3')
        co = request.form.get('co')
        so2 = request.form.get('so2')
        benzene = request.form.get('benzene')
        toluene = request.form.get('toluene')
        xylene = request.form.get('xylene')
        nox = 51.44

        
        new_data = {
            'PM2.5': [pm2],
            'PM10': [pm1],
            'NO': [no],
            'NO2': [no2],
            'NOx': [nox],
            'NH3': [nh3],
            'CO': [co],
            'SO2': [so2],
            'O3': [o3],
            'Benzene': [benzene],
            'Toluene': [toluene],
            'Xylene': [xylene]

        }


        new_df = pd.DataFrame(new_data)

        predicted_aqi = model.predict(new_df)
        print("Predicted AQI:", predicted_aqi[0])
        predicted = predicted_aqi[0]

        g = get_aqi_bucket(predicted)
        graded = g

    return render_template('index.html', value =  predicted, gra = graded   )

if __name__ == '__main__':
    app.run(debug=True)

