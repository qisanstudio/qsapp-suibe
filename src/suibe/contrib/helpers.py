# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import render_template_string
from jinja2 import Markup
from ..models import NaviModel


navi_str = '''
	{% for channel in navi.channels %}
		{% if not channel.channels %}
			<li class=""><a href="{{ channel.url }}">{{ channel.name }}</a></li>
		{% else %}
			<li class="dropdown">
				<a href="{{ channel.url }}" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">{{ channel.name }}<span class="caret"></span></a>
				<ul class="dropdown-menu">
				{% for subchannel in channel.channels %}
					<li><a href="{{ subchannel.url }}">{{ subchannel.name }}</a></li>
				{% endfor %}
				</ul>
			</li>
		{% endif %}
	{% endfor %}
'''


def render_navi(navi_id):
    navi = NaviModel.query.get(1)
    return Markup(render_template_string(navi_str, navi=navi))
