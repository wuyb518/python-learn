#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

from django.http import HttpResponse
from TestModel.models import Test

# 数据库操作
def testdb(request):
    # test1=Test(name='runoob')
    # test1.save()
    # return HttpResponse('<p>数据添加成功</p>')

    # 初始化
    response=''
    response1=''

    list=Test.objects.all()

    response2=Test.objects.filter(id=1)

    response3=Test.objects.get(id=1)

    Test.objects.order_by('id')

    Test.objects.filter(name='runoob').order_by('id')

    for x in list:
        response1+=x.name +' '
    response=response1
    return HttpResponse(r'<p>%s</p>' % response)
