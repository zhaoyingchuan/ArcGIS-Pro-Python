def convert2(DLBM):
    if DLBM == '0101':
        return '0101 水田'
    elif DLBM == '0102':
        return '0102 水浇地'
    elif DLBM == '0103':
        return '0103 旱地'
    elif DLBM == '0201':
        return '0201 果园'
    elif DLBM == '0202':
        return '0202 茶园'
    elif DLBM == '0203':
        return '0203 橡胶园'
    elif DLBM == '0204':
        return '0204 其他果园'
    elif DLBM == '0301':
        return '0301 乔木林地'
    elif DLBM == '0302':
        return '0302 竹林地'
    elif DLBM == '0303':
        return '0507 红树林地'
    elif DLBM == '0304':
        return '0501 森林沼泽'
    elif DLBM == '0305':
        return '0303 灌木竹地'
    elif DLBM == '0306':
        return '0502灌丛沼泽'
    elif DLBM == '0307':
        return '0304 其他林地'
    elif DLBM == '0401':
        return '0401 天然牧草地'
    elif DLBM == '0402':
        return '0503 沼泽草地'
    elif DLBM == '0403':
        return '0402 人工牧草地'
    elif DLBM == '0404':
        return '0403 其他草地'
    elif DLBM == '0508':
        return ''
    elif DLBM == '05H1':
        return ''
    elif DLBM == '0601':
        return '1001 工业用地'
    elif DLBM == '0602':
        return '1002 采矿用地'
    elif DLBM == '0603':
        return '1003 盐田'
    elif DLBM == '0701':
        return '0701 城镇住宅用地'
    elif DLBM == '0702':
        return '0703 农村宅基地'
    elif DLBM == '0809':
        return ''
    elif DLBM == '0810':
        return ''
    elif DLBM == '0810A':
        return '1403 广场用地'
    elif DLBM == '08H2':
        return ''
    elif DLBM == '09':
        return ''
    elif DLBM == '1001':
        return ''
    elif DLBM == '1002':
        return '1206 城市轨道交通用地'
    elif DLBM == '1003':
        return '1202 公路用地'
    elif DLBM == '1004':
        return ''
    elif DLBM == '1005':
        return ''
    elif DLBM == '1006':
        return ''
    elif DLBM == '1007':
        return '1203 机场用地'
    elif DLBM == '1008':
        return ''
    elif DLBM == '1009':
        return '1205 管道运输用地'
    elif DLBM == '1101':
        return '1701 河流水面'
    elif DLBM == '1102':
        return '1702 湖泊水面'
    elif DLBM == '1103':
        return '1703 水库水面'
    elif DLBM == '1104':
        return '1704 坑塘水面'
    elif DLBM == '1104A':
        return '1704 坑塘水面'
    elif DLBM == '1105':
        return '0505 沿海滩涂'
    elif DLBM == '1106':
        return '0506 内陆滩涂'
    elif DLBM == '1107':
        return ''
    elif DLBM == '1108':
        return ''
    elif DLBM == '1109':
        return '1312 水工设施用地'
    elif DLBM == '1110':
        return '1706 冰川及常年积雪'
    elif DLBM == '1201':
        return '2301 空闲地'
    elif DLBM == '1202':
        return ''
    elif DLBM == '1203':
        return '2302 田坎'
    elif DLBM == '1204':
        return '2304 盐碱地'
    elif DLBM == '1205':
        return '2305 沙地'
    elif DLBM == '1206':
        return '2306 裸土地'
    elif DLBM == '1207':
        return '2307 裸岩石砾地'
    else:
        return ""