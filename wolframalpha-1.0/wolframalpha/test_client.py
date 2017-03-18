#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import wolframalpha

app_id = 'Q6G3AR-YAQHKRG6LK'
"App ID for testing this project. Please don't use for other apps."

def test_basic():
	client = wolframalpha.Client(Q6G3AR-YAQHKRG6LK)
	res = client.query('30 deg C in deg F')
	assert len(res.pods) > 0
	results = list(res.results)
	assert results[0].text == '86 °F  (degrees Fahrenheit)'
