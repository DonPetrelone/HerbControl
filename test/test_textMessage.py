# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# tests the test message alert function

import pytest
import TextMessage

def test_text():
	assert TextMessage.text('This is a test alert') == None

	return