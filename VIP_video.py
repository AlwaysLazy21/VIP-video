import webbrowser

url_map = {
    1: 'https://jx.playerjy.com/?url=',
    2: 'https://video.stkey.top/api1/?url=',
    3: 'https://video.stkey.top/api2/?url=',
    4: 'https://okjx.cc/?url=',
    5: 'https://jx.bozrc.com:4433/player/?url=',
    6: 'https://www.ckplayer.vip/jiexi/?url=',
    7: 'https://www.8090.la/8090/?url=',
    8: 'http://www.pangujiexi.cc/jiexi.php?url=',
    9: 'https://www.h8jx.com/jiexi.php?url=',
}

bilibili = [1]
tencent = [1, 2, 3, 5, 6, 7, 9]
iqiyi = [1, 5, 6, 7, 9]
youku = [1, 2, 3, 6, 7, 9]
mgtv = [1, 2, 3]

author = '''
    _    _                         _                    ____  _ 
   / \  | |_      ____ _ _   _ ___| |    __ _ _____   _|___ \/ |
  / _ \ | \ \ /\ / / _` | | | / __| |   / _` |_  / | | | __) | |
 / ___ \| |\ V  V / (_| | |_| \__ \ |__| (_| |/ /| |_| |/ __/| |
/_/   \_\_| \_/\_/ \__,_|\__, |___/_____\__,_/___|\__, |_____|_|
                         |___/                    |___/         
'''

if __name__ == '__main__':
    print(author)
    print('----' * 5, 'VIP_video (version = 2.0)', '----' * 5)
    print('Resp Url: https://github.com/AlwaysLazy21/VIP-video')
    print('-' * 67)
    print('Support: bilibili, tencent, iqiyi, youku, mangguo')
    url = input('url: ')

    platform = url.split('.')[1]

    if platform == 'bilibili':
        for it in bilibili:
            video_url = url_map[it] + url
            webbrowser.open(video_url)
    elif platform == 'qq':
        for it in tencent:
            video_url = url_map[it] + url
            webbrowser.open(video_url)
    elif platform == 'iqiyi':
        for it in iqiyi:
            video_url = url_map[it] + url
            webbrowser.open(video_url)
    elif platform == 'youku':
        for it in youku:
            video_url = url_map[it] + url
            webbrowser.open(video_url)
    elif platform == 'mgtv':
        for it in mgtv:
            video_url = url_map[it] + url
            webbrowser.open(video_url)
    else:
        print('Sorry! The video of the platform is not supported yet.')
    input('本项目推荐使用edge浏览器，搭配adguard插件进行食用。')
