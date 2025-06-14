import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

df = pd.read_csv("stationfinal.csv")
print(df.head()) 

df.dropna(inplace=True)

df = df.drop(columns=['Date', 'AQI_Bucket'], errors='ignore')

X = df.drop('AQI', axis=1)
y = df['AQI']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)


# After training your model
joblib.dump(model,'urbanmodel.pkl')





# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor


# new_data = {
#     'PM2.5': [80],
#     'PM10': [100],
#     'NO': [10],
#     'NO2': [20],
#     'NOx': [30],
#     'NH3': [5],
#     'CO': [1.2],
#     'SO2': [10],
#     'O3': [15],
#     'Benzene': [2],
#     'Toluene': [5],
#     'Xylene': [1]
# }

        
# new_df = pd.DataFrame(new_data)

# predicted_aqi = model.predict(new_df)
# print("Predicted AQI:", predicted_aqi[0])
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
