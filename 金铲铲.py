import cv2
import pyautogui
import time
import numpy as np  # 导入numpy库并设置别名np
import random
import keyboard
def readimg(img1,img2):
    # 加载要查找的模板图像（这里假设你已经有了要点击区域的截图作为模板）
    template1 = cv2.imread(img1, cv2.IMREAD_COLOR)
    template2 = cv2.imread(img2, cv2.IMREAD_COLOR)

    # 确保模板图像加载成功
    if template1 is None or template2 is None:
        print("模板图像加载失败，请检查文件路径和文件名。")
        exit(1)

    # 分别获取两个模板图像的尺寸
    template1_height, template1_width, _ = template1.shape
    template2_height, template2_width, _ = template2.shape

    last = ()

    while True:
        if keyboard.is_pressed(']'):
            return
        # 截取当前屏幕图像
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # 对template1进行模板匹配
        result1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
        print("对template1进行模板匹配")
        # 对template2进行模板匹配
        result2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
        print("对template2进行模板匹配")
        # 设置匹配阈值，这里假设阈值为0.8，你可以根据实际情况调整
        threshold = 0.8
        random1 = random.randint(0,50)
        random2 = random.randint(0,50)
        if keyboard.is_pressed('d'):
            last=()

        # 检查template1是否匹配成功
        if max_val1 >= threshold:
            print("匹配成功")
            # 找到匹配的位置，计算点击的坐标
            click_x1 = max_loc1[0] + template1_width // 2
            click_y1 = max_loc1[1] + template1_height // 2
            if last!=(click_x1,click_y1):
                if random1 > 25:
                    # 模拟鼠标点击操作
                    pyautogui.click(click_x1 - random1, click_y1 + random2)
                    print(f"在坐标 ({click_x1}, {click_y1}) 处点击模板1")
                else:
                    # 模拟鼠标点击操作
                    pyautogui.click(click_x1, click_y1)
                    print(f"在坐标 ({click_x1 - random2}, {click_y1 + random1}) 处点击模板1")
                    # time.sleep(0.1)
                # last = (click_x1, click_y1)


        # 检查template2是否匹配成功
        if max_val2 >= threshold:
            # 找到匹配的位置，计算点击的坐标
            click_x2 = max_loc2[0] + template2_width // 2
            click_y2 = max_loc2[1] + template2_height // 2
            if random1>25:
                # 模拟鼠标点击操作
                pyautogui.click(click_x2-random1, click_y2+random2)
                print(f"在坐标 ({click_x2}, {click_y2}) 处点击模板1")
            else:
                # 模拟鼠标点击操作
                pyautogui.click(click_x2, click_y2)
                print(f"在坐标 ({click_x2-random2}, {click_y2+random1}) 处点击模板1")
                #time.sleep(0.1)

        # 每隔一段时间检查一次屏幕，这里设置为1秒
        time.sleep(0.1)
running = False  # 状态标志，表示是否在运行中
if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('['):
            if not running:
                running = True
                print("开始执行")
                readimg('3.png', 'like2.png')
            else:
                print("已经在运行中")
            # time.sleep(0.5)  # 防止多次触发
        elif keyboard.is_pressed(']'):
            if running:
                running = False
                print("已暂停")
            else:
                print("当前已是暂停状态")
            # time.sleep(0.5)

