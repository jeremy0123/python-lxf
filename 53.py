# -*-coding: utf-8 -*-

# hashlib md5 sha1
import hashlib

md51 = hashlib.md5()
md51.update('how to use md5 in python hashlib?')
str1 = md51.hexdigest()
md52 = hashlib.md5()
md52.update('how to use md5 ')
md52.update('in python hashlib?')
str2 =  md52.hexdigest()
print str1
print str2
print str1 == str2

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

#由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

#def calc_md5(password):
#    return get_md5(password + 'the-Salt')
#经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

#但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

#如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
