import pandas as pd
import json
import requests
from pyquery import PyQuery as pq
from lxml import etree
import js2xml
from bs4 import BeautifulSoup
import execjs
from datetime import datetime


def parse_html_jsscript(response, table_id):
    bsObj = BeautifulSoup(response.text,'html.parser')
    bsObj = bsObj.find('div', id=table_id)
    # print(bsObj)
    bsElems = bsObj.find_all('script', type='text/javascript')
    tag = bsElems[0]
    # print(tag)
    # print(tag.string)
    # print(type(tag.string))
    # print(str(tag.text))
    # print(type(tag.text))
    # for x in bsElems:
    #     print(x.string)
    js_str = str(tag.text).split(";")[0].strip()
    js_str = js_str.strip().lstrip("tableData['"+table_id+"']")
    js_str = js_str.strip().lstrip("=")
    return js_str


def preprocess_js_str(js_str):

    json_obj = execjs.eval("my_list=" + js_str)
    # print(json_obj)
    _list = json_obj["list"]
    staticDate = json_obj["staticDate"]
    header = json_obj["header"]

    stock_info_list = []
    for item in _list:
        if item != '':
            item[2] = item[2].replace(" ","").replace("\t", "").strip()
            stock_info_list.append(item)

    # print(stock_info_list)

    return staticDate, header, stock_info_list


def get_SHHK_HK_eligible():
    response = requests.get("http://www.sse.com.cn/services/hkexsc/disclo/eligible/")
    response.encoding = 'utf-8'

    table_id = "tableData_918"
    js_str = parse_html_jsscript(response, table_id)

    staticDate, header, stock_info_list = preprocess_js_str(js_str)
    print(staticDate, header, stock_info_list)


def get_SHHK_HK_eligiblead():
    response = requests.get("http://www.sse.com.cn/services/hkexsc/disclo/eligiblead/")
    response.encoding = 'utf-8'

    table_id = "tableData_982"
    js_str = parse_html_jsscript(response, table_id)

    staticDate, header, stock_info_list = preprocess_js_str(js_str)
    print(staticDate, header, stock_info_list)


def pdf_file(url,file_name):
    response = requests.get(url)

    with open(file_name, "wb") as file:
            file.write(response.content)
    df = pd.read_excel(file_name)
    return df


def get_SZHK_HK_underlylist():

    url = 'http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=SGT_GGTBDQD&TABKEY=tab1&random=0.387256318420603'
    # date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date = datetime.now().strftime("%Y-%m-%d")
    file_name = '深港通港股通标的证券名单.' +date+'.xlsx'
    df_table = pdf_file(url, file_name)

    print(df_table)
    # sh_gg_name_list = df_table['中文简称'].values
    # print(sh_gg_name_list)
    # print(len(sh_gg_name_list))


def get_SZHK_HK_underlyadjust():

    url = 'http://www.szse.cn/api/report/ShowReport?SHOWTYPE=xlsx&CATALOGID=SGT_GGTBDTZ&TABKEY=tab1&random=0.2507281989293433'
    date = datetime.now().strftime("%Y-%m-%d")
    file_name = '深港通港股通标的证券调整.' +date+'.xlsx'
    df_table = pdf_file(url, file_name)

    print(df_table)


def get_SSE_Securities():
    url = ''
    date = datetime.now().strftime("%Y-%m-%d")
    file_name = '沪股通标的证券.' +date+'.xlsx'
    df_table = pdf_file(url, file_name)

    print(df_table)


def get_Change_of_SSE_Securities_Lists():
    url = ''
    date = datetime.now().strftime("%Y-%m-%d")
    file_name = '沪股通标的证券调整.' +date+'.xlsx'
    df_table = pdf_file(url, file_name)

    print(df_table)


if __name__=="__main__":
    '''
    print(len(stock_info_list))
    stock_list = []
    sz_gg_name_list = []
    for item in stock_info_list:
        if item != '':
            item[2] = item[2].replace(" ","").replace("\t", "").strip()
            # 有的只有英文名，没有中文名
            sz_gg_name_list.append(item[2])
            stock_list.append(item)



    print(stock_list)
    print(len(stock_list))
    sz_gg_name_list.sort()
    print(sz_gg_name_list)
    print(len(sz_gg_name_list))


    table = pd.read_excel("/Users/zhangjinzhi/Downloads/深港通港股通标的证券名单.xlsx")
    sh_gg_name_list = table['中文简称'].values
    # print(sh_gg_name_list)
    print(len(sh_gg_name_list))


    intersection  = list(set(sz_gg_name_list).intersection(sh_gg_name_list))
    intersection.sort()
    print(intersection)
    print(len(intersection))
    '''
    # 沪港通-港股通-标的证券名单
    # get_SHHK_HK_eligible()
    # 沪港通-港股通-标的证券调整信息
    # get_SHHK_HK_eligiblead()

    # 深港通-港股通-标的证券名单
    # get_SZHK_HK_underlylist()
    # 深港通-港股通-标的证券调整信息
    # get_SZHK_HK_underlyadjust()


    df = pd.read_excel("/Users/zhangjinzhi/Downloads/SSE_Securities_c.xls")

    # print(df)


    from opencc import openCC

    file_path = "/Users/zhangjinzhi/Downloads/SSE_Securities_c (1).xls"
    cc = OpenCC('mix2s')  # mix2s - Mixed to Simplified Chinese
    f = open(file_path, 'w')
    for line in open(file_path).readlines():
        l = line.decode('utf8', 'ignore').rstrip(u'\n')
        f.write(cc.convert(l) + u'\n')
    f.close()
    print(len(open(file_path).readlines()))















