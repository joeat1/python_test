#coding=utf-8
import math
from Element import Element
from utils import settings
class ElementBuilder():
    '''
    根据类型生成对应的 Element的content, 输出数组
    '''
    
    def adjust_content(self, content, length):
        '''
        使得conten的每一个字符串长度是一样的
        '''
        for i in range(len(content)):
            content[i] += (length - len(content[i])) * ' '
        
        return content
    
    def gen_horiz(self, content_len, character):
        '''
        param:  content_len  字符串长度
                characters   水平字符集
        Usage: gen_horiz(5, '-')
        Example:  
            '---------'
        '''
        return (content_len * character)
    
    def gen_verti(self, content_len, character):
        '''
        param:  content_len  字符串长度
                characters   竖直字符集
        Usage: gen_verti(3, '|')
        Example:  
            '|
             |
             |'
        '''
        return [character] * content_len
    
    def gen_horizend(self, content, *characters):
        '''
        param:  content  字符串
                characters   竖直字符集
        Usage: gen_horizend(content, '\', '/')
        Example:  
                \content/
        '''
        if len(characters)==1:
            return (characters[0] + content + characters[0])
        elif len(characters)==2:
            return (characters[0] + content + characters[1])
        else:
            logging.warning("The args nums is not valide")
            return None
    
    def gen_vertiend(self, content, *characters):
        '''
        param:  content  字符串
                characters   竖直字符集
        Usage: gen_horizend(content, '\\', '/')
        Example:  
                \
                content
                /
        '''
        if len(characters)==1:
            return ([characters[0]] + content + [characters[0]])
        elif len(characters)==2:
            return ([characters[0]] + content + [characters[1]])
        else:
            logging.warning("The args nums is not valide")
            return None
    
    def gen_connectipon(self, length, character='-', elem_output = True):
        '''
        param:  length  character
        Usage: gen_connectipon(10)
        Example:  
                 -------- 
        '''
        result = [self.gen_horizend(self.gen_horiz(length, character), ' ')]
        if elem_output:
            result = Element(result)
        return result
    
    def gen_small_title(self, content, length =4, elem_output = True):
        result = [self.gen_horizend(content, '[' + '-'*length, '-'*length + ']')]
        if elem_output:
            result = Element(result)
        return result
    
    def gen_arrows(self, length=4, direction=settings.Right, elem_output = True):
        '''
        param:  length
        Usage: gen_arrows(10, 1)   5^v 4↑ 3↓ 2<> 1→ 0←
        Example：
             <-------- 
        '''
        if direction == settings.Left:
            result = [self.gen_horizend(self.gen_horiz(length, '-'), '<', ' ')]
        elif direction == settings.Right:
            result = [self.gen_horizend(self.gen_horiz(length, '-'), ' ', '>')]
        elif direction == settings.LeftRight:
            result = [self.gen_horizend(self.gen_horiz(length, '-'), '<', '>')]
        elif direction == settings.Down:
            result = [self.gen_vertiend(self.gen_verti(length, '|'), ' ', 'v')]
        elif direction == settings.Up:
            result = [self.gen_vertiend(self.gen_verti(length, '|'), '^', ' ')]
        elif direction == settings.UpDown:
            result = [self.gen_vertiend(self.gen_verti(length, '|'), '^', 'v')]
        else:
            logging.warning("The args nums is not valide")
            return None
        if elem_output:
            result = Element(result)
        return result
    def gen_rectangle(self, content, character_h='-', character_v='|', lines = 1, elem_output = True):
        '''
        param:  character_v  竖直字符
                character_h   水平字符
        Usage: gen_rectangle(content, '-', '|')
        Example: -------
                |content|
                 -------
        '''
        content_len = math.ceil( len(content)/lines )
        result = []
        # fill with space
        content += (content_len * lines - len(content)) * ' '
        result.append( self.gen_horizend(self.gen_horiz(content_len, character_h), ' ') )
        for i in range(lines):
            begin = i * content_len
            end = i*content_len+content_len
            result.append( self.gen_horizend(content[begin:end], character_v) )
        result.append( self.gen_horizend(self.gen_horiz(content_len, character_h), ' ') )
        #result = self.adjust_content(result, content_len+2)
        if elem_output:
            result = Element(result)
        return result
        
    def gen_triangle(self, content, character='*', elem_output = True):
        '''
        param:  content
                character  包裹的字符
        Usage: gen_triangle(content, '*')
        Example:    *
                   * *    1
                  *   *   3
                 *bad  *  5
                  *   *
                   * *
                    *
        '''
        content = content+' ' if (len(content)%2==0) else content
        content_len = len(content) + 2
        result = []
        # gen using petty func
        result.append( self.gen_horizend(character, ' ' *(int(content_len/2)) ) )
        
        for num in range(1, int(content_len/2)):
            result.append( self.gen_horizend(self.gen_horizend(' ' * (num*2-1) ,character), ' '*(int(content_len/2) - num) ) )
        
        result.append( self.gen_horizend(content, character) )
        
        for num in range(int(content_len/2), 1, -1):
            result.append( self.gen_horizend(self.gen_horizend(' ' * (num*2-1) ,character), ' '*(int(content_len/2) - num) ) )
        
        result.append( self.gen_horizend(character, ' ' *(int(content_len/2)) ) )
        if elem_output:
            result = Element(result)
        return result
        
    def gen_bracket(self, unit_length, unit_num, direction=settings.Right, elem_output = True):
        result = []
        if unit_length<0 or unit_num<2:
            logging.warning("The unit_length can not be negative, unit_num cannot be lower than two")
            return None
        if direction == settings.Left:
            # _
            #  |
            #  |
            # _|__
            #  |
            # _|
            result=['_   ']
            for i in range(unit_num-1):
                result += [' |  '] * (unit_length-1)
                result.append('_|  ')
            mid_point = (math.ceil( unit_length*(unit_num-1) /2))
            result[mid_point] = result[mid_point][:-2] + '__'
        elif direction == settings.Right:
            #   _
            #  |
            #__|_
            #  |
            #  |_
            result=['   _']
            for i in range(unit_num-1):
                result += ['  | '] * (unit_length-1)
                result.append('  |_')
            mid_point = (math.ceil( unit_length*(unit_num-1) /2))
            result[mid_point] = '__' + result[mid_point][2:]
        elif direction == settings.Down:
            # ____|____
            #|    |    |
            tmp = self.gen_horizend(unit_length*' ' , '|')
            for i in range(unit_num-2):
                tmp += self.gen_horizend( unit_length*' ' , '', '|')
            left_part = (math.ceil( unit_length*(unit_num-1) /2) + math.ceil(unit_num/2) - 2 ) * '_'
            result.append( self.gen_horizend(self.gen_horizend('|',left_part, (len(tmp) -len(left_part) - 3) * '_'), ' ' ) )
            result.append(tmp)
        elif direction == settings.Up:
            #|____|____|  unit_num = 3
            #     |       unit_length = 4
            tmp = self.gen_horizend(unit_length*'_' , '|')
            for i in range(unit_num-2):
                tmp += self.gen_horizend( unit_length*'_' , '', '|')
            result.append(tmp)
            left_part = (math.ceil( unit_length*(unit_num-1) /2) + math.ceil(unit_num/2) ) *' '
            result.append( self.gen_horizend('|',left_part, (len(tmp) -len(left_part) - 1) * ' ') )
        else:
            logging.warning("The args nums is not valide")
            return None
        if elem_output:
            result = Element(result)
        return result
    
    def gen_bracket4elem(self, direction, *elem_list, elem_output = True):
        result = []
        unit_length = 0
        if direction == settings.Left:
            result=['_   ']
            for elem in elem_list[:-1]:
                result += [' |  '] * (elem.lines - 1)
                result.append('_|  ')
                unit_length += elem.lines
            mid_point = (math.ceil( unit_length /2))
            result[mid_point] = result[mid_point][:-2] + '__'
        elif direction == settings.Right:
            #   _
            #  |
            #__|_
            #  |
            #  |_
            result=['   _']
            for elem in elem_list[:-1]:
                result += ['  | '] * (elem.lines - 1)
                result.append('  |_')
                unit_length += elem.lines
            mid_point = (math.ceil( unit_length /2))
            result[mid_point] = '__' + result[mid_point][2:]
        elif direction == settings.Down:
            # ____|____
            #|    |    |
            tmpd = ''
            tmpu = ''
            first_left = math.ceil( elem_list[0].length / 2)
            last_right = math.ceil( elem_list[-1].length / 2)
            for elem in elem_list:
                left_length = math.ceil( elem.length / 2)
                tmpd += left_length * ' ' + '|' + (elem.length - left_length)*' '
                tmpu += (elem.length+1) * '_'
                unit_length += elem.length
            
            mid_point = (math.ceil( unit_length /2))
            
            tmpu = ' '*(first_left+1) + tmpu[first_left+1:]
            tmpu = tmpu[:-last_right] + ' '*last_right
            tmpu = tmpu[:mid_point+1] + '|' +tmpu[mid_point+2:]
            
            result.append(tmpu)
            result.append(tmpd)
        elif direction == settings.Up:
            #|____|____|  unit_num = 3
            #     |       unit_length = 4
            tmpd = ''
            tmpu = ''
            first_left = math.ceil( elem_list[0].length / 2)
            last_right = math.ceil( elem_list[-1].length / 2)
            for elem in elem_list:
                left_length = math.ceil( elem.length / 2)
                tmpu += left_length * '_' + '|' + (elem.length - left_length)*'_'
                tmpd += (elem.length+1) * ' '
                unit_length += elem.length
            
            mid_point = (math.ceil( unit_length /2))
            tmpu = ' '*first_left + tmpu[first_left:]
            tmpu = tmpu[:-last_right+1] + ' '*(last_right-1)
            tmpd = tmpd[:mid_point+1] + '|' +tmpd[mid_point+2:]
            
            result.append(tmpu)
            result.append(tmpd)
        else:
            logging.warning("The args nums is not valide")
            return None
        if elem_output:
            result = Element(result)
        return result