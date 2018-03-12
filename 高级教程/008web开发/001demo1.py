#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

# urlparse 模块
import urlparse

# 切分url
parse_result = urlparse.urlparse('http://www.baidu.com/2018/02/index.html?id=2&name=wuyb&date=2018-1-1#tech')

print parse_result

#拼接url
unparse_result = urlparse.urlunparse(urlparse.urlparse('http://www.baidu.com/2018/02/index.html?id=2&name=wuyb&date=2018-1-1#tech'))
print unparse_result

#相对路径拼接,urlparse.urljoin(baseurl,newurl,allowFlag=None)
print urlparse.urljoin('http://baidu.com/2018/index.html?id=2','2018/lib.index.html?id=3')

# urllib 模块
import urllib
page =urllib.urlopen('http://baidu.com')

result = urllib.urlretrieve('http://baidu.com',filename='高级教程/008web开发/baidu.html')
print result

# urlib.quote url编码
print urllib.quote('http://baidu.com?name=哈哈&date=2017-2-2')

# urllib.quote_plus url编码（类似urllib.quote，但是会额外将空格编码成'+'号
print urllib.quote('http://baidu.com?cand=2+2&name=lin li&age=1')
print urllib.quote('http://baidu.com?cand=2+2&name=lin li&age=1')

# url.unquote url解码
# url.unquote_plus解码

# urlliburlencode() 将字典编译成 name=value&....形式的字符串
dict={'name':'lin li','age':15}
print urllib.urlencode(dict)