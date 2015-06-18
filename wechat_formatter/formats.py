# coding: utf-8

__author__ = 'jsun'

class BaseFormat(object):

    def __init__(self):
        self.name = "base_format"
        self.id = -1
        self.description = ""
        self.html_pre = ""
        self.html_post = ""
        self.child_formats = []
        self.usep = False
        self.useheader = False

class SectionTitle(BaseFormat):

    # wechat_guide/3.html
    def __init__(self):
        self.name = "section_title"
        self.id = 1
        self.description = "小标题"

        self.html_pre = '<p style="line-height: normal; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;"><strong>'

        self.html_post = '</strong></p>'

        self.child_formats = []

        self.usep = False

        self.useheader = False

class AuthorFormat(BaseFormat):
    #wechat_guide/4.html
    def __init__(self):
        self.name = "author_name"
        self.id = 2
        self.description = "作者姓名"

        self.html_pre = '<br/><p style="box-sizing: border-box; padding: 0px; margin: 0px;"><span style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(85, 85, 85); box-sizing: border-box; padding: 0px; margin-bottom: 20px; text-align: left;">文 / </span><span style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin-bottom: 20px; text-align: left;">'

        self.html_post = '</span></p><br/>'

        self.usep = False
        self.useheader = False

class ParagraphFormat(BaseFormat):
    #wechat_guide/5.html
    def __init__(self):
        self.name = "paragraph"
        self.id = 3
        self.description = "正文段落"

        self.html_pre = ''

        self.html_post = ''

        self.usep = True

        self.p_pre = '<p style="line-height: 1.5em; font-size: 16px; font-family: 微软雅黑; color: #555555; padding: 0px; margin: 10px 0px; text-align: left;">'

        self.p_post = '</p>'
        self.useheader = False

class CitationFormat(BaseFormat):
    #wechat_guide/6.html
    def __init__(self):
        self.name = "citation"
        self.id = 4
        self.description = "引用"

        self.usep = True

        self.html_pre = '<section data-id="23" style="border: 0px none; padding: 0px; box-sizing: border-box; margin: 0px; font-size: 16px; font-family: 微软雅黑;" class="135editor" data-color="#00BBAA" data-custom="#00BBAA"><blockquote class="135brush" style="orphans: 2; white-space: normal; widows: 2; font-size: 16px; line-height: normal; margin: 10px 0px; padding: 15px 20px 15px 45px; outline: 0px; border: 0px currentcolor; color: rgb(0, 187, 170); vertical-align: baseline; box-sizing: border-box; background-image: url(http://www.wx135.com/img/bg/left_quote.jpg); background-color: rgb(241, 241, 241); background-position: 1% 5px; background-repeat: no-repeat;">'

        self.html_post = '</blockquote></section>'

        self.p_pre = "<p>"
        self.p_post = "</p>"
        self.useheader = False

class RelatedArticle(BaseFormat):
    #wechat_guide/7.html
    def __init__(self):
        self.name = "related_article"
        self.id = 5
        self.description = "相关文章; 格式:同节标题+正文,例:<理工女发刊词>｜性别不是放弃的理由"

        self.html_pre = '<h2 style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;"><strong style="box-sizing: border-box; padding: 0px; margin: 0px;">相关文章</strong><br style="box-sizing: border-box; padding: 0px; margin: 0px;"/></h2>'

        self.html_post = ''

        self.usep = True

        self.p_pre = '<p style="line-height: normal; font-size: 16px; font-family: 微软雅黑; color: rgb(85, 85, 85); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;">'
        self.p_post = '</p>'

        self.useheader = False

class ArticleSource(BaseFormat):
    #wechat_guide/8.html
    def __init__(self):
        self.name = "article_source"
        self.id = 6
        self.description = "文章来源"

        self.usep = True

        self.html_pre = '<h2 style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;"><strong>文章来源</strong></h2>'
        self.html_post = ''

        self.p_pre = '<p style="line-height: normal; font-size: 12px; font-family: 微软雅黑; box-sizing: border-box; padding: 0px; margin: 0px 0px 5px; color: rgb(85, 85, 85);">'
        self.p_post = '</p>'

        self.useheader = False

class Reference(BaseFormat):
    #wechat_guide/8.html
    def __init__(self):
        self.name = "reference"
        self.id = 7
        self.description = "参考文献"

        self.usep = True

        self.html_pre = '<h2 style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;"><strong>参考文献</strong></h2>'
        self.html_post = ''

        self.p_pre = '<p style="line-height: normal; font-size: 12px; font-family: 微软雅黑; box-sizing: border-box; padding: 0px; margin: 0px 0px 5px; color: rgb(85, 85, 85);">'
        self.p_post = '</p>'

        self.useheader = False


class Introduction(BaseFormat):
    #wechat_guide/2.html
    def __init__(self):
        self.name = "introduction"
        self.id = 8
        self.description = "引言、作者简介、其他章节类标题"

        self.usep = True

        self.useheader = True

        self.header_pre = '<strong>'
        self.header_post = '</strong>'

        self.p_pre = '<p style="color: #555555; font-size: 16px; font-weight: normal; line-height: normal; box-sizing: border-box; padding: 0px; margin: 0px;">'
        self.p_post = '</p>'

        self.html_pre = '<section data-id="1" style="border: 0px none; padding: 0px; box-sizing: border-box; margin: 0px; font-size: 16px; font-family: 微软雅黑;" class="135editor"><h1 class="135brush" placeholder="请输入标题" style="border-left-width: 5px; border-left-style: solid; border-left-color: rgb(0, 187, 170); font-size: 16px; line-height: 2em; color: #555555; padding: 5px 10px; margin: 10px 0px; box-sizing: border-box;">'
        self.html_post = '</h1></section>'

class Copyright(BaseFormat):
    #wechat_guide/9.html
    def __init__(self):
        self.name = "copyright"
        self.id = 9
        self.description = "版权声明"

        self.usep = True
        self.useheader = False

        self.html_pre = '<section style="margin: 0px 0px; padding: 5px 20px 15px 20px; outline: 0px; border: 1px #555555; background-color:#f1f1f1;background-position: 1% 5px; background-repeat: no-repeat; font-family: 微软雅黑;"><h1 style="white-space: normal; margin-top: 10px; margin-bottom: 10px; font-size: 16px; line-height: 1.75em; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px;"><strong style="box-sizing: border-box; padding: 0px; margin: 0px;">版权声明</strong></h1>'
        self.html_post = '<p style="margin-bottom: 5px; line-height: normal; white-space: normal; font-size: 16px; color: rgb(85, 85, 85); box-sizing: border-box; padding: 0px 0px 0px 10px;">本文为本站成员原创，版权及其他合法权利均归作者与本站共同所有。任何媒体或网站未经本站授权不得转贴或以其他方式复制发表本文。寻求授权请联系： <span style="color:#00bbaa;">contact@stemgirlschina.com</span></p></section><p style="margin-top: 5px; margin-bottom: 5px; font-family: sans-serif; font-size: 16px; line-height: normal; white-space: normal; box-sizing: border-box; padding: 0px;"><br/></p>'

        self.p_pre = '<p style="margin-bottom: 5px; line-height: normal; white-space: normal; font-size: 16px; color: rgb(85, 85, 85); box-sizing: border-box; padding: 0px 0px 0px 10px;">'
        self.p_post = '</p>'