def fill(Field):
    if Field=='采矿用地':
        return '独立工矿区'
    elif Field=='城镇用地':
        return '城镇建设用地区'
    elif Field=='公路用地':
	    return '其他用地'
    elif Field == '管道运输用地':
        return '其他用地'
    elif Field == '旱地':
        return '一般农地区'
    elif Field == '河流水面':
        return '其他用地'
    elif Field == '湖泊水面':
        return '其他用地'
    elif Field == '坑塘水面':
        return '一般农地区'
    elif Field == '林地':
        return '林业用地区'
    elif Field == '牧草地':
        return '生态环境安全控制区'
    elif Field == '农村道路':
        return '一般农地区'
    elif Field == '农村居民点用地':
        return '村庄建设用地区'
    elif Field == '农田水利用地':
        return '其他用地'
    elif Field == '设施农用地':
        return '一般农地区'
    elif Field == '水工建筑用地':
        return '其他用地'
    elif Field == '水浇地':
        return '一般农地区'
    elif Field == '水库水面':
        return '其他用地'
    elif Field == '水田':
        return '一般农地区'
    elif Field == '特殊用地':
        return '其他用地'
    elif Field == '铁路用地':
        return '其他用地'
    elif Field == '园地':
        return '一般农地区'
    elif Field == '自然保留地':
        return '一般农地区'
    else:
        return ""
