#coding=utf-8
import math

from utils import settings

class Element():
    '''
    元素模块，记录元素信息，调用对应的生成函数
    lines, length: 占据的长度和行数
    content： 每一行的信息保留在列表中的一个元素中，列表中每个元素的长度是相同的
    '''
    def __init__(self, content = [], padding = 0):
        #self.shape = [0, 0] # lines, length [self.lines, self.length]
        self.lines = 0
        self.length = 0
        self.content = []
        self.padding = padding
        self.set_content(content)
        self.set_padding(padding)
    
    def get_lines(self):
        return self.lines
    def get_length(self):
        return self.length
    def get_shape(self):
        return [self.lines, self.length]
    def get_padding(self):
        return self.padding
    
    def check_content(self, content):
        lines = len(content)
        if lines >0:
            length = len(content[0])
            for line in content:
                if len(line) != length:
                    logging.warning("[-] The format of content is invalide")
                    return -1, -1
            return lines, length
        return -1, -1
        
    def set_content(self, content):
        '''
        content: list
        #need to calcule the shape of content
        '''
        lines, length = self.check_content(content)
        if length != -1:
            self.lines = lines
            self.content = content
            self.length = length
    
    def set_padding(self, padding, direction=settings.LeftRight):
        if padding < 0:
            logging.warning("[-] Padding can not be negative")
            return 
        if direction == settings.LeftRight:
            self.length += padding * 2
            for i in range(len(self.content)):
                self.content[i] = ' '*padding + self.content[i] + ' '*padding
        elif direction == settings.Left:
            self.length += padding
            for i in range(len(self.content)):
                self.content[i] = ' '*padding + self.content[i]
        elif direction == settings.Right:
            self.length += padding
            for i in range(len(self.content)):
                self.content[i] = self.content[i] + ' '*padding
        elif direction == settings.Up:
            self.lines += padding
            self.content = [' ' * self.length] * padding + self.content
        elif direction == settings.Down:
            self.lines += padding
            self.content =  self.content + [' ' * self.length] * padding
        elif direction == settings.UpDown:
            self.lines += padding * 2
            self.content =  [' ' * self.length]  + self.content + [' ' * self.length]
        elif direction == settings.All:
            for i in range(len(self.content)):
                self.content[i] = ' '*padding + self.content[i] + ' '*padding
            self.content = [' ' * self.length]  + self.content + [' ' * self.length]
            self.lines += padding * 2
            self.length += padding * 2
        
    def set_length(self, length):
        if length < 0:
            logging.warning('[-] length can not be negative')
            return 
        elif self.length > length:
            result = self.connect()
            self.lines = math.ceil( len(result) / length )
            for i in range(self.lines):
                begin = i*length
                end = min(i*length + length, len(result))
                self.content[i] = result[begin : end]
            self.length = length
        else:
            half_length = math.ceil((length - self.length)/2)
            for i in range(self.lines):
                self.content[i] = ' ' * half_length + self.content[i] + ' ' * (length - self.length - half_length) 
            self.length = length
    def set_lines(self, lines):
        if lines < 0:
            logging.warning('[-] length can not be negative')
            return 
        elif  self.lines > lines:
            result = self.connect()
            self.length = math.ceil( len(result) / lines )
            self.lines = lines
            for i in range(self.lines):
                begin = i * self.length
                end = min(i * self.length + self.length, len(result))
                self.content[i] = result[begin : end]
        
        else:
            half_lines = math.ceil((lines - self.lines)/2)
            self.content = [' ' * self.length] * half_lines + self.content + [' ' * self.length] * (lines - self.lines - half_lines)
            self.lines = lines
            print (self.content)
    
    def reverse(self):
        for i in range(self.lines):
            content[i] = content[i][::-1]
    
    def connect(self):
        '''
        将元素的content变成一行
        '''
        result = ''
        for line in self.content:
            result += line
        return result
    
    def display_content(self):
        '''
        将元素的content变成列表的输出模式
        '''
        result = ''
        for line in self.content:
            result += line
            result += '\n'
        return result