import pandas as pd


def match(df_a, df_b, filename_a, filename_b, df_old=None, df_new=None):
    num_a = int(filename_a[:8])
    num_b = int(filename_b[:8])
    date_str = ""

    if num_a > num_b:
        df_new = df_a
        df_old = df_b
        date_str = str(num_a)

    elif num_a < num_b:
        df_new = df_b
        df_old = df_a
        date_str = str(num_b)

    else:
        # 处理文件名相等的情况，这里可以根据实际情况处理
        pass

    merged_df = pd.merge(df_new, df_old[
        ["笔记链接", "曝光量", "阅读量", "阅读UV", "互动量", "点赞量", "收藏量", "评论量", "分享量", "关注量",
         "自然曝光量", "自然阅读量", "推广曝光量", "推广阅读量",
         "发现页自然曝光", "搜索页自然曝光", "个人页自然曝光", "关注页自然曝光", "附近页自然曝光", "其他自然曝光",
         "发现页自然阅读", "搜索页自然阅读", "个人页自然阅读", "关注页自然阅读", "附近页自然阅读", "其他自然阅读",
         "粉丝总阅读", "女性总阅读", "男性总阅读", "<18总阅读", "18~24总阅读", "25~34总阅读", "35~44总阅读",
         ">44总阅读",
         "正文组件曝光量", "正文组件点击量", "正文组件点击人数",
         "评论区组件曝光量", "评论区组件点击量", "评论区组件点击人数"
         ]], on="笔记链接", how="left").fillna(0)

    formatted_date = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
    merged_df.to_excel(f"{formatted_date}_2日合并.xlsx", index=False, engine='openpyxl')

    print(merged_df.head())

    merged_df["间隔列"] = ""

    #曝光量
    merged_df["新增曝光量"] = merged_df["曝光量_x"] - merged_df["曝光量_y"]
    merged_df["新增自然曝光量"] = merged_df["自然曝光量_x"] - merged_df["自然曝光量_y"]
    merged_df["新增推广曝光量"] = merged_df["推广曝光量_x"] - merged_df["推广曝光量_y"]

    merged_df["新增发现页自然曝光"] = merged_df["发现页自然曝光_x"] - merged_df["发现页自然曝光_y"]
    merged_df["新增搜索页自然曝光"] = merged_df["搜索页自然曝光_x"] - merged_df["搜索页自然曝光_y"]
    merged_df["新增个人页自然曝光"] = merged_df["个人页自然曝光_x"] - merged_df["个人页自然曝光_y"]
    merged_df["新增关注页自然曝光"] = merged_df["关注页自然曝光_x"] - merged_df["关注页自然曝光_y"]
    merged_df["新增附近页自然曝光"] = merged_df["附近页自然曝光_x"] - merged_df["附近页自然曝光_y"]
    merged_df["新增其他自然曝光"] = merged_df["其他自然曝光_x"] - merged_df["其他自然曝光_y"]
    # 阅读量
    merged_df["新增阅读量"] = merged_df["阅读量_x"] - merged_df["阅读量_y"]
    merged_df["新增阅读UV"] = merged_df["阅读UV_x"] - merged_df["阅读UV_y"]
    merged_df["新增自然阅读量"] = merged_df["自然阅读量_x"] - merged_df["自然阅读量_y"]
    merged_df["新增推广阅读量"] = merged_df["推广阅读量_x"] - merged_df["推广阅读量_y"]

    merged_df["新增发现页自然阅读量"] = merged_df["发现页自然阅读_x"] - merged_df["发现页自然阅读_y"]
    merged_df["新增搜索页自然阅读量"] = merged_df["搜索页自然阅读_x"] - merged_df["搜索页自然阅读_y"]
    merged_df["新增个人页自然阅读量"] = merged_df["个人页自然阅读_x"] - merged_df["个人页自然阅读_y"]
    merged_df["新增关注页自然阅读量"] = merged_df["关注页自然阅读_x"] - merged_df["关注页自然阅读_y"]
    merged_df["新增附近页自然阅读量"] = merged_df["附近页自然阅读_x"] - merged_df["附近页自然阅读_y"]
    merged_df["新增其他自然阅读量"] = merged_df["其他自然阅读_x"] - merged_df["其他自然阅读_y"]

    #总阅读-分受众
    merged_df["新增粉丝总阅读量"] = merged_df["粉丝总阅读_x"] - merged_df["粉丝总阅读_y"]
    merged_df["新增女性总阅读量"] = merged_df["女性总阅读_x"] - merged_df["女性总阅读_y"]
    merged_df["新增男性总阅读量"] = merged_df["男性总阅读_x"] - merged_df["男性总阅读_y"]
    merged_df["新增<18总阅读量"] = merged_df["<18总阅读_x"] - merged_df["<18总阅读_y"]
    merged_df["新增18~24总阅读量"] = merged_df["18~24总阅读_x"] - merged_df["18~24总阅读_y"]
    merged_df["新增25~34总阅读量"] = merged_df["25~34总阅读_x"] - merged_df["25~34总阅读_y"]
    merged_df["新增35~44总阅读量"] = merged_df["35~44总阅读_x"] - merged_df["35~44总阅读_y"]
    merged_df["新增>44总阅读量"] = merged_df[">44总阅读_x"] - merged_df[">44总阅读_y"]

    #互动量
    merged_df["新增互动量"] = merged_df["互动量_x"] - merged_df["互动量_y"]
    merged_df["新增点赞量"] = merged_df["点赞量_x"] - merged_df["点赞量_y"]
    merged_df["新增收藏量"] = merged_df["收藏量_x"] - merged_df["收藏量_y"]
    merged_df["新增评论量"] = merged_df["评论量_x"] - merged_df["评论量_y"]
    merged_df["新增分享量"] = merged_df["分享量_x"] - merged_df["分享量_y"]
    merged_df["新增关注量"] = merged_df["关注量_x"] - merged_df["关注量_y"]
    #组件转化
    merged_df["新增正文组件曝光量"] = merged_df["正文组件曝光量_x"] - merged_df["正文组件曝光量_y"]
    merged_df["新增正文组件点击量"] = merged_df["正文组件点击量_x"] - merged_df["正文组件点击量_y"]
    merged_df["新增正文组件点击人数"] = merged_df["正文组件点击人数_x"] - merged_df["正文组件点击人数_y"]
    merged_df["新增评论区组件曝光量"] = merged_df["评论区组件曝光量_x"] - merged_df["评论区组件曝光量_y"]
    merged_df["新增评论区组件点击量"] = merged_df["评论区组件点击量_x"] - merged_df["评论区组件点击量_y"]
    merged_df["新增评论区组件点击人数"] = merged_df["评论区组件点击人数_x"] - merged_df["评论区组件点击人数_y"]


    #创建曝光日
    merged_df["曝光日"] = formatted_date

    #修改字段名
    merged_df.rename(columns={'笔记发布日期': '发布日'}, inplace=True)

    columns_to_keep = ["曝光日", "发布日", "品牌", "负责人", "博主昵称", "博主粉丝量", "博主健康等级", "笔记标题",
                       "笔记类型", "笔记链接", "博主报价", "服务费金额", "新增曝光量", "新增自然曝光量",
                       "新增推广曝光量", "新增发现页自然曝光", "新增搜索页自然曝光", "新增个人页自然曝光",
                       "新增关注页自然曝光", "新增附近页自然曝光", "新增其他自然曝光", "新增阅读量", "新增阅读UV",
                       "新增自然阅读量", "新增推广阅读量", "新增发现页自然阅读量", "新增搜索页自然阅读量",
                       "新增个人页自然阅读量", "新增关注页自然阅读量", "新增附近页自然阅读量", "新增其他自然阅读量",
                       "新增粉丝总阅读量", "新增女性总阅读量", "新增男性总阅读量", "新增<18总阅读量",
                       "新增18~24总阅读量",
                       "新增25~34总阅读量", "新增35~44总阅读量", "新增>44总阅读量", "新增互动量", "新增点赞量",
                       "新增收藏量", "新增评论量", "新增分享量", "新增关注量", "新增正文组件曝光量",
                       "新增正文组件点击量", "新增正文组件点击人数", "评论区组件文案", "新增评论区组件曝光量",
                       "新增评论区组件点击量", "新增评论区组件点击人数"]

    df_non_funnel = merged_df[columns_to_keep]

    df_non_funnel.to_excel(f"{date_str}_内容效率_最新非漏斗.xlsx", index=False, engine='openpyxl')
    return df_non_funnel
