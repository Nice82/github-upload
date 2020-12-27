class Settings():
    """设置"""

    def __init__(self):
        """一般设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (233, 233, 233)
        self.screen_resolution = (1200, 800)

        #自机设置
        self.ship_speed_high = 0.5
        self.ship_speed_low = 0.2
        self.ship_speed = self.ship_speed_high