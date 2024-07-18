import base64
import streamlit as st
import pandas as pd
import time
from io import BytesIO
from funnel import funnel  # 确保导入正确的函数
from nonfunnel import match  # 确保导入正确的函数
import re
import datetime


st.title("内容效率助手")
st.write(f"今天是{time.strftime('%Y年%m月%d日')}")

st.write("注：文档格式必须为：“20240714_内容效率_全量漏斗.xlsx”")
st.write("")

uploaded_file1 = st.file_uploader("上传前一日Excel文件: ", type=['xlsx', 'xls'])
uploaded_file2 = st.file_uploader("上传后一日Excel文件: ", type=['xlsx', 'xls'])


def extract_date_from_filename(filename):
    match = re.match(r"(\d{8})", filename)
    if match:
        date_str = match.group(1)
        return date_str
    else:
        return None


if uploaded_file1 and uploaded_file2:
    # 提取文件名中的日期部分
    filename1 = extract_date_from_filename(uploaded_file1.name)
    filename2 = extract_date_from_filename(uploaded_file2.name)

    if filename1 and filename2:
        df1 = pd.read_excel(uploaded_file1, skiprows=2, engine='openpyxl')
        df2 = pd.read_excel(uploaded_file2, skiprows=2, engine='openpyxl')

        # 处理函数的调用和结果处理
        funnel1 = funnel(df1, filename1)  # 假设 funnel 函数返回处理后的结果
        funnel2 = funnel(df2, filename2)  # 假设 funnel 函数返回处理后的结果
        nonfunnel_new = match(df1, df2, filename1, filename2)  # 假设 match 函数返回处理后的结果

        # 展示处理后的数据或结果
        st.write("前一日数据处理结果示例：")
        st.write(funnel1.head())  # 根据实际情况调整展示的数据量和方式
        st.write("后一日数据处理结果示例：")
        st.write(funnel2.head())  # 根据实际情况调整展示的数据量和方式
        st.write("非漏斗匹配结果示例：")
        st.write(nonfunnel_new.head())  # 根据实际情况调整展示的数据量和方式

        # 添加下载按钮
        def download_button(data, filename, button_text):
            csv = data.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label=button_text,
                data=csv,
                file_name=f"{filename}.csv",
                mime='text/csv',
            )

        download_button(funnel2, '单日漏斗数据源', '下载单日漏斗数据源')
        download_button(nonfunnel_new, '最新非漏斗', '下载最新非漏斗')
    else:
        st.warning("无法从文件名中提取日期，请确保文件名以8位日期开头。")
else:
    st.warning("请上传两个Excel文件以继续操作。")