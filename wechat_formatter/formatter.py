__author__ = 'jsun'

from flask import Blueprint, render_template

bp_wechat_formatter = Blueprint('bp_wechat_formatter', __name__, template_folder = 'templates')

@bp_wechat_formatter.route('/wechat-formatter')
def format_wechat():

    return render_template('wechat_format.html')
