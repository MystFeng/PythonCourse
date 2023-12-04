import openpyxl as pyxl
import requests as req
from lxml import etree

new = pyxl.Workbook()
new.save("Excel//douban_content.xlsx")
new_wa = new.active


def main():
    for n in range(0, 9):
        base_url = f"https://movie.douban.com/top250?start={25 * n}&filter="
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/95.0.4638.69 Safari/537.36'}
        douban = req.get(url=base_url, headers=header)
        douban_html = etree.HTML(douban.text)
        # imgsrc是一个列表，存储25个图片的网络地址src
        # numarr是一个列表，存储25个电影的序号
        imgsrc = douban_html.xpath("//div[@class='pic']/a/img/@src")
        numarr = douban_html.xpath("//div[@class='pic']/em/text()")
        titilearr = douban_html.xpath("//div[@class='hd']/a/span[1]/text()")
        desarr = douban_html.xpath("//div[@class='bd']/p[@class='quote']/span/text()")
        print(imgsrc)
        print(numarr)
        print(titilearr)
        print(desarr)
        for i in range(0, len(imgsrc)):
            img = req.get(url=imgsrc[i], headers=header)
            with open(f"Img//{numarr[i] + '.' + titilearr[i]}.jpg", 'wb') as f:
                f.write(img.content)

        for i in range(len(numarr)):
            new_wa.append([numarr[i], titilearr[i], desarr[i]])
        new.save("Excel//douban_content.xlsx")
        print(f"爬取第{n}页完毕")


if __name__ == "__main__":
    main()