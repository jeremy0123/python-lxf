# -*-coding: utf-8 -*-

# base64
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

# 标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url
#  safe"的base64编码，其实就是把字符+和/分别变成-和_：
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
# print base64.urlsafe_b64decode('abcd--__')

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:
# 'abcd' -> 'YWJjZA=='
# 自动去掉=:
# 'abcd' -> 'YWJjZA'
# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
