# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# Runs all controller unit tests

import test_textMessage
import test_database
import test_watchdog

def run_tests():
	# tests the text functionality
	assert test_textMessage.test_text() == None
	# attempts a database insertion with set test values
	assert test_database.test_dbInsert(-1, -1, -1) == None
	# tests ranges gathered from the webpage
	assert test_database.test_dbGetRanges() == None

	# add watchdog unit test calls here

	return