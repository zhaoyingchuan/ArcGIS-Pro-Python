def fill(Field):
    if Field=='010':
        return '基本农田保护区'
    elif Field=='020':
        return '一般农地区'
    elif Field=='030':
        return '城镇建设用地区'
    elif Field == '040':
        return '村庄建设用地区'
    elif Field == '050':
        return '独立工矿区'
    elif Field == '060':
        return '风景旅游用地区'
    elif Field == '070':
        return '生态环境安全控制区'
    elif Field == '080':
        return '自然与文化遗产保护'
    elif Field == '090':
        return '林业用地区'
    elif Field == '110':
        return '牧业用地区'
    elif Field == '990':
        return '其他用地'
    else:
        return ""
