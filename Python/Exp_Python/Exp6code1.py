#Exp6code1

# -*- coding: UTF-8 -*-
Dict={'京':'北京市','津':'天津市','冀':'河北省','晋':'山西省','内蒙古':'内蒙古自治区','辽':'辽宁市','吉':'吉林省','黑':'黑龙江省','沪':'上海市','苏':'江苏省','浙':'浙江省','皖':'安徽省','闽':'福建省','赣':'江西省','鲁':'山东省','豫':'河南省','鄂':'湖北省','湘':'湖南省','粤':'广东省','桂':'广西壮族自治区','琼':'海南省','渝':'重庆市','川':'四川省','蜀':'四川省','黔':'贵州省','贵':'贵州省','滇':'云南省','云':'云南省','藏':'西藏自治区','陕':'陕西省','秦':'陕西省','甘':'甘肃省','陇':'甘肃省','青':'青海省','宁':'宁夏回族自治区','新':'新疆维吾尔自治区','港':'香港特别行政区','澳':'澳门特别行政区','台':'台湾省'}

a=input('请输入我国34个省级行政单位的简称(键)，然后此程序会输出这个简称的全称(值):')
if a in Dict:
    print(Dict[a])
else:
    print('您输入的键不存在！')
