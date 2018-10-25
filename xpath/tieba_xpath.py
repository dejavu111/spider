import os
import urllib.request
from lxml import etree
class Spider:
    def __init__(self):
        self.tiebaName = input('请输入要访问的贴吧：')
        self.beginPage = int(input('请输入起始页:'))
        self.endPage = int(input('请输入终止页：'))

        self.url = 'http://tieba.baidu.com/f'
        self.ua_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'}

        # 图片编号
        self.userName = 1

    def tiebaSpider(self):
        for page in range(self.beginPage,self.endPage+1):
            pn = (page-1)*50 # page number
            word = {'pn':pn,'kw':self.tiebaName}
            word = urllib.parse.urlencode(word)
            myUrl = self.url + '?' + word

            # 示例：http://tieba.baidu.com/f? kw=%E7%BE%8E%E5%A5%B3 & pn=50
            # 调用 页面处理函数load_Page
            # 并且获取页面所有帖子链接
            links = self.loadPage(myUrl)

    # 读取页面内容
    def loadPage(self,url):
        print(url)
        req = urllib.request.Request(url,headers=self.ua_header)
        html = urllib.request.urlopen(req).read()
        print(html)
        # 解析html为HTML文档
        selector = etree.HTML(html)
        with open('b.txt','wb') as f:
            f.write(html)
        # 抓取当前页面的所有帖子url的后半部分，也就是帖子编号(每个帖子)
        # http://tieba.baidu.com/p/4884069807里的 “p/4884069807”
        # <div class="threadlist_lz clearfix">
        #                 <div class="threadlist_title pull_left j_th_tit ">
        #
        #
        #     <a rel="noreferrer" href="/p/5922379606" title="谁可以帮忙写一下硕士论文啊" target="_blank" class="j_th_tit " clicked="true">谁可以帮忙写一下硕士论文啊</a>
        # </div><div class="threadlist_author pull_right">
        #     <span class="tb_icon_author " title="主题作者: WXscy5201314xt" data-field="{&quot;user_id&quot;:3106988625}"><i class="icon_author"></i><span class="frs-author-name-wrap"><a rel="noreferrer" data-field="{&quot;un&quot;:&quot;WXscy5201314xt&quot;}" class="frs-author-name j_user_card " href="/home/main/?un=WXscy5201314xt&amp;ie=utf-8&amp;id=51e2575873637935323031333134787430b9&amp;fr=frs" target="_blank">WXscy5201314xt</a></span><span class="icon_wrap  icon_wrap_theme1 frs_bright_icons "></span>    </span>
        #     <span class="pull-right is_show_create_time" title="创建时间">12:43</span>
        # </div>
        #             </div>
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        links = selector.xpath('//div[@class="threadlist_lz clearfix"]')
        print(links)
        # links类型为etreeElementString列表
        # 遍历列表，并且合并成一个帖子地址，调用图片处理函数loadImage
        for link in links:
            link = 'http://baidu.com' + link
            self.loadImages(link)

    # 获取图片
    def loadImages(self,link):
        req = urllib.request.Request(link,headers=self.ua_header)
        html = urllib.request.urlopen(req).read()

        selector = etree.HTML(html)

        imagesLinks = selector.xpath('//img[@class="BDE_Image"]/@src')
        #属性有确定值直接[@属性名=“属性值”] 用作筛选
        #没有确定值/@属性名


        # 依次取出图片路径，下载保存
        for imagesLink in imagesLinks:
            self.writeImages(imagesLink)

    def writeImages(self,imagesLink):
        print(imagesLink)
        print('正在存储文件%d...' %self.userName)

        # 1.打开文件，返回一个对象
        with open('./images/'+str(self.userName)+'.png','wb') as f:
            images = urllib.request.urlopen(imagesLink).read()
            f.write(images)
        self.userName = self.userName+1

if __name__ == "__main__":
    mySpider = Spider()
    mySpider.tiebaSpider()
