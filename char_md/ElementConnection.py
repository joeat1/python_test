#coding=utf-8
from Element import Element
from utils import settings
class ElementConnection():
    '''
    元素组合器，用于调整和组装, 返回元素类型
    '''
    def adjust_content(self, content, length):
        '''
        使得conten的每一个字符串长度是一样的
        '''
        for i in range(len(content)):
            content[i] += (length - len(content[i])) * ' '
        
        return content
    
    def get_new_lines(self, elem_list):
        '''
        获取多个元素中行数的最大值，用于水平合并时得到新生成的content行数
        '''
        new_lines = 0
        for elem in elem_list:
            if elem.get_lines() > new_lines:
                new_lines = elem.get_lines()
        return new_lines
    
    def get_new_length(self, elem_list):
        '''
        获取元素列表中，长度的最大值作为新元素的长度
        '''
        new_length = 0
        for elem in elem_list:
            if elem.get_length() > new_length:
                new_length = elem.get_length()
        return new_length
    
    
    def connect_horiz(self, *elem_list):
        '''
        param: elem_line： [elem1,elem2]   --->  new_content:[ elem1   elem2]
        Usage: connect_horiz([['deaf', 'whom'],['all', 'var', 'due']])
        Example:
            deafall
            whomvar
                due
        '''
        new_lines = self.get_new_lines(elem_list)
        
        new_content = [''] * new_lines
        for elem in elem_list:
            elem.set_lines(new_lines)
            for i in range(new_lines):
                new_content[i] += elem.content[i]
        new_elem = Element( new_content )
        return new_elem
    
    def connect_verti(self, *elem_list):
        '''
        param: elem_list： [elem1,elem2]   --->  new_content:[ elem1 ]  
                                                             [ elem2 ]
        Usage: connect_horiz([['deaf', 'whom'],['all', 'var', 'due']])
        Example:
            deaf
            whom
            all 
            var 
            due 
        '''
        new_content = []
        new_length = 0
        for elem in elem_list:
            new_content += elem.content
            if new_length < elem.length:
                new_length = elem.length
        
        #adjust content to the same length
        new_content = self.adjust_content(new_content, new_length)
        new_elem = Element(new_content)
        return new_elem