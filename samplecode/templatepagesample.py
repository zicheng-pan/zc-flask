#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))
