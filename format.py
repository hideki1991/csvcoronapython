import pandas as pd
import urllib.request
from time import sleep


def transform(beforepath, afterpath):
    df_before = pd.read_csv(beforepath)
    indexNames = df_before[df_before['Time'] != 2019].index
    df_before.drop(indexNames, inplace=True)
    df_before.to_csv(afterpath)


def transform2(beforepath, beforepath2, afterpath):
    df_before = pd.read_csv(beforepath)
    df_before2 = pd.read_csv(beforepath)
    df_index = pd.read_csv(beforepath2)
    index = df_index["Country/Region"]
    index = index.tolist()
    indexNames = df_before[~df_before['Location'].isin(index)].index
    print(indexNames)
    df_before.drop(indexNames, inplace=True)
    df_before = df_before.sort_values("Location")
    df_before.to_csv(afterpath)



def transform3(beforepath, beforepath2):
    df_before = pd.read_csv(beforepath)
    df_index = pd.read_csv(beforepath2)
    index = df_index["Location"]
    index = index.tolist()
    indexNames = df_before[df_before['Country/Region'].isin(index)].index
    print(indexNames)
    df_before.drop(indexNames, inplace=True)
    df_before.to_csv("omitted.csv")


def transform4(beforepath, afterpath):
    df_before = pd.read_csv(beforepath)
    df_before = df_before.drop(df_before.columns[[0, 1, 2, 4, 5, 6, 7, 8, 9]], axis=1)
    print(df_before)
    df_before.to_csv(afterpath)



# 国連データから2019以外を除去を除去してpopulationを作成
# transform("rawdata/WPP2019_TotalPopulationBySex.csv", "./population.csv")
# populationのデータを手動で整形、国連データに含まれていない国を無くす　population1revised
# コロナのデータのうち、population1revisedに含まれていない国がないかチェック
transform3("rawdata/time_series_covid19_confirmed_global.csv", "population1revised.csv")
# population1revisedのうち、コロナに含まれていない地域を除去
transform2("population1revised.csv", "rawdata/time_series_covid19_confirmed_global.csv","population2.csv")
# population2の余分な列を除去
transform4("population2.csv", "population3.csv")
# population2の人口、人口密度をコロナに結合
