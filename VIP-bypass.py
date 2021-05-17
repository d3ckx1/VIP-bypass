# coding=utf-8

import tkinter as tk
import tkinter.messagebox
import webbrowser as wb


class player:
    def __init__(self):
        self.root = tk.Tk()  # 初始化窗口
        self.root.title('VIP视频免费播放软件_v1.1 -by d3ckx1')  # 窗口名称
        self.root.geometry("700x400")  # 设置窗口大小
        # 设置窗口是否可变，宽不可变，高可变，默认为True
        self.root.resizable(width=True, height=True)

        # 创建一个顶级菜单
        self.menu = tk.Menu(self.root)
        # 创建另一个下拉菜单“帮助”，然后将它添加到顶级菜单中
        self.helpmenu = tk.Menu(self.menu, tearoff=0)
        self.helpmenu.add_command(label='帮助文档', command=self.about)
        self.helpmenu.add_command(label='作者信息', command=self.zzxx)
        self.helpmenu.add_command(label="退出", command=self.root.quit)
        self.menu.add_cascade(label='帮助(H)', menu=self.helpmenu)
        # 显示菜单
        self.root.config(menu=self.menu)

        self.val = tk.StringVar(value='')
        self.label1 = tk.Label(self.root, text='视频播放通道')
        self.label1.place(x=20, y=20, width=100, height=20)
        self.Radio = tk.IntVar(value=1)
        self.Radio1 = tk.Radiobutton(self.root, variable=self.Radio, value=0, text='视频通道1')
        self.Radio2 = tk.Radiobutton(self.root, variable=self.Radio, value=1, text='视频通道2')
        self.Radio3 = tk.Radiobutton(self.root, variable=self.Radio, value=2, text='视频通道3')
        self.Radio4 = tk.Radiobutton(self.root, variable=self.Radio, value=3, text='视频通道4')
        self.Radio1.place(x=150, y=20, width=100, height=20)
        self.Radio2.place(x=250, y=20, width=100, height=20)
        self.Radio3.place(x=350, y=20, width=100, height=20)
        self.Radio4.place(x=450, y=20, width=100, height=20)

        self.val1 = tk.StringVar(value='https://www.iqiyi.com/v_19rqpqcijk.html#vfrm=19-9-0-1')
        self.link = tk.Label(self.root, text='视频播放链接')
        self.link.place(x=20, y=60, width=100, height=20)
        self.movie = tk.Entry(self.root, textvariable=self.val1)
        self.movie.place(x=130, y=60, width=450, height=25)

        self.warn = tk.Label(self.root, text='将视频链接复制到框内，点击“播放VIP视频”')
        self.warn.place(x=130, y=90, width=400, height=20)
        self.val2 = tk.StringVar
        self.start = tk.Button(self.root, text='播放VIP视频', command=self.Button)
        self.start.place(x=280, y=140, width=80, height=30)
        self.start1 = tk.Button(self.root, text='爱奇艺', command=self.openaqy)
        self.start1.place(x=100, y=200, width=70, height=30)
        self.start2 = tk.Button(self.root, text='腾讯视频', command=self.opentx)
        self.start2.place(x=200, y=200, width=80, height=30)
        self.start3 = tk.Button(self.root, text='优酷视频', command=self.openyq)
        self.start3.place(x=300, y=200, width=80, height=30)
        self.b1 = tk.Button(self.root, text='芒果TV', command=self.openmg)
        self.b1.place(x=400, y=200, width=80, height=30,)
        self.root.mainloop()

    def Button(self):
        url = 'http://z1.m1907.cn/?jx=' if self.val1.get() else 'https://v.znb.me/?url=' if self.val2.get() else 'http://17kyun.com/api.php?url=' if self.val3.get() else 'http://z1.m1907.cn/?jx='
        
        yget = self.movie.get()
        wb.open(url + yget)  # 打开浏览器进行播放

    def openaqy(self):
        wb.open('http://www.iqiyi.com')

    def opentx(self):
        wb.open('http://v.qq.com')

    def openyq(self):
        wb.open('http://www.youku.com/')

    def openmg(self):
        wb.open('https://www.mgtv.com/')

    def about(self):
        abc = '''
                经过测试 ,支持站点:

                爱奇艺 腾讯 优酷 土豆 芒果 乐视 搜狐 PPTV 华数TV 风行 咪咕 哔哩哔哩 ACfun 暴风 CCTV CNTV 
                范特西 9i广场舞 搜狐自媒体 M1905视频 看看视频 27盘 虎牙直播 全民直播 战旗直播 人人视频 爆米花 
                今日头条 天翼视频 糖豆视频 龙珠视频 快手视频 一直播 新浪视频 360小视频 熊猫TV 斗鱼TV 花椒直播 
                网易公开课 音悦台 秒拍网 美拍网 爱拍 凤凰视频 梨视频 微录客 人民微视频 17173视频 
                优米视频 m3u8 mp4视频 微博视频 YY视频 私有云资源
                
                '''
        tkinter.messagebox.showinfo(title='帮助文件', message=abc)

    def zzxx(self):
        msg = '''
                作者：d3ckx1
                Vx: D3ck_cn
                '''
        tkinter.messagebox.showinfo(title='联系方式', message=msg)


player()
