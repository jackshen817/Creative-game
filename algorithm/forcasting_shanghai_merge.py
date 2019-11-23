from fbprophet import Prophet
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

#提取上海每日温度、湿度、气压文件
dfall_shanghai_day_temperature = pd.read_csv(r'E:\pycharm\Creative game\Average_data\operation_result\shanghai\shanghai_average_everyday_temperature.csv',parse_dates=['date'],infer_datetime_format=True)
dfall_shanghai_day_humidity = pd.read_csv(r'E:\pycharm\Creative game\Average_data\operation_result\shanghai\shanghai_average_everyday_humidity.csv',parse_dates=['date'],infer_datetime_format=True)
dfall_shanghai_day_pressure = pd.read_csv(r'E:\pycharm\Creative game\Average_data\operation_result\shanghai\shanghai_average_everyday_pressure.csv',parse_dates=['date'],infer_datetime_format=True)

#处理上海每日温度数据
dfall_shanghai_day_temperature.replace(999999,np.nan,inplace=True)
dfall_shanghai_day_temperature.fillna(method='ffill',inplace=True)

#处理上海每日湿度数据
dfall_shanghai_day_humidity.replace(999999,np.nan,inplace=True)
dfall_shanghai_day_humidity.fillna(method='ffill',inplace=True)

#处理上海每日气压数据
dfall_shanghai_day_pressure.replace(999999,np.nan,inplace=True)
dfall_shanghai_day_pressure.fillna(method='ffill',inplace=True)


dfall_temperature_1 = dfall_shanghai_day_temperature.rename(columns={'date':'ds', 'temperature':'y'})
#dfall['y'] = np.log(dfall['y'])
dfall_temperature_1['y'] = (dfall_temperature_1['y'] - dfall_temperature_1['y'].min()) / (dfall_temperature_1['y'].max() - dfall_temperature_1['y'].min())
dfall_temperature_1['ds'] = pd.to_datetime(dfall_temperature_1['ds'])
dfall_temperature_1.set_index('ds')
df_temperature = dfall_temperature_1


dfall_humidity_1 = dfall_shanghai_day_humidity.rename(columns={'date':'ds', 'humidity':'y'})
#dfall['y'] = np.log(dfall['y'])
dfall_humidity_1['y'] = (dfall_humidity_1['y'] - dfall_humidity_1['y'].min()) / (dfall_humidity_1['y'].max() - dfall_humidity_1['y'].min())
dfall_humidity_1['ds'] = pd.to_datetime(dfall_humidity_1['ds'])
dfall_humidity_1.set_index('ds')
df_humidity = dfall_humidity_1

dfall_pressure_1 = dfall_shanghai_day_pressure.rename(columns={'date':'ds', 'pressure':'y'})
#dfall['y'] = np.log(dfall['y'])
dfall_pressure_1['y'] = (dfall_pressure_1['y'] - dfall_pressure_1['y'].min()) / (dfall_pressure_1['y'].max() - dfall_pressure_1['y'].min())
dfall_pressure_1['ds'] = pd.to_datetime(dfall_pressure_1['ds'])
dfall_pressure_1.set_index('ds')
df_pressure = dfall_pressure_1


m_temperature = Prophet(daily_seasonality=False,weekly_seasonality=False,changepoint_prior_scale=0.01)
m_temperature.fit(df_temperature)

m_humidity = Prophet(daily_seasonality=False,weekly_seasonality=False,changepoint_prior_scale=0.01)
m_humidity.fit(df_humidity)

m_pressure = Prophet(daily_seasonality=False,weekly_seasonality=False,changepoint_prior_scale=0.01)
m_pressure.fit(df_pressure)


future_temperature = m_temperature.make_future_dataframe(periods = 180)
future_temperature.tail()

future_humidity = m_humidity.make_future_dataframe(periods = 180)
future_humidity.tail()

future_pressure = m_pressure.make_future_dataframe(periods = 180)
future_pressure.tail()


forecast_temperature = m_temperature.predict(future_temperature)

forecast_humidity = m_humidity.predict(future_humidity)

forecast_pressure = m_pressure.predict(future_pressure)


df1 = forecast_temperature[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
df1['ds'] = pd.to_datetime(df1['ds'])
df1.set_index('ds', inplace=True)

df2 = forecast_humidity[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
df2['ds'] = pd.to_datetime(df2['ds'])
df2.set_index('ds', inplace=True)

df3 = forecast_pressure[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
df3['ds'] = pd.to_datetime(df3['ds'])
df3.set_index('ds', inplace=True)

df1['yhat'] = (df1['yhat'] * (dfall_shanghai_day_temperature['temperature'].max() - dfall_shanghai_day_temperature['temperature'].min())) + dfall_shanghai_day_temperature['temperature'].min()

df2['yhat'] = (df2['yhat'] * (dfall_shanghai_day_humidity['humidity'].max() - dfall_shanghai_day_humidity['humidity'].min())) + dfall_shanghai_day_humidity['humidity'].min()

df3['yhat'] = (df3['yhat'] * (dfall_shanghai_day_pressure['pressure'].max() - dfall_shanghai_day_pressure['pressure'].min())) + dfall_shanghai_day_pressure['pressure'].min()


data_temperature = df1[-180:]
data1 = data_temperature.rename(columns={'yhat':'yhat_temperature', 'yhat_lower':'yhat_lower_temperature', 'yhat_upper':'yhat_upper_temperature'})
#data1.to_csv('data_shanghai_forecasting_temperature_data.csv')

data_humidity = df2[-180:]
data2 = data_humidity.rename(columns={'yhat':'yhat_humidity', 'yhat_lower':'yhat_lower_humidity', 'yhat_upper':'yhat_upper_humidity'})
#data2.to_csv('data_shanghai_forecasting_humidity_data.csv')

data_pressure = df3[-180:]
data3 = data_pressure.rename(columns={'yhat':'yhat_pressure', 'yhat_lower':'yhat_lower_pressure', 'yhat_upper':'yhat_upper_pressure'})
#data3.to_csv('data_shanghai_forecasting_pressure_data.csv')

forecast_shanghai_sum_data = pd.concat([data1, data2, data3], axis= 1)
forecast_shanghai_sum_data.to_csv("forecast_shanghai_sum_data.csv")
