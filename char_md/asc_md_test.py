#coding=utf-8
'''
  构建由字符集合构建的思维导图模板，方便在文本层面上满足简易画图的需求
  基本元素：大括号，各种括号
  方框，三角形，区域分割线，左右框定，关联，各式方向箭头
  
  弹性模块：输出形式，基本元素生成方式，元素的扩展
'''
import os

from Element import Element
from ElementConnection import ElementConnection
from ElementBuilder import ElementBuilder
from utils import settings

# TODO: 
#       参考网页元素的属性，位置等布置元素内容
#       元素的set_lines和set_length 等需要验证
#       ** 参考字符画的生成方式 **
# 类图
#                              shape content       [[elem1,elem2],[elem3],[elem4]]
#                                                           元素组合
#                                  元素                      模块
#             |                      |                        |
#     --- 解释器【表现需求】---->生成器【表现形式】----->组合器【组合方式】---->展示器【输出格式】--
#    |                                                                                              |
# content                                                                                      pasred(content)
#

if __name__ == '__main__':
    
    builder = ElementBuilder()
    
    title = 'This is a test for the function of ascll text draw'
    title = builder.gen_small_title(title, 5)
    title.set_padding(1, settings.UpDown)
    
    main_content = 'ascll_md'
    main_content = builder.gen_rectangle(main_content, lines = 1)
    
    content1 = 'explain'
    content1 = builder.gen_rectangle(content1, lines = 1)
    
    content2 = 'builder'
    content2 = builder.gen_rectangle(content2, lines = 1)
    
    content3 = 'connection'
    content3 = builder.gen_rectangle(content3, lines = 1)
    
    content4 = 'display model'
    content4 = builder.gen_rectangle(content4, lines = 1)
    
    bracket = builder.gen_bracket4elem(settings.Right, content1, content2, content3, content4)
    
    triangle = builder.gen_triangle('content', '*')
    arrows = builder.gen_arrows(10, settings.Left)
    
    connection = ElementConnection()
    b = connection.connect_verti(connection.connect_horiz(main_content, bracket, connection.connect_verti(content1, content2, content3, content4), arrows, triangle))
    
    b = connection.connect_verti(title, b)
    print(b.display_content())