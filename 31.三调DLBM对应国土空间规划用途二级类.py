def fill(Field):
    if Field == '0304':
        return '1702 沼泽'
    elif Field == '0306':
        return '1702 沼泽'
    elif Field == '0402':
        return '1702 沼泽'
    elif Field == '0603':
        return '1602 盐田'
    elif Field == '1106':
        return '1703 滩涂'
    elif Field == '1108':
        return '1702 沼泽'
    elif Field == '0101':
        return '无'
    elif Field == '0102':
        return '无'
    elif Field == '0103':
        return '无'
    elif Field == '0201':
        return '无'
    elif Field == '0202':
        return '无'
    elif Field == '0203':
        return '无'
    elif Field == '0204':
        return '无'
    elif Field == '0301':
        return '无'
    elif Field == '0302':
        return '无'
    elif Field == '0305':
        return '无'
    elif Field == '0307':
        return '无'
    elif Field == '0404':
        return '1805 其他草地'
    # elif Field == '0508':
    #     return '09 仓储用地'
    # elif Field == '0601':
    #     return '08 工业用地'
    elif Field == '0602':
        return '1601 采矿用地'
    elif Field == '0701':
        return '0601 城镇住宅用地'
    elif Field == '0702':
        return '0602 农村住宅用地'
    elif Field == '08H1':
        return '0701 行政办公用地'
    # elif Field == '0810':
    #     return '12 绿地与广场用地'
    elif Field == '0810A':
        return '1203 广场用地'
    # elif Field == '09':
    #     return '15 特殊用地'
    elif Field == '1001':
        return '1401 铁路用地'
    elif Field == '1002':
        return '1003 城市轨道交通用地'
    elif Field == '1003':
        return '1402 公路用地'
    # elif Field == '1004':
    #     return '10 道路与交通设施用地'
    # elif Field == '1005':
    #     return '10 道路与交通设施用地'
    elif Field == '1006':
        return '0502 农村道路'
    elif Field == '1007':
        return '1402 机场用地'
    elif Field == '1008':
        return '1403 港口码头用地'
    elif Field == '1009':
        return '1405 管道运输用地'
    elif Field == '1101':
        return '1901 河流水面'
    elif Field == '1102':
        return '1902 湖泊水面'
    elif Field == '1103':
        return '1903 水库水面'
    elif Field == '1104':
        return '0504 坑塘水面'
    elif Field == '1107':
        return '0505 沟渠'
    elif Field == '1109':
        return '1406 区域公用设施用地'
    elif Field == '1201':
        return '无'
    elif Field == '1202':
        return '0501 设施农用地'
    elif Field == '1203':
        return '0503田坎'
    elif Field == '1204':
        return '1801 盐碱地'
    elif Field == '1205':
        return '1802 沙地'
    elif Field == '1206':
        return '1803 裸土地'
    elif Field == '1207':
        return '1804 裸岩石砾地'
    else:
        return ""