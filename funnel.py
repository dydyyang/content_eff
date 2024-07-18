import pandas as pd
import os
from datetime import datetime, timedelta


def calculate_exposures(df):
    # 计算自然曝光绝对值
    df["发现页自然曝光"] = (df["发现页"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["搜索页自然曝光"] = (df["搜索页"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["个人页自然曝光"] = (df["个人页"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["关注页自然曝光"] = (df["关注页"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["附近页自然曝光"] = (df["附近页"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["其他自然曝光"] = (df["其他"].apply(pd.to_numeric, errors='coerce') * df["自然曝光量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)


def calculate_reads(df):
    # 计算自然阅读绝对值
    df["发现页自然阅读"] = (df["发现页.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["搜索页自然阅读"] = (df["搜索页.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["个人页自然阅读"] = (df["个人页.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["关注页自然阅读"] = (df["关注页.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["附近页自然阅读"] = (df["附近页.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["其他自然阅读"] = (df["其他.1"].apply(pd.to_numeric, errors='coerce') * df["自然阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)


def calculate_demographics(df):
    # 计算基础画像阅读绝对数
    df["粉丝总阅读"] = (df["粉丝占比"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["女性总阅读"] = (df["女"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["男性总阅读"] = (df["男"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["<18总阅读"] = (df["<18"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["18~24总阅读"] = (df["18~24"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["25~34总阅读"] = (df["25~34"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["35~44总阅读"] = (df["35~44"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df[">44总阅读"] = (df[">44"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)


def calculate_devices(df):
    # 计算手机阅读量
    df["Top1手机总阅读"] = (df["top1占比"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["Top2手机总阅读"] = (df["top2占比"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["Top3手机总阅读"] = (df["top3占比"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)


def calculate_provinces(df):
    # 计算省份阅读量
    df["Top1省份总阅读"] = (df["top1占比"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["Top2省份总阅读"] = (df["top2占比.1"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)
    df["Top3省份总阅读"] = (df["top3占比.2"].apply(pd.to_numeric, errors='coerce') * df["阅读量"].apply(pd.to_numeric, errors='coerce')).fillna(0).round().astype(int)


def convert_component(df):
    fields = [
        "正文组件曝光量",
        "正文组件点击量",
        "正文组件点击人数",
        "评论区组件曝光量",
        "评论区组件点击量",
        "评论区组件点击人数",
    ]

    # Convert the fields to numeric and handle errors
    for field in fields:
        df[field] = pd.to_numeric(df[field], errors='coerce').fillna(0).astype(int)


def process_filename(input_filename):
    # 获取文件名和扩展名
    filename, extension = os.path.splitext(input_filename)

    # 构建新的文件名
    new_filename = f"{filename}_已加漏斗数值{extension}"

    return new_filename


def funnel(df, filename):
    # 调用各个计算函数
    calculate_exposures(df)
    calculate_reads(df)
    calculate_demographics(df)
    calculate_devices(df)
    calculate_provinces(df)
    convert_component(df)
    df['笔记发布日期'] = pd.to_datetime(df['笔记发布日期']).dt.strftime('%Y-%m-%d')
    df['Unnamed: 0'] = pd.to_datetime(df['Unnamed: 0']).dt.strftime('%Y-%m-%d')

    columns_to_drop = [
        "任务名称", "星任务主任务id", "任务开始时间", "任务结束时间", "抽样比例", "阅读uv", "评论uv",
        "点赞uv", "收藏uv", "分享uv", "总金额", "蒲公英金额", "广告金额", "进店uv", "进店率",
        "累计进店成本", "跨域项目名称", "跨域项目ID", "阅读uv.1", "评论uv.1", "点赞uv.1",
        "收藏uv.1", "分享uv.1", "关注uv", "总金额.1", "蒲公英金额.1", "广告金额.1",
        "任务开始时间.1", "任务结束时间.1", "抽样比例.1", "站外活跃行为uv（30天设备归因）",
        "站外活跃率（30天设备归因）", "站外活跃成本（30天设备归因）", "站外活跃行为uv（15天设备归因）",
        "站外活跃率（15天设备归因）", "站外活跃成本（15天设备归因）", "任务开始时间.2", "任务结束时间.2",
        "品牌名称", "抽样比例.2", "站外行为UV（30天设备归因）", "站外转化率（30天设备归因）",
        "站外转化成本（30天设备归因）", "站外行为UV（15天设备归因）", "站外转化率（15天设备归因）",
        "站外转化成本（15天设备归因）"
    ]

    # 将结果写入Excel文件
    df.rename(columns={'Unnamed: 0': '数据更新日'}, inplace=True)
    df.drop(columns=columns_to_drop, inplace=True)
    df.to_excel(f"{filename}_内容效率_已处理漏斗_.xlsx", index=False, engine='openpyxl', sheet_name=f'{filename}')
    return df



