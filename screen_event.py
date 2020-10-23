import cv2


def takeclick(event, x,y, flag, params):
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        from main import img
        print(x,y)
        print(img[y][x])
        blue, green, red = img[y][x]
        print('red: %d' % red)
        print('green: %d' % green)
        print('blue: %d' % blue)
        
        