import pandas as pd

from app.models import tibmed


def getEchartsTibData():
    entity1_name = []
    relation = []
    entity2_name = []
    # django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]
    data = tibmed.objects.filter(entity1='རྒྱ་གྲོ།')
    # data = []
    for i in range(len(data)):
        entity1_name.append(data.values()[i].get('entity1'))
        relation.append(data.values()[i].get('relationship'))
        entity2_name.append(data.values()[i].get('entity2'))

    # 首先使用读取的节点名称构造关系数据
    link = [{'target':entity2_name[i],'source':entity1_name[i],'name':relation[i],'des':''} \
        for i in range(len(entity1_name))]
    print(link)

    # 存储目录级别 6级目录节点 藏药材、科属等等
    category_list = []

    # 构造节点数据 首先进行节点去重处理 原因：echarts构造图谱时 冗余节点名称会造成图谱无法显示
    entity1_set = list(set([entity1_name[i].strip() for i in range(len(entity1_name))]))
    # 添加藏药材目录级别代码
    category_list.append(0)

    # 构件Echarts显示的数据 此处构建包含实体1的节点数据
    data = [{'name': item, 'des': item, 'symbolSize': 80, 'category': 0} \
            for item in entity1_set]

    # 数据集对应的关系类别
    relation_set = ['དབྱེ་བ།', 'རྣམ་པ།', 'སྐྱེ་གནས།', 'འཚོལ་བསྡུ།', 'ཉེར་སྤྱོད།', 'རོ་དྲི།', 'གཙོ་བཅོས།']

    # 存储每一类关系对应的实体2, 字典存储
    entity2_dict = {r: [] for r in relation_set}

    # 遍历存储数据
    for i in range(len(relation)):
        entity2_dict[relation[i]].append(entity2_name[i])


    # 对实体2去重处理
    entity2_dict = {k:list(set(v)) for k,v in entity2_dict.items()}

    # 遍历构建实体2节点Echarts所需数据
    for i in range(len(relation_set)):

        # 获取已添加到data中的实体2数据
        e2_input = [item['name'] for item in data]

        # 遍历实体2数据并判断，若已添加，则不添加 原因：echarts构造图谱时 冗余节点名称会造成图谱无法显示
        for item in entity2_dict[relation_set[i]]:
            if item not in e2_input:

                # 构建时指定目录级别
                data.append({'name': item, 'des': item, 'symbolSize': 60, 'category': i+1})
                category_list.append(i+1)


    # 返回用于构建图谱的节点数据data、关系数据link及构建图谱的目录级别数据
    return data, link, list(set(category_list))

def getEchartsChiData():
    entity1_name = []
    relation = []
    entity2_name = []
    # 读取excel表 注意!! 文件路径需要修改，方法:使用pycharm打开项目DataDeal文件夹，点击藏药材.xlsx文件，然后右键 copy path
    # 若为windows 则将路径中 \ 修改为 /
    data = pd.read_excel(r'D:\PycharmProjects\DjangoDemo\dataprocess\CSKB中文症状知识库.xlsx', sheet_name='Sheet1')

    # 获取实体1数据列
    entity1_name = data['实体1']

    # 获取关系数据列
    relation = data['关系']

    # 获取实体2数据列
    entity2_name = data['实体2']

    # 首先使用读取的节点名称构造关系数据
    link = [{'target': entity2_name[i], 'source': entity1_name[i], 'name': relation[i], 'des': relation[i]} \
            for i in range(len(entity1_name))]

    # 存储目录级别 10级目录节点 患病部位、定义、所属科室等等
    category_list = []

    # 构造节点数据 首先进行节点去重处理 原因：echarts构造图谱时 冗余节点名称会造成图谱无法显示
    entity1_set = list(set([entity1_name[i].strip() for i in range(len(entity1_name))]))

    # 添加藏药材目录级别代码
    category_list.append(0)

    # 构件Echarts显示的数据 此处构建包含实体1的节点数据
    data = [{'name': item, 'des': item, 'symbolSize': 80, 'category': 0} \
            for item in entity1_set]

    # 数据集对应的关系类别
    relation_set = ['患病部位', '定义', '所属科室', '相关疾病', '常用检查', '症因', '鉴别诊断', '预防治疗', '相关症状', '食疗']

    # 存储每一类关系对应的实体2
    entity2_dict = {r: [] for r in relation_set}

    # 遍历存储数据
    for i in range(len(relation)):
        entity2_dict[relation[i].strip()].append(entity2_name[i].strip())

    # 对实体2去重处理
    entity2_dict = {k: list(set(v)) for k, v in entity2_dict.items()}

    # 遍历构建实体2节点Echarts所需数据
    for i in range(len(relation_set)):

        # 获取已添加到data中的实体2数据
        e2_input = [item['name'] for item in data]

        # 遍历实体2数据并判断，若已添加，则不添加 原因：echarts构造图谱时 冗余节点名称会造成图谱无法显示
        for item in entity2_dict[relation_set[i]]:
            if item not in e2_input:
                # 构建时指定目录级别
                data.append({'name': item, 'des': item, 'symbolSize': 60, 'category': i + 1})
                category_list.append(i + 1)

    # 返回用于构建图谱的节点数据data、关系数据link及构建图谱的目录级别数据
    print(data)
    print(link)
    print(list(set(category_list)))
    return data, link, list(set(category_list))