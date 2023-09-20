import time
import uiautomator2 as u2

# 连接到设备
d = u2.connect()


# 使用 uiautomator2 查找要拖动的元素
element_to_drag = d(
    resourceId='com.viewsonic.sidetoolbar:id/iv_annotation_bar_right')


# 定义拖动的目标位置（屏幕的右边缘）
target_x = d.info['displayWidth'] - 1  # 屏幕的宽度减 1，即最右侧的位置
target_y = d.info['displayHeight'] - 1
element_bounds = element_to_drag.info['bounds']

# 计算中心点的坐标
center_x = (element_bounds['left'] + element_bounds['right']) // 2
center_y = (element_bounds['top'] + element_bounds['bottom']) // 2


d.drag(center_x, center_y, target_x, 0)
