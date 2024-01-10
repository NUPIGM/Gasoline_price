import requests
import os 


url = 'https://cx.sinopecsales.com/yjkqiantai/data/switchProvince'

PROVINCE_JSON={
  "北京": "11",
  "天津": "12",
  "河北": "13",
  "山西": "14",
  "内蒙古": "15",
  "辽宁": "21",
  "吉林": "22",
  "黑龙江": "23",
  "上海": "31",
  "江苏": "32",
  "浙江": "33",
  "安徽": "34",
  "福建": "35",
  "江西": "36",
  "山东": "37",
  "河南": "41",
  "湖北": "42",
  "湖南": "43",
  "广东": "44",
  "广西": "45",
  "海南": "46",
  "重庆": "50",
  "四川": "51",
  "贵州": "52",
  "云南": "53",
  "西藏": "54",
  "陕西": "61",
  "甘肃": "62",
  "青海": "63",
  "宁夏": "64",
  "新疆": "65"
}
name=os.getenv("Gas_area") or "福建"
token=os.getenv("Gas_token") or "http://127.0.0.1"
group=os.getenv("Gas_group") or "Gasoline_price"
payload = {"provinceId":PROVINCE_JSON[name]}

# 发送JSON格式的POST请求
response = requests.post(url, json=payload)

if response.status_code == 200:
  data=response.json()
  GAS_92=data["data"]["provinceData"]["GAS_92"]
  GAS_95=data["data"]["provinceData"]["GAS_95"]
  AIPAO_GAS_98=data["data"]["provinceData"]["AIPAO_GAS_98"]
  CHECHAI_0=data["data"]["provinceData"]["CHECHAI_0"]
  print(data["data"]["provinceData"])
  requests.get(f"{token}/今日{name}油价/92号:{GAS_92}元,  95号:{GAS_95}元;\n98号:{AIPAO_GAS_98}元,  0号:{CHECHAI_0}元?group={group}")


 