import re

def filter_screen_size(text:str) ->float:
    regex = re.compile(r'^\s*([\d.]+)')
    m = regex.match(text)
    if m:
        size_str = m.group(1)
        return size_str
    
text = '15.6" (39.62 см)'
screen_size = filter_screen_size(text)
print(screen_size)