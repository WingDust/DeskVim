# debugger 
import pysnooper

from pynput import mouse , keyboard

from pprint import pprint

from ahk import AHK
from ahk.window import Window

import win32gui,win32api

import ctypes
# from ctypes import Stucture,c_long

# global var
ahk = AHK()

## 
## class POINT(Stucture):
##     _fields_ = [("x",c_long),("y",c_long)]
## 


# li= win32api.GetKeyboardLayout()

# s=win32api.GetKeyState()

# sta=win32api.GetKeyboardState()
# key=win32api.GetKeyboardLayoutName()

# [如何利用Python和win32编程避免重复性体力劳动（一）——开始、FindWindow和FindWindowE](https://blog.csdn.net/seele52/article/details/17504925)
# [pythonwin-win32gui 显示，子窗口查找和遍历](https://blog.csdn.net/davidsu33/article/details/51330036)

def find_idxSubHandle(pHandle,winClass,index=0):
    """
    已知子窗口的窗体类名
    寻找第index号个同类型的兄弟窗口
    """
    assert type(index) == int and index >= 0
    handle = win32gui.FindWindowEx(pHandle,handle,winClass,None)
    while index > 0:
        handle = win32gui.FindWindowEx(pHandle,handle,winClass,None)
        index -= 1
    return handle

def find_subHandle(pHandle,winClassList):
    """
    递归寻找子窗口的句柄
    pHandle是祖父窗口的句柄
    winClassList是各个子窗口的class列表，父辈的list-index小于子辈
    """
    assert type(winClassList) == lit
    if len(winClassList) == 1:
        return find_idxSubHandle(pHandle,winClassList[0][0],winClassList[0][1])
    else:
        pHandle = find_idxSubHandle(pHandle,winClassList[0][0],winClassList[0][1])
        return find_subHandle(pHandle,winClassList[1:])


def gbk2utf8(s):
    #return s.decode('gbk').encode('utf-8')
    return s.encode('utf-8')
 
def show_window_attr(hWnd):
    '''
    显示窗口的属性
    :return:
    '''
    if not hWnd:
        return
 
    #中文系统默认title是gb2312的编码
    # 窗口必须有WS_VISBLE样式，并不在处于窗口最小化
    if (win32gui.IsWindowVisible(hWnd) and not win32gui.IsIconic(hWnd) and win32gui.IsWindowEnabled(hWnd)) and ctypes.windll.user32.GetAltTabInfoW(hWnd)==0:
        title = win32gui.GetWindowText(hWnd)
        title = gbk2utf8(title)
        clsname = win32gui.GetClassName(hWnd)
        # (l,u,r,d) = win32gui.GetWindowRect(hWnd)
        print(win.title)
        if title !=b'':
            print(l,u,r,d)
            print ('窗口句柄:%s ' % (hWnd))
            print ('窗口标题:%s' % (title))
            print ('窗口类名:%s' % (clsname))
            print ('end')
 
def show_windows(hWndList):
    for h in hWndList:
        show_window_attr(h)


class FaceGenWindow(object):
    def __init__(self,WinClasss,Wintitle,fgFilePath=None):
        self.Mhandle = win32gui.FindWindow(WinClasss,Wintitle)
        print ("FaceGen initialization compeleted")


find = FaceGenWindow(None,"Neovim")

print(find)
print(dir(find))
print(find.Mhandle)

# subHandle = find_subHandle(find.Mhandle,)
windows = []
print(win32gui.EnumChildWindows(find.Mhandle,lambda hWnd,param:param.append(hWnd),windows))
print(windows)
# subHandle = win32gui.FindWindowEx(find.Mhandle,0,None,None)


def demo_top_windows():
    '''
    演示如何列出所有的顶级窗口
    :return:
    '''
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    show_windows(hWndList)
 
    return hWndList

def demo_child_windows(parent):
    '''
    演示如何列出所有的子窗口
    :return:
    '''
    if not parent:
        return
 
    hWndChildList = []
    win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)
    show_windows(hWndChildList)
    return hWndChildList


# 使用 pynput 的全局监听键会使程序阻塞，在热键上可以很好的执行
    # windows = []
    # print(win32gui.EnumChildWindows(find.Mhandle,lambda hWnd,param:param.append(hWnd),windows))
    # print(windows)
    #demo_top_windows()
    #demo_child_windows(find.Mhandle)






## def keyboard_listener():
##     global listener
##     def on_press(key):
##         print('press',key,'2')
## 
## 
##     def on_release(key):
##         print('release',key,'3')
## 
## 
##     def win32_event_filter(msg,data):
##         print(msg,data.vkCode,'1')
##         print(ahk.active_window.title)
##         # title = win32gui.GetWindowText(hWnd)
##         if(msg==257 or msg ==256 ) and data.vkCode == 27:
##             listener._suppress=True
##         else:
##             listener._suppress=False
##         return True
## 
##     return keyboard.Listener(
##             #on_press=on_press,
##             #on_release=on_release,
##             win32_event_filter=win32_event_filter,
##             suppress=False
##             )
## 
## 
## 
## listener = keyboard_listener()



#if __name__ == '__main__':
#    with listener as ml:
#        ml.join()









 
