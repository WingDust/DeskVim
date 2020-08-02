
import win32gui
from AltTab import AltTab

from pynput import keyboard as kb

import time

import keyboard

import threading


status=0

def arrow_remapp():
    keyboard.remap_key('h','left')
    keyboard.remap_key('j','down')
    keyboard.remap_key('k','up')
    keyboard.remap_key('l','right')

def unhook_arrow():
    keyboard.unhook_key('h')
    keyboard.unhook_key('j')
    keyboard.unhook_key('k')
    keyboard.unhook_key('l')

def on_activate_exit():
    global status
    print('current status:',status)
    if status==1 or status==4:
        unhook_arrow()
        status=2
        print('current status 已修改成:',status)
        return
    if status==2:
        keyboard.remap_key('h','left')
        keyboard.remap_key('j','down')
        keyboard.remap_key('k','up')
        keyboard.remap_key('l','right')
        status=4
        print('current status 已修改成:',status)
        return

# 1 为刚进入设置并成功 2 为进入设置后取消,已完成 3 为其它的退出了这个桌面

def  on_activate_WinD():
    time.sleep(0.003) # delay execute 300ms
    flag = AltTab.list_alttab_windows()
    global status
    print(flag)
    if flag:
        print('将 hjkl 设置为 arrow flag:',flag)
        arrow = threading.Thread(target=arrow_remapp,name="arrow")
        arrow.start()
        status=1
    else:
        print('不能 hjkl 设置为 arrow flag:',flag)



def quit():
    global status
    if status==1 or status == 4 :
        unhook_arrow()
        status = 3
        print('已将 status :',status)


# The key combination to check
COMBINATION = {kb.Key.alt_l, kb.Key.tab}

# The currently active modifiers
current = set()

# 设立一个状态来确定是否这个键被 hold
# 
alt_status = 0

def on_press(key):
    print('press:',key,'\n')
    if key in COMBINATION:
        current.add(key) # auto deduplication
        if all(k in current for k in COMBINATION):
            global alt_status
            alt_status=1
            print('All modifiers active!')


def on_release(key):
    print('release:',key,'\n')
    if alt_status==1:
        if key ==kb.Key.alt_l:
            # global alt_status
            # alt_status=2
            print('将alttab中的设置为 还原')
            quit()
    # if not current: # 当它为空set 还原
    try:
        current.remove(key)
    except KeyError:
        pass


# with kb.GlobalHotKeys({
    # '<cmd>+d': on_activate_WinD,
    # '<esc>': on_activate_exit,
    # '<ctrl>+<shift>+<esc>':quit,
    # '<alt>+<tab>':quit
    # }) as h:
 # h.join()


listener = kb.Listener(on_press=on_press, on_release=on_release)
listener.start()


h = kb.GlobalHotKeys({'<cmd>+d':on_activate_WinD,'<esc>':on_activate_exit})
h.start()


listener.join()
h.join()


keyboard.add_hotkey('ctrl+shift+esc',quit)
# keyboard.add_hotkey('alt+tab',quit)
keyboard.wait()

