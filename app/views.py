from django.shortcuts import render
import json

# Create your views here.
from app.models import tibmed
# from app01.models import chimed
from dataprocess.datapr import getEchartsTibData, getEchartsChiData


def showdata_view(request):
    data = tibmed.objects.all()
    return render(request, 'showdata.html', {'data': data})

# def showdata_view(request):
#     data = chimed.objects.all()
#     return render(request, 'showdata.html', {'data': data})

def echarts_view(request):
    return render(request, 'echarts.html')

# def index_view(request):
#     # 调用方法获取构建图谱所需数据
#     data, link, category_list = getEchartsTibData()
#
#     # 所有目录
#     categories = [{'name': 'སྨན་རྫས།'}, {'name': 'དབྱེ་བ།'}, {'name': 'རྣམ་པ།'}, {'name': 'སྐྱེ་གནས།'},
#                   {'name': 'འཚོལ་བསྡུ།'}, {'name': 'ཉེར་སྤྱོད།'}, {'name': 'རོ་དྲི།'}, {'name': 'གཙོ་བཅོས།'}]
#
#     # 获取实际所需的目录
#     categories = [categories[i] for i in category_list]
#
#     # 数据返回至前端展示
#     return render(request, 'test.html', {'data': json.dumps(data), 'link': json.dumps(link), 'categories': json.dumps(categories)})

def index_view(request):
    # 调用方法获取构建图谱所需数据
    data, link, category_list = getEchartsChiData()

    # 所有目录
    categories = [{'name': '药物'}, {'name': '患病部位'}, {'name': '定义'}, {'name': '所属科室'}, {'name': '相关疾病'},  {'name': '常用检查'},
                  {'name': '症因'}, {'name': '鉴别诊断'}, {'name': '预防治疗'}, {'name': '相关症状'}, {'name': '食疗'}]

    # 获取实际所需的目录
    categories = [categories[i] for i in category_list]

    # 数据返回至前端展示
    return render(request, 'index.html', {'data': json.dumps(data), 'link': json.dumps(link), 'categories': json.dumps(categories)})