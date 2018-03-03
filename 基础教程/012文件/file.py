#!/usr/bin/python
# _*_ coding:UTF-8 _*_
# file.close() 关闭文件如果有写入流,则先flush
# file.flush()
# file.fileno() 返回一个整形的文件描述符,可以用在os模块的read方法等一些底层操作
# file.isatty() 如果文件链接到一个终端瑟呗返回True,否则返回False
# file.next() 返回文件下一样
# file.read([size]) 从文件读取指定的字节数,如果为给定或者为负数则读取所有,如果指定size大于后面的长度,则读取后面所有
# file.readline([size]) 读取整行,包括'\n'字符
# file.readlines([size]) 读取所有行并返回列表,如果给定sizeint>0,则是设置一次读取多少个字节,这是为了减轻读取压力
# file.seek(offset,[,whence]) 设置文件当前位置
# file.tell() 返回文件当前位置
# file.truncate(size) 截取文件,截取的字节同步哦size指定,默认为当前文件位置
# file.write(str) 将字符串写入文件,没有返回值
# file.writelines(sequence) 向文件吸入一个序列字符串列表,如果需要换行则需要自己在每行后面加入换行符
