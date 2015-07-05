__author__ = 'jsun'
# coding: utf-8

from flask import Blueprint, render_template, Response, request
from utils.basic_auth import requires_auth
import json
from bs4 import BeautifulSoup

bp_wechat_formatter = Blueprint('bp_wechat_formatter', __name__, template_folder = 'templates')

# load formats

from wechat_formatter.formats import *
from wechat_formatter.static import copyright_str


format_dict = {
    1: SectionTitle(),
    2: AuthorFormat(),
    3: ParagraphFormat(),
    4: CitationFormat(),
    5: RelatedArticle(),
    6: ArticleSource(),
    7: Reference(),
    8: Introduction(),
    9: Copyright()
}

@bp_wechat_formatter.route('/wechat-formatter/guide/<name>', methods = ['GET'])
def wechat_guides(name):

    return render_template('wechat_guide/' + name + '.html')
    #return render_template('wechat_format.html')


@bp_wechat_formatter.route('/wechat-formatter', methods = ['GET'])
@requires_auth
def format_wechat():
    return render_template('wechat_format.html')

@bp_wechat_formatter.route('/wechat-formatter/get-formats', methods = ['POST'])
def get_formats():
    '''
    [
        {'id':0, 'description', 'name', 'html_pre', 'html_post'}
    ]

    '''

    result = []
    for format_id in format_dict.keys():
        fformat = format_dict[format_id]
        result.append({'id':fformat.id,
                       'name': fformat.name,
                       'description': fformat.description,
                       'html_pre': fformat.html_pre,
                       'html_post': fformat.html_post})

    return Response(json.dumps(result), mimetype="application/json")

@bp_wechat_formatter.route('/wechat-formatter/render', methods = ['POST'])
def render():
    print(request.form)
    texts = request.json['input']
    result_str = ''

    for text in texts:
        format_id = int(text['format_id_str'])
        value = text['value'].decode("utf-8").replace("\n", "")
        fformat = format_dict[format_id]

        if fformat.useheader:
            result_str += fformat.html_pre.decode('utf-8')
            tokens = value.split("</p>")

            if len(tokens) > 2:
                header = tokens[0]
                if len(header) > 0:
                    result_str += fformat.header_pre.decode('utf-8') + header.decode('utf-8') + fformat.header_post.decode('utf-8')
                    result_str += '\n'
                for token in tokens[1:]:
                    if len(token) > 0:
                        if 'li' in token:
                            soup = BeautifulSoup(token)
                            strings = list(soup.strings)
                            replace_dict = {e.decode('utf-8'): fformat.p_pre.decode('utf-8') + e.decode('utf-8') + fformat.p_post.decode('utf-8') for e in strings}

                            new_token = token
                            for k in replace_dict:
                                new_token = new_token.replace(k, replace_dict[k])

                            result_str += new_token + '\n'

                        else:
                            result_str += fformat.p_pre.decode("utf-8") + token.decode("utf-8") + fformat.p_post.decode("utf-8")
                            result_str += "\n"
            result_str += fformat.html_post.decode('utf-8')

        else:

            if fformat.usep:
                result_str += fformat.html_pre.decode('utf-8')
                tokens = value.split("</p>")
                for token in tokens:
                    token = token.replace("<p>", "")
                    if len(token) > 0:
                        # NOTE: dirty hack, wrap p within li
                        # TODO: test!
                        if 'li' in token:
                            soup = BeautifulSoup(token)
                            strings = list(soup.strings)
                            replace_dict = {e.decode('utf-8'): fformat.p_pre.decode('utf-8') + e.decode('utf-8') + fformat.p_post.decode('utf-8') for e in strings}

                            new_token = token
                            for k in replace_dict:
                                new_token = new_token.replace(k, replace_dict[k])

                            result_str += new_token + '\n'

                        else:
                            result_str += fformat.p_pre.decode("utf-8") + token.decode("utf-8") + fformat.p_post.decode("utf-8")
                            result_str += "\n"
                result_str += fformat.html_post.decode("utf-8")

            else:
                value = value.replace("<p>", "").replace("</p>","")
                result_str += fformat.html_pre.decode("utf-8") + value + fformat.html_post.decode("utf-8")

        result_str += "\n\n" # more user-friendly

    result_str += copyright_str

    return Response(json.dumps(result_str), mimetype="application/json")