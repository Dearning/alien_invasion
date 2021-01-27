#添加新功能 新设定(setting)
class Settings():
    """ 存储所有 "外星人入侵" 的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置
        """
        #screen setting 屏幕设置
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)