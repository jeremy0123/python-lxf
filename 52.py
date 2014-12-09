# -*- coding: utf-8 -*-

# struct模块来解决str和其他二进制数据类型的转换。
import struct
# print struct.pack('>I', 10240099) # 无法打印
# '>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# >IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数。
