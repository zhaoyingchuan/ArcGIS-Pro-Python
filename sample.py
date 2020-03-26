def fill(Field):
    if Field == '公路用地':
        return 5
    elif Field == '城市':
        return 5
    elif Field == '建制镇':
        return 5
    elif Field == '村庄':
        return 5
    elif Field == '水工建筑用地':
        return 5
    elif Field == '采矿用地':
        return 5
    elif Field == '铁路用地':
        return 5
    elif Field == '风景名胜及特殊用地':
        return 5
    elif Field == '港口码头用地':
        return 5
    elif Field == '其他园地':
        return 1
    elif Field == '园地':
        return 1
    elif Field == '果园':
        return 1
    elif Field == '茶园':
        return 1
    elif Field == '旱地':
        return 1
    elif Field == '水浇地':
        return 1
    elif Field == '水田':
        return 1
    elif Field == '农村道路':
        return 1
    elif Field == '坑塘水面':
        return 1
    elif Field == '沟渠':
        return 1
    elif Field == '设施农用地':
        return 1
    elif Field == '田坎':
        return 1
    elif Field == '其他林地':
        return 2
    elif Field == '其它林地':
        return 2
    elif Field == '有林地':
        return 2
    elif Field == '林地':
        return 2
    elif Field == '灌木林地':
        return 2
    elif Field == '其他草地':
        return 3
    elif Field == '其它草地':
        return 3
    elif Field == '内陆滩涂':
        return 6
    elif Field == '沼泽地':
        return 6
    elif Field == '自然保留地':
        return 6
    elif Field == '裸土地':
        return 6
    elif Field == '裸地':
        return 6
    elif Field == '沙地':
        return 6
    elif Field == '水库水面':
        return 4
    elif Field == '河流水面':
        return 4
    else:
        return 0
