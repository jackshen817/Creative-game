import pandas as pd
import numpy as np
import csv


shanghai = pd.read_csv(open('forecast_shanghai_sum_data.csv'))
shanghai_ds = np.array(shanghai['ds'])
shanghai_date = shanghai_ds.tolist()

beijing = pd.read_csv(open('forecast_beijing_sum_data.csv'))
beijing_ds = np.array(beijing['ds'])
beijing_date = beijing_ds.tolist()


chongqing = pd.read_csv(open('forecast_chongqing_sum_data.csv'))
chongqing_ds = np.array(chongqing['ds'])
chongqing_date = chongqing_ds.tolist()

input_city = input('请输入城市：')
city = ['重庆','上海','北京']
while input_city not in city:
    input_city = input('请重新输入城市：')
input_date = input('请输入时间：')



if input_city == '重庆':
    date = chongqing_date
    while input_date not in date:
        input_date = input('请重新输入时间(格式类似于2017-12-24)：')

    input_cut_date = input_date.split('-')

    year = np.int(input_cut_date[0])
    month = np.int(input_cut_date[1])
    date = np.int(input_cut_date[2])

    if year % 4 == 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 29:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if year % 4 != 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 28:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if new_month < 11:
        new_month = str(0) + str(new_month)
    if new_date < 11:
        new_date = str(0) + str(new_date)
    tomorrow_date = str(new_year) + '-' + str(new_month) + '-' + str(new_date)
    df_input = chongqing[chongqing['ds'] == input_date]
    df_input = np.array(df_input).tolist()
    df_input_temperature = df_input[0][1]
    df_input_humidity = df_input[0][4]
    df_input_pressure = df_input[0][7]

    df_tomorrow = chongqing[chongqing['ds'] == tomorrow_date]
    df_tomorrow = np.array(df_tomorrow).tolist()
    df_tomorrow_temperature = df_tomorrow[0][1]
    df_tomorrow_humidity = df_tomorrow[0][4]
    df_tomorrow_pressure = df_tomorrow[0][7]

    if 0 < float(df_input_temperature) <= 5:
        chongqing_input_temperatur_Spiciness = 5
    elif 5 < float(df_input_temperature) <= 16:
        chongqing_input_temperatur_Spiciness = 4.5
    elif 16 < float(df_input_temperature) <= 27:
        chongqing_input_temperatur_Spiciness = 3.5
    elif 27 < float(df_input_temperature) <= 36:
        chongqing_input_temperatur_Spiciness = 3

    if 45 < float(df_input_humidity) <= 55:
        chongqing_input_humidity_Spiciness = 2
    elif 55 < float(df_input_humidity) <= 65:
        chongqing_input_humidity_Spiciness = 2.5
    elif 65 < float(df_input_humidity) <= 80:
        chongqing_input_humidity_Spiciness = 3
    elif 80 < float(df_input_humidity) <= 100:
        chongqing_input_humidity_Spiciness = 3.5

    chongqing_input_Spiciness = chongqing_input_temperatur_Spiciness * 0.3 + chongqing_input_humidity_Spiciness * 0.7

    if 0 < float(df_input_temperature) <= 5:
        chongqing_input_temperatur_Salinity = 2.5
    elif 5 < float(df_input_temperature) <= 16:
        chongqing_input_temperatur_Salinity = 2
    elif 16 < float(df_input_temperature) <= 27:
        chongqing_input_temperatur_Salinity = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        chongqing_input_temperatur_Salinity = 1.5

    if 45 < float(df_input_humidity) <= 55:
        chongqing_input_humidity_Salinity = 1.5
    elif 55 < float(df_input_humidity) <= 65:
        chongqing_input_humidity_Salinity = 2
    elif 65 < float(df_input_humidity) <= 80:
        chongqing_input_humidity_Salinity = 2.5
    elif 80 < float(df_input_humidity) < 100:
        chongqing_input_humidity_Salinity = 3

    if 948 < float(df_input_pressure) <= 959:
        chongqing_input_pressure_Salinity = 1
    elif 959 < float(df_input_pressure) <= 973:
        chongqing_input_pressure_Salinity = 2
    elif 973 < float(df_input_pressure) <= 985:
        chongqing_input_pressure_Salinity = 2
    elif 985 < float(df_input_pressure) < 1000:
        chongqing_input_pressure_Salinity = 3

    chongqing_input_Salinity = chongqing_input_temperatur_Salinity * 0.3 + chongqing_input_humidity_Salinity * 0.6 + chongqing_input_pressure_Salinity * 0.1

    if 0 < float(df_input_temperature) <= 5:
        chongqing_input_temperatur_Acidity = 1
    elif 5 < float(df_input_temperature) <= 16:
        chongqing_input_temperatur_Acidity = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        chongqing_input_temperatur_Acidity = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        chongqing_input_temperatur_Acidity = 2

    if 45 < float(df_input_humidity) <= 55:
        chongqing_input_humidity_Acidity = 2
    elif 55 < float(df_input_humidity) <= 65:
        chongqing_input_humidity_Acidity = 1.5
    elif 65 < float(df_input_humidity) <= 80:
        chongqing_input_humidity_Acidity = 1.5
    elif 80 < float(df_input_humidity) <= 100:
        chongqing_input_humidity_Acidity = 1

    chongqing_input_Acidity = chongqing_input_temperatur_Acidity * 0.3 + chongqing_input_humidity_Acidity * 0.7

    if 0 < float(df_input_temperature) <= 5:
        chongqing_input_temperatur_Sweetness = 1
    elif 5 < float(df_input_temperature) <= 16:
        chongqing_input_temperatur_Sweetness = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        chongqing_input_temperatur_Sweetness = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        chongqing_input_temperatur_Sweetness = 2

    if 45 < float(df_input_humidity) <= 55:
        chongqing_input_humidity_Sweetness = 2
    elif 5 < float(df_input_humidity) <= 65:
        chongqing_input_humidity_Sweetness = 1.5
    elif 65 < float(df_input_humidity) <= 80:
        chongqing_input_humidity_Sweetness = 1.5
    elif 80 < float(df_input_humidity) <= 100:
        chongqing_input_humidity_Sweetness = 1

    chongqing_input_Sweetness = chongqing_input_temperatur_Sweetness * 0.3 + chongqing_input_humidity_Sweetness * 0.7

    input_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    input_dishes = input_data[
        (input_data['Spiciness'] < chongqing_input_Spiciness + 0.5) & (input_data['Spiciness'] > chongqing_input_Spiciness - 0.5)
        & (input_data['Salinity'] < chongqing_input_Salinity + 0.5) & (input_data['Salinity'] > chongqing_input_Salinity - 0.5)
        & (input_data['Acidity'] < chongqing_input_Acidity + 0.5) & (input_data['Acidity'] > chongqing_input_Acidity - 0.5)
        & (input_data['Sweetness'] < chongqing_input_Sweetness + 0.5) & (input_data['Sweetness'] > chongqing_input_Sweetness - 0.5)]



    if 0 < float(df_tomorrow_temperature) <= 5:
        chongqing_tomorrow_temperatur_Spiciness = 5
    elif 5 < float(df_tomorrow_temperature) <= 16:
        chongqing_tomorrow_temperatur_Spiciness = 4.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        chongqing_tomorrow_temperatur_Spiciness = 3.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        chongqing_tomorrow_temperatur_Spiciness = 3

    if 45 < float(df_tomorrow_humidity) <= 55:
        chongqing_tomorrow_humidity_Spiciness = 2
    elif 55 < float(df_tomorrow_humidity) <= 65:
        chongqing_tomorrow_humidity_Spiciness = 2.5
    elif 65 < float(df_input_humidity) <= 80:
        chongqing_tomorrow_humidity_Spiciness = 3
    elif 80 < float(df_tomorrow_humidity) <= 100:
        chongqing_tomorrow_humidity_Spiciness = 3.5

    chongqing_tomorrow_Spiciness = chongqing_tomorrow_temperatur_Spiciness * 0.3 + chongqing_tomorrow_humidity_Spiciness * 0.7

    if 0 < float(df_tomorrow_temperature) <= 5:
        chongqing_tomorrow_temperatur_Salinity = 2.5
    elif 5 < float(df_tomorrow_temperature) <= 16:
        chongqing_tomorrow_temperatur_Salinity = 2
    elif 16 < float(df_tomorrow_temperature) <= 27:
        chongqing_tomorrow_temperatur_Salinity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        chongqing_tomorrow_temperatur_Salinity = 1.5

    if 45 < float(df_tomorrow_humidity) <= 55:
        chongqing_tomorrow_humidity_Salinity = 1.5
    elif 55 < float(df_tomorrow_humidity) <= 65:
        chongqing_tomorrow_humidity_Salinity = 2
    elif 65 < float(df_tomorrow_humidity) <= 80:
        chongqing_tomorrow_humidity_Salinity = 2.5
    elif 80 < float(df_tomorrow_humidity) < 100:
        chongqing_tomorrow_humidity_Salinity = 3

    if 948 < float(df_tomorrow_pressure) <= 959:
        chongqing_tomorrow_pressure_Salinity = 1
    elif 959 < float(df_tomorrow_pressure) <= 973:
        chongqing_tomorrow_pressure_Salinity = 2
    elif 973 < float(df_tomorrow_pressure) <= 985:
        chongqing_tomorrow_pressure_Salinity = 2
    elif 985 < float(df_input_pressure) < 1000:
        chongqing_tomorrow_pressure_Salinity = 3

    chongqing_tomorrow_Salinity = chongqing_tomorrow_temperatur_Salinity * 0.3 + chongqing_tomorrow_humidity_Salinity * 0.6 + chongqing_tomorrow_pressure_Salinity * 0.1

    if 0 < float(df_tomorrow_temperature) <= 5:
        chongqing_tomorrow_temperatur_Acidity = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        chongqing_tomorrow_temperatur_Acidity = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        chongqing_tomorrow_temperatur_Acidity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        chongqing_tomorrow_temperatur_Acidity = 2

    if 45 < float(df_tomorrow_humidity) <= 55:
        chongqing_tomorrow_humidity_Acidity = 2
    elif 55 < float(df_tomorrow_humidity) <= 65:
        chongqing_tomorrow_humidity_Acidity = 1.5
    elif 65 < float(df_tomorrow_humidity) <= 80:
        chongqing_tomorrow_humidity_Acidity = 1.5
    elif 80 < float(df_tomorrow_humidity) <= 100:
        chongqing_tomorrow_humidity_Acidity = 1

    chongqing_tomorrow_Acidity = chongqing_tomorrow_temperatur_Acidity * 0.3 + chongqing_tomorrow_humidity_Acidity * 0.7

    if 0 < float(df_tomorrow_temperature) <= 5:
        chongqing_tomorrow_temperature_Sweetness = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        chongqing_tomorrow_temperature_Sweetness = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        chongqing_tomorrow_temperature_Sweetness = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        chongqing_tomorrow_temperature_Sweetness = 2

    if 45 < float(df_tomorrow_humidity) <= 55:
        chongqing_tomorrow_humidity_Sweetness = 2
    elif 5 < float(df_tomorrow_humidity) <= 65:
        chongqing_tomorrow_humidity_Sweetness = 1.5
    elif 65 < float(df_tomorrow_humidity) <= 80:
        chongqing_tomorrow_humidity_Sweetness = 1.5
    elif 80 < float(df_tomorrow_humidity) <= 100:
        chongqing_tomorrow_humidity_Sweetness = 1

    chongqing_tomorrow_Sweetness = chongqing_tomorrow_temperature_Sweetness * 0.3 + chongqing_tomorrow_humidity_Sweetness * 0.7

    tomorrow_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    tomorrow_dishes = tomorrow_data[
        (tomorrow_data['Spiciness'] < chongqing_tomorrow_Spiciness + 0.5) & (tomorrow_data['Spiciness'] > chongqing_tomorrow_Spiciness - 0.5)
        & (tomorrow_data['Salinity'] < chongqing_tomorrow_Salinity + 0.5) & (tomorrow_data['Salinity'] > chongqing_tomorrow_Salinity - 0.5)
        & (tomorrow_data['Acidity'] < chongqing_tomorrow_Acidity + 0.5) & (tomorrow_data['Acidity'] > chongqing_tomorrow_Acidity - 0.5)
        & (tomorrow_data['Sweetness'] < chongqing_tomorrow_Sweetness + 0.5) & (tomorrow_data['Sweetness'] > chongqing_tomorrow_Sweetness - 0.5)]

    chongqing_input_Recommend_dishes = input_dishes.sample(n=3, axis=0, replace=False)
    input_dishes = np.array(chongqing_input_Recommend_dishes).tolist()

    chongqing_tomorrow_Recommend_dishes = tomorrow_dishes.sample(n=3, axis=0, replace=False)
    tomorrow_dishes = np.array(chongqing_tomorrow_Recommend_dishes).tolist()
    print('今天的温度为：%.2f' %df_input_temperature, '°C','今天的湿度为：%.2f' %df_input_humidity ,'%','今天的气压为：%.2f'%df_input_pressure,'百帕')
    print('今日为您推荐的菜品为:%s' % input_dishes[0][0], ',%s' % input_dishes[1][0], ',%s' % input_dishes[2][0])
    print('明日为您推荐的菜品为:%s' % tomorrow_dishes[0][0], ',%s' % tomorrow_dishes[1][0], ',%s' % tomorrow_dishes[2][0])



if input_city == '北京':
    date = beijing_date
    while input_date not in date:
        input_date = input('请重新输入时间(格式类似于2017-12-24)：')

    input_cut_date = input_date.split('-')

    year = np.int(input_cut_date[0])
    month = np.int(input_cut_date[1])
    date = np.int(input_cut_date[2])

    if year % 4 == 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 29:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if year % 4 != 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 28:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if new_month < 11:
        new_month = str(0) + str(new_month)
    if new_date < 11:
        new_date = str(0) + str(new_date)
    tomorrow_date = str(new_year) + '-' + str(new_month) + '-' + str(new_date)


    df_input = beijing[beijing['ds'] == input_date]
    df_input = np.array(df_input).tolist()
    df_input_temperature = df_input[0][1]
    df_input_humidity = df_input[0][4]
    df_input_pressure = df_input[0][7]

    df_tomorrow = beijing[beijing['ds'] == tomorrow_date]
    df_tomorrow = np.array(df_tomorrow).tolist()
    df_tomorrow_temperature = df_tomorrow[0][1]
    df_tomorrow_humidity = df_tomorrow[0][4]
    df_tomorrow_pressure = df_tomorrow[0][7]


    if -17 < float(df_input_temperature) <= 5:
        beijing_input_temperatur_Spiciness = 4.5
    elif 5 < float(df_input_temperature) <= 16:
        beijing_input_temperatur_Spiciness = 3.5
    elif 16 < float(df_input_temperature) <= 27:
        beijing_input_temperatur_Spiciness = 2.5
    elif 27 < float(df_input_temperature) <= 34:
        beijing_input_temperatur_Spiciness = 1

    if 8 < float(df_input_humidity) <= 30:
        beijing_input_humidity_Spiciness = 1
    elif 30 < float(df_input_humidity) <= 50:
        beijing_input_humidity_Spiciness = 2.5
    elif 50 < float(df_input_humidity) <= 75:
        beijing_input_humidity_Spiciness = 3
    elif 75 < float(df_input_humidity) <= 100:
        beijing_input_humidity_Spiciness = 4

    beijing_input_Spiciness = beijing_input_temperatur_Spiciness * 0.6 + beijing_input_humidity_Spiciness * 0.4

    if -17 < float(df_input_temperature) <= 5:
        beijing_input_temperatur_Salinity = 3
    elif 5 < float(df_input_temperature) <= 16:
        beijing_input_temperatur_Salinity = 2.5
    elif 16 < float(df_input_temperature) <= 27:
        beijing_input_temperatur_Salinity = 1.5
    elif 27 < float(df_input_temperature) <= 34:
        beijing_input_temperatur_Salinity = 1

    if 8 < float(df_input_humidity) <= 30:
        beijing_input_humidity_Salinity = 1
    elif 30 < float(df_input_humidity) <= 50:
        beijing_input_humidity_Salinity = 2
    elif 50 < float(df_input_humidity) <= 75:
        beijing_input_humidity_Salinity = 2.5
    elif 75 < float(df_input_humidity) < 100:
        beijing_input_humidity_Salinity = 3

    if 977 < float(df_input_pressure) <= 990:
        beijing_input_pressure_Salinity = 1
    elif 990 < float(df_input_pressure) <= 1005:
        beijing_input_pressure_Salinity = 2
    elif 1005 < float(df_input_pressure) <= 1025:
        beijing_input_pressure_Salinity = 2.5
    elif 1025 < float(df_input_pressure) < 1036:
        beijing_input_pressure_Salinity = 3

    beijing_input_Salinity = beijing_input_temperatur_Salinity * 0.6 + beijing_input_humidity_Salinity * 0.2 + beijing_input_pressure_Salinity * 0.2

    if -17 < float(df_input_temperature) <= 5:
        beijing_input_temperatur_Acidity = 1
    elif 5 < float(df_input_temperature) <= 16:
        beijing_input_temperatur_Acidity = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        beijing_input_temperatur_Acidity = 1.5
    elif 27 < float(df_input_temperature) <= 34:
        beijing_input_temperatur_Acidity = 2

    if 8 < float(df_input_humidity) <= 30:
        beijing_input_humidity_Acidity = 2
    elif 30 < float(df_input_humidity) <= 50:
        beijing_input_humidity_Acidity = 1.5
    elif 50 < float(df_input_humidity) <= 75:
        beijing_input_humidity_Acidity = 1
    elif 75 < float(df_input_humidity) <= 100:
        beijing_input_humidity_Acidity = 1

    beijing_input_Acidity = beijing_input_temperatur_Acidity * 0.3 + beijing_input_humidity_Acidity * 0.7

    if -17 < float(df_input_temperature) <= 5:
        beijing_input_temperatur_Sweetness = 1
    elif 5 < float(df_input_temperature) <= 16:
        beijing_input_temperatur_Sweetness = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        beijing_input_temperatur_Sweetness = 1.5
    elif 27 < float(df_input_temperature) <= 34:
        beijing_input_temperatur_Sweetness = 2

    if 8 < float(df_input_humidity) <= 30:
        beijing_input_humidity_Sweetness = 2
    elif 30 < float(df_input_humidity) <= 50:
        beijing_input_humidity_Sweetness = 1.5
    elif 50 < float(df_input_humidity) <= 75:
        beijing_input_humidity_Sweetness = 1.5
    elif 75 < float(df_input_humidity) <= 100:
        beijing_input_humidity_Sweetness = 1

    beijing_input_Sweetness = beijing_input_temperatur_Sweetness * 0.7 + beijing_input_humidity_Sweetness * 0.3

    input_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    input_dishes = input_data[(input_data['Spiciness'] < beijing_input_Spiciness + 0.5) & (input_data['Spiciness'] > beijing_input_Spiciness - 0.5)
                  & (input_data['Salinity'] < beijing_input_Salinity + 0.5) & (input_data['Salinity'] > beijing_input_Salinity - 0.5)
                  & (input_data['Acidity'] < beijing_input_Acidity + 0.5) & (input_data['Acidity'] > beijing_input_Acidity - 0.5)
                  & (input_data['Sweetness'] < beijing_input_Sweetness + 0.5) & (input_data['Sweetness'] > beijing_input_Sweetness - 0.5)]




    if -17 < float(df_tomorrow_temperature) <= 5:
        beijing_tomorrow_temperatur_Spiciness = 4.5
    elif 5 < float(df_tomorrow_temperature) <= 16:
        beijing_tomorrow_temperatur_Spiciness = 3.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        beijing_tomorrow_temperatur_Spiciness = 2.5
    elif 27 < float(df_input_temperature) <= 34:
        beijing_tomorrow_temperatur_Spiciness = 1

    if 8 < float(df_tomorrow_humidity) <= 30:
        beijing_tomorrow_humidity_Spiciness = 1
    elif 30 < float(df_tomorrow_humidity) <= 50:
        beijing_tomorrow_humidity_Spiciness = 2.5
    elif 50 < float(df_tomorrow_humidity) <= 75:
        beijing_tomorrow_humidity_Spiciness = 3
    elif 75 < float(df_tomorrow_humidity) <= 100:
        beijing_tomorrow_humidity_Spiciness = 4

    beijing_tomorrow_Spiciness = beijing_tomorrow_temperatur_Spiciness * 0.6 + beijing_tomorrow_humidity_Spiciness * 0.4

    if -17 < float(df_tomorrow_temperature) <= 5:
        beijing_tomorrow_temperatur_Salinity = 3
    elif 5 < float(df_tomorrow_temperature) <= 16:
        beijing_tomorrow_temperatur_Salinity = 2.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        beijing_tomorrow_temperatur_Salinity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 34:
        beijing_tomorrow_temperatur_Salinity = 1

    if 8 < float(df_tomorrow_humidity) <= 30:
        beijing_tomorrow_humidity_Salinity = 1
    elif 30 < float(df_tomorrow_humidity) <= 50:
        beijing_tomorrow_humidity_Salinity = 2
    elif 50 < float(df_tomorrow_humidity) <= 75:
        beijing_tomorrow_humidity_Salinity = 2.5
    elif 75 < float(df_tomorrow_humidity) < 100:
        beijing_tomorrow_humidity_Salinity = 3

    if 977 < float(df_tomorrow_pressure) <= 990:
        beijing_tomorrow_pressure_Salinity = 1
    elif 990 < float(df_tomorrow_pressure) <= 1005:
        beijing_tomorrow_pressure_Salinity = 2
    elif 1005 < float(df_tomorrow_pressure) <= 1025:
        beijing_tomorrow_pressure_Salinity = 2.5
    elif 1025 < float(df_tomorrow_pressure) < 1036:
        beijing_tomorrow_pressure_Salinity = 3

    beijing_tomorrow_Salinity = beijing_tomorrow_temperatur_Salinity * 0.6 + beijing_tomorrow_humidity_Salinity * 0.2 + beijing_tomorrow_pressure_Salinity * 0.2

    if -17 < float(df_tomorrow_temperature) <= 5:
        beijing_tomorrow_temperatur_Acidity = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        beijing_tomorrow_temperatur_Acidity = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        beijing_tomorrow_temperatur_Acidity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 34:
        beijing_tomorrow_temperatur_Acidity = 2

    if 8 < float(df_tomorrow_humidity) <= 30:
        beijing_tomorrow_humidity_Acidity = 2
    elif 30 < float(df_tomorrow_humidity) <= 50:
        beijing_tomorrow_humidity_Acidity = 1.5
    elif 50 < float(df_tomorrow_humidity) <= 75:
        beijing_tomorrow_humidity_Acidity = 1
    elif 75 < float(df_tomorrow_humidity) <= 100:
        beijing_tomorrow_humidity_Acidity = 1

    beijing_tomorrow_Acidity = beijing_tomorrow_temperatur_Acidity * 0.3 + beijing_tomorrow_humidity_Acidity * 0.7

    if -17 < float(df_tomorrow_temperature) <= 5:
        beijing_tomorrow_temperatur_Sweetness = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        beijing_tomorrow_temperatur_Sweetness = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        beijing_tomorrow_temperatur_Sweetness = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 34:
        beijing_tomorrow_temperatur_Sweetness = 2

    if 8 < float(df_tomorrow_humidity) <= 30:
        beijing_tomorrow_humidity_Sweetness = 2
    elif 30 < float(df_tomorrow_humidity) <= 50:
        beijing_tomorrow_humidity_Sweetness = 1.5
    elif 50 < float(df_tomorrow_humidity) <= 75:
        beijing_tomorrow_humidity_Sweetness = 1.5
    elif 75 < float(df_tomorrow_humidity) <= 100:
        beijing_tomorrow_humidity_Sweetness = 1

    beijing_tomorrow_Sweetness = beijing_tomorrow_temperatur_Sweetness * 0.7 + beijing_tomorrow_humidity_Sweetness * 0.3

    tomorrow_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    tomorrow_dishes = tomorrow_data[(tomorrow_data['Spiciness'] < beijing_tomorrow_Spiciness + 0.5) & (tomorrow_data['Spiciness'] > beijing_tomorrow_Spiciness - 0.5)
                  & (tomorrow_data['Salinity'] < beijing_tomorrow_Salinity + 0.5) & (tomorrow_data['Salinity'] > beijing_tomorrow_Salinity - 0.5)
                  & (tomorrow_data['Acidity'] < beijing_tomorrow_Acidity + 0.5) & (tomorrow_data['Acidity'] > beijing_tomorrow_Acidity - 0.5)
                  & (tomorrow_data['Sweetness'] < beijing_tomorrow_Sweetness + 0.5) & (tomorrow_data['Sweetness'] > beijing_tomorrow_Sweetness - 0.5)]




    beijing_input_Recommend_dishes = input_dishes.sample(n=3, axis=0, replace=False)
    input_dishes = np.array(beijing_input_Recommend_dishes).tolist()
    beijing_tomorrow_Recommend_dishes = tomorrow_dishes.sample(n=3, axis=0, replace=False)
    tomorrow_dishes = np.array(beijing_tomorrow_Recommend_dishes).tolist()

    print('今天的温度为：%.2f' %df_input_temperature, '°C','今天的湿度为：%.2f' %df_input_humidity ,'%','今天的气压为：%.2f'%df_input_pressure,'百帕')
    print('今日为您推荐的菜品为:%s' % input_dishes[0][0], ',%s' % input_dishes[1][0], ',%s' % input_dishes[2][0])
    print('明日为您推荐的菜品为:%s' % tomorrow_dishes[0][0], ',%s' % tomorrow_dishes[1][0], ',%s' % tomorrow_dishes[2][0])


if input_city == '上海':
    date = shanghai_date
    while input_date not in date:
        input_date = input('请重新输入时间(格式类似于2017-12-24)：')

    input_cut_date = input_date.split('-')

    year = np.int(input_cut_date[0])
    month = np.int(input_cut_date[1])
    date = np.int(input_cut_date[2])

    if year % 4 == 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 29:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if year % 4 != 0:
        if month == 1:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 2
            else:
                new_date = date + 1
                new_month = month
        elif month == 2:
            new_year = year
            if date == 28:
                new_date = 1
                new_month = 3
            else:
                new_date = date + 1
                new_month = month
        elif month == 3:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 4
            else:
                new_date = date + 1
                new_month = month
        elif month == 4:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 5
            else:
                new_date = date + 1
                new_month = month
        elif month == 5:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 6
            else:
                new_date = date + 1
                new_month = month
        elif month == 6:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 7
            else:
                new_date = date + 1
                new_month = month
        elif month == 7:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 8
            else:
                new_date = date + 1
                new_month = month
        elif month == 8:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 9
            else:
                new_date = date + 1
                new_month = month
        elif month == 9:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 10
            else:
                new_date = date + 1
                new_month = month
        elif month == 10:
            new_year = year
            if date == 31:
                new_date = 1
                new_month = 11
            else:
                new_date = date + 1
                new_month = month
        elif month == 11:
            new_year = year
            if date == 30:
                new_date = 1
                new_month = 12
            else:
                new_date = date + 1
                new_month = month
        elif month == 12:
            if date == 31:
                new_date = 1
                new_month = 1
                new_year = year + 1
            else:
                new_date = date + 1
                new_month = month
                new_year = year
    if new_month < 11:
        new_month = str(0) + str(new_month)
    if new_date < 11:
        new_date = str(0) + str(new_date)
    tomorrow_date = str(new_year) + '-' + str(new_month) + '-' + str(new_date)
    df_input = shanghai[shanghai['ds'] == input_date]
    df_input = np.array(df_input).tolist()
    df_input_temperature = df_input[0][1]
    df_input_humidity = df_input[0][4]
    df_input_pressure = df_input[0][7]

    df_tomorrow = shanghai[shanghai['ds'] == tomorrow_date]
    df_tomorrow = np.array(df_tomorrow).tolist()
    df_tomorrow_temperature = df_tomorrow[0][1]
    df_tomorrow_humidity = df_tomorrow[0][4]
    df_tomorrow_pressure = df_tomorrow[0][7]


    if -7 < float(df_input_temperature) <= 5:
        shanghai_input_temperatur_Spiciness = 3.5
    elif 5 < float(df_input_temperature) <= 16:
        shanghai_input_temperatur_Spiciness = 3
    elif 16 < float(df_input_temperature) <= 27:
        shanghai_input_temperatur_Spiciness = 2.5
    elif 27 < float(df_input_temperature) <= 36:
        shanghai_input_temperatur_Spiciness = 1

    if 25 < float(df_input_humidity) <= 40:
        shanghai_input_humidity_Spiciness = 1
    elif 40 < float(df_input_humidity) <= 60:
        shanghai_input_humidity_Spiciness = 2.5
    elif 60 < float(df_input_humidity) <= 80:
        shanghai_input_humidity_Spiciness = 3
    elif 80 < float(df_input_humidity) <= 100:
        shanghai_input_humidity_Spiciness = 3.5

    shanghai_input_Spiciness = shanghai_input_temperatur_Spiciness * 0.7 + shanghai_input_humidity_Spiciness * 0.3

    if -7 < float(df_input_temperature) <= 5:
        shanghai_input_temperatur_Salinity = 2.5
    elif 5 < float(df_input_temperature) <= 16:
        shanghai_input_temperatur_Salinity = 2
    elif 16 < float(df_input_temperature) <= 27:
        shanghai_input_temperatur_Salinity = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        shanghai_input_temperatur_Salinity = 1

    if 25 < float(df_input_humidity) <= 40:
        shanghai_input_humidity_Salinity = 1
    elif 40 < float(df_input_humidity) <= 60:
        shanghai_input_humidity_Salinity = 2
    elif 60 < float(df_input_humidity) <= 80:
        shanghai_input_humidity_Salinity = 2
    elif 80 < float(df_input_humidity) < 100:
        shanghai_input_humidity_Salinity = 2.5

    if 980 < float(df_input_pressure) <= 1000:
        shanghai_input_pressure_Salinity = 1
    elif 1000 < float(df_input_pressure) <= 1015:
        shanghai_input_pressure_Salinity = 2
    elif 1015 < float(df_input_pressure) <= 1030:
        shanghai_input_pressure_Salinity = 2
    elif 1030 < float(df_input_pressure) < 1045:
        shanghai_input_pressure_Salinity = 3

    shanghai_input_Salinity = shanghai_input_temperatur_Salinity * 0.5 + shanghai_input_humidity_Salinity * 0.3 + shanghai_input_pressure_Salinity * 0.2

    if -7 < float(df_input_temperature) <= 5:
        shanghai_input_temperatur_Acidity = 1
    elif 5 < float(df_input_temperature) <= 16:
        shanghai_input_temperatur_Acidity = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        shanghai_input_temperatur_Acidity = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        shanghai_input_temperatur_Acidity = 2

    if 25 < float(df_input_humidity) <= 40:
        shanghai_input_humidity_Acidity = 2
    elif 40 < float(df_input_humidity) <= 60:
        shanghai_input_humidity_Acidity = 1.5
    elif 60 < float(df_input_humidity) <= 80:
        shanghai_input_humidity_Acidity = 1
    elif 80 < float(df_input_humidity) <= 100:
        shanghai_input_humidity_Acidity = 1

    shanghai_input_Acidity = shanghai_input_temperatur_Acidity * 0.3 + shanghai_input_humidity_Acidity * 0.7

    if -7 < float(df_input_temperature) <= 5:
        shanghai_input_temperatur_Sweetness = 1
    elif 5 < float(df_input_temperature) <= 16:
        shanghai_input_temperatur_Sweetness = 1.5
    elif 16 < float(df_input_temperature) <= 27:
        shanghai_input_temperatur_Sweetness = 1.5
    elif 27 < float(df_input_temperature) <= 36:
        shanghai_input_temperatur_Sweetness = 2

    if 25 < float(df_input_humidity) <= 40:
        shanghai_input_humidity_Sweetness = 2
    elif 40 < float(df_input_humidity) <= 60:
        shanghai_input_humidity_Sweetness = 1.5
    elif 60 < float(df_input_humidity) <= 80:
        shanghai_input_humidity_Sweetness = 1.5
    elif 80 < float(df_input_humidity) <= 100:
        shanghai_input_humidity_Sweetness = 1

    shanghai_input_Sweetness = shanghai_input_temperatur_Sweetness * 0.7 + shanghai_input_humidity_Sweetness * 0.3

    input_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    input_dishes = input_data[(input_data['Spiciness'] < shanghai_input_Spiciness + 0.5) & (input_data['Spiciness'] > shanghai_input_Spiciness - 0.5)
                  & (input_data['Salinity'] < shanghai_input_Salinity + 0.5) & (input_data['Salinity'] > shanghai_input_Salinity - 0.5)
                  & (input_data['Acidity'] < shanghai_input_Acidity + 0.5) & (input_data['Acidity'] > shanghai_input_Acidity - 0.5)
                  & (input_data['Sweetness'] < shanghai_input_Sweetness + 0.5) & (input_data['Sweetness'] > shanghai_input_Sweetness - 0.5)]




    if -7 < float(df_tomorrow_temperature) <= 5:
        shanghai_tomorrow_temperatur_Spiciness = 3.5
    elif 5 < float(df_tomorrow_temperature) <= 16:
        shanghai_tomorrow_temperatur_Spiciness = 3
    elif 16 < float(df_tomorrow_temperature) <= 27:
        shanghai_tomorrow_temperatur_Spiciness = 2.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        shanghai_tomorrow_temperatur_Spiciness = 1

    if 25 < float(df_tomorrow_humidity) <= 40:
        shanghai_tomorrow_humidity_Spiciness = 1
    elif 40 < float(df_tomorrow_humidity) <= 60:
        shanghai_tomorrow_humidity_Spiciness = 2.5
    elif 60 < float(df_tomorrow_humidity) <= 80:
        shanghai_tomorrow_humidity_Spiciness = 3
    elif 80 < float(df_tomorrow_humidity) <= 100:
        shanghai_tomorrow_humidity_Spiciness = 3.5

    shanghai_tomorrow_Spiciness = shanghai_tomorrow_temperatur_Spiciness * 0.7 + shanghai_tomorrow_humidity_Spiciness * 0.3

    if -7 < float(df_tomorrow_temperature) <= 5:
        shanghai_tomorrow_temperatur_Salinity = 2.5
    elif 5 < float(df_tomorrow_temperature) <= 16:
        shanghai_tomorrow_temperatur_Salinity = 2
    elif 16 < float(df_tomorrow_temperature) <= 27:
        shanghai_tomorrow_temperatur_Salinity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        shanghai_tomorrow_temperatur_Salinity = 1

    if 25 < float(df_tomorrow_humidity) <= 40:
        shanghai_tomorrow_humidity_Salinity = 1
    elif 40 < float(df_tomorrow_humidity) <= 60:
        shanghai_tomorrow_humidity_Salinity = 2
    elif 60 < float(df_tomorrow_humidity) <= 80:
        shanghai_tomorrow_humidity_Salinity = 2
    elif 80 < float(df_tomorrow_humidity) < 100:
        shanghai_tomorrow_humidity_Salinity = 2.5

    if 980 < float(df_tomorrow_pressure) <= 1000:
        shanghai_tomorrow_pressure_Salinity = 1
    elif 1000 < float(df_tomorrow_pressure) <= 1015:
        shanghai_tomorrow_pressure_Salinity = 2
    elif 1015 < float(df_tomorrow_pressure) <= 1030:
        shanghai_tomorrow_pressure_Salinity = 2
    elif 1030 < float(df_tomorrow_pressure) < 1045:
        shanghai_tomorrow_pressure_Salinity = 3

    shanghai_tomorrow_Salinity = shanghai_tomorrow_temperatur_Salinity * 0.5 + shanghai_tomorrow_humidity_Salinity * 0.3 + shanghai_tomorrow_pressure_Salinity * 0.2

    if -7 < float(df_tomorrow_temperature) <= 5:
        shanghai_tomorrow_temperatur_Acidity = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        shanghai_tomorrow_temperatur_Acidity = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        shanghai_tomorrow_temperatur_Acidity = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        shanghai_tomorrow_temperatur_Acidity = 2

    if 25 < float(df_tomorrow_humidity) <= 40:
        shanghai_tomorrow_humidity_Acidity = 2
    elif 40 < float(df_tomorrow_humidity) <= 60:
        shanghai_tomorrow_humidity_Acidity = 1.5
    elif 60 < float(df_tomorrow_humidity) <= 80:
        shanghai_tomorrow_humidity_Acidity = 1
    elif 80 < float(df_tomorrow_humidity) <= 100:
        shanghai_tomorrow_humidity_Acidity = 1

    shanghai_tomorrow_Acidity = shanghai_tomorrow_temperatur_Acidity * 0.3 + shanghai_tomorrow_humidity_Acidity * 0.7

    if -7 < float(df_tomorrow_temperature) <= 5:
        shanghai_tomorrow_temperatur_Sweetness = 1
    elif 5 < float(df_tomorrow_temperature) <= 16:
        shanghai_tomorrow_temperatur_Sweetness = 1.5
    elif 16 < float(df_tomorrow_temperature) <= 27:
        shanghai_tomorrow_temperatur_Sweetness = 1.5
    elif 27 < float(df_tomorrow_temperature) <= 36:
        shanghai_tomorrow_temperatur_Sweetness = 2

    if 25 < float(df_tomorrow_humidity) <= 40:
        shanghai_tomorrow_humidity_Sweetness = 2
    elif 40 < float(df_tomorrow_humidity) <= 60:
        shanghai_tomorrow_humidity_Sweetness = 1.5
    elif 60 < float(df_tomorrow_humidity) <= 80:
        shanghai_tomorrow_humidity_Sweetness = 1.5
    elif 80 < float(df_tomorrow_humidity) <= 100:
        shanghai_tomorrow_humidity_Sweetness = 1

    shanghai_tomorrow_Sweetness = shanghai_tomorrow_temperatur_Sweetness * 0.7 + shanghai_tomorrow_humidity_Sweetness * 0.3

    tomorrow_data = pd.read_excel('味道数据.xlsx', sheet_name='Sheet1')

    tomorrow_dishes = tomorrow_data[(tomorrow_data['Spiciness'] < shanghai_tomorrow_Spiciness + 0.5) & (tomorrow_data['Spiciness'] > shanghai_tomorrow_Spiciness - 0.5)
                  & (tomorrow_data['Salinity'] < shanghai_tomorrow_Salinity + 0.5) & (tomorrow_data['Salinity'] > shanghai_tomorrow_Salinity - 0.5)
                  & (tomorrow_data['Acidity'] < shanghai_tomorrow_Acidity + 0.5) & (tomorrow_data['Acidity'] > shanghai_tomorrow_Acidity - 0.5)
                  & (tomorrow_data['Sweetness'] < shanghai_tomorrow_Sweetness + 0.5) & (tomorrow_data['Sweetness'] > shanghai_tomorrow_Sweetness - 0.5)]


    shanghai_input_Recommend_dishes = input_dishes.sample(n=3, axis=0, replace=False)
    input_dishes = np.array(shanghai_input_Recommend_dishes).tolist()

    shanghai_tomorrow_Recommend_dishes = tomorrow_dishes.sample(n=3, axis=0, replace=False)
    tomorrow_dishes = np.array(shanghai_tomorrow_Recommend_dishes).tolist()


    print('今天的温度为：%.2f' %df_input_temperature, '°C','今天的湿度为：%.2f' %df_input_humidity ,'%','今天的气压为：%.2f'%df_input_pressure,'百帕')
    print('今日为您推荐的菜品为:%s' % input_dishes[0][0], ',%s' % input_dishes[1][0], ',%s' % input_dishes[2][0])
    print('明日为您推荐的菜品为:%s' % tomorrow_dishes[0][0], ',%s' % tomorrow_dishes[1][0], ',%s' % tomorrow_dishes[2][0])
