
#opencv 读取图片默认bgr！！！
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx
    ''' 
    上面的h,s,v值的范围分别是0-360, 0-1, 0-1
    openCV中，H,S,V的范围是0-180,0-255,0-255
    所以需要转换    
    '''
    H = h / 2
    S = s * 255.0
    V = v * 255.0
    return H, S, V
