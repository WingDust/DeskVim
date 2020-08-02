
import win32gui
from AltTab import AltTab

from pynput import  keyboard as kb

import time

import keyboard

import threading
import multiprocessing

import os

print('Main:',os.getpid())

times=0

def arrow_remapp():
    keyboard.remap_key('h','left')
    keyboard.remap_key('j','down')
    keyboard.remap_key('k','up')
    keyboard.remap_key('l','right')

def on_activate_exit():
    print('exit')
    global times
    print(times)
    if times==1 or times==4:
        keyboard.unhook_key('h')
        keyboard.unhook_key('j')
        keyboard.unhook_key('k')
        keyboard.unhook_key('l')
        times=2
        return
    if times==2 or times == 3:
        keyboard.remap_key('h','left')
        keyboard.remap_key('j','down')
        keyboard.remap_key('k','up')
        keyboard.remap_key('l','right')
        times=4
        return

# 1 为刚进入设置并成功 2 为进入设置后取消,已完成 3 为其它的退出了这个桌面

def  on_activate_WinD():
    time.sleep(0.001) # delay execute 100ms
    flag = AltTab.list_alttab_windows()
    global times
    print(flag)
    if flag:
        arrow = threading.Thread(target=arrow_remapp,name="arrow")
        arrow.start()
        times=1


def quit():
    global times
    times = 3

# keyboard.add_hotkey('windows+d',on_activate_WinD)
# keyboard.add_hotkey('esc',on_activate_exit)
# keyboard.add_hotkey('ctrl+shift+esc',quit)
# keyboard.add_hotkey('alt+tab',quit)
# keyboard.wait()

def check_Window(title=None):
    def run_time(func):
        def wrapper():
            hWnd = win32gui.GetActiveWindow()
            ctitle = win32gui.GetWindowText(hWnd)
            print('current windows title:',ctitle)
            title==ctitle ? flag = True : flag= False
            func(flag)
        return wrapper
    return run_time
    

@check_Window(title="任务切换")
def h(flag):
    if flag:


# The key combination to check
COMBINATION = {kb.Key.alt_l, kb.Key.tab}

# The currently active modifiers
current = set()

# 设立一个状态来确定是否这个键被 hold
alt_status = 0

def on_press(key):
    print(1,key,'\n')
    if key in COMBINATION:
        if key == kb.Key.alt_l:
            global alt_status
            alt_status=1
        current.add(key) # auto deduplication
        if all(k in current for k in COMBINATION):
            if alt_status == 2:
                quit()
            print('All modifiers active!')


def on_release(key):
    print(2,key,'\n')
    if key ==kb.Key.alt_l:
        global alt_status
        alt_status=2
    try:
        current.remove(key)
    except KeyError:
        pass

listener = kb.Listener(on_press=on_press, on_release=on_release)
listener.start()


h = kb.GlobalHotKeys({'<cmd>+d':on_activate_WinD,'<esc>':on_activate_exit})
h.start()


listener.join()
h.join()


# with kb.GlobalHotKeys({
    # '<cmd>+d': on_activate_WinD,
    # '<esc>': on_activate_exit,
    # '<alt>+<tab>':quit
    # }) as h:
 # h.join()


    

