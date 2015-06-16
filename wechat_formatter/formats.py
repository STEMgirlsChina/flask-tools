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

class SectionTitle(BaseFormat):

    # wechat_guide/3.html
    def __init__(self):
        self.name = "section_title"
        self.id = 1
        self.description = "小标题"

        self.html_pre = '<h2 style="line-height: normal; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin: 10px 0px; text-align: left;"><strong>'

        self.html_post = '</strong></h2>'

        self.child_formats = []

        self.usep = False

class AuthorFormat(BaseFormat):
    #wechat_guide/4.html
    def __init__(self):
        self.name = "author_name"
        self.id = 2
        self.description = "作者姓名"

        self.html_pre = '<br/><p style="box-sizing: border-box; padding: 0px; margin: 0px;"><span style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(85, 85, 85); box-sizing: border-box; padding: 0px; margin-bottom: 20px; text-align: left;">文 / </span><span style="line-height: 1.75em; font-size: 16px; font-family: 微软雅黑; color: rgb(0, 187, 170); box-sizing: border-box; padding: 0px; margin-bottom: 20px; text-align: left;">'

        self.html_post = '</span></p><br/>'

        self.usep = False

class ParagraphFormat(BaseFormat):
    #wechat_guide/5.html
    def __init__(self):
        self.name = "paragraph"
        self.id = 3
        self.description = "正文段落"

        self.html_pre = ''

        self.html_post = ''

        self.usep = True

        self.p_pre = '<p style="line-height: normal; font-size: 16px; font-family: 微软雅黑; color: #555555; padding: 0px; margin: 10px 0px; text-align: left;">'

        self.p_post = '</p>'

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