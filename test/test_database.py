# CS 4910 - Herb Control Project
# Western Michigan University
# Authors: Vinicius Petrelli Cicerone, Dylan Lafleur, Paxton Plum
# Faculty Advisor: Dr. John Kapenga
# tests the insertion and range functions from the database script

import pytest
import Database

# inserts a test value into the database (not automated, must manually check for now)
def test_dbInsert(x, y, z):
	assert Database.dbInsert(x, y, z) == None

	return

# test that the gathered values from the webpage fall within the required range
def test_dbGetRanges():
	r = Database.dbGetRanges()
	assert 80 <= r[0] <= 100
	assert 60 <= r[1] <= 79
	assert 40 <= r[2] <= 59
	assert 20 <= r[3] <= 49
	assert 0 <= r[4] <= 19
	assert 80 <= r[5] <= 100
	assert 60 <= r[6] <= 79
	assert 40 <= r[7] <= 59
	assert 20 <= r[8] <= 49
	assert 0 <= r[9] <= 19
	assert 80 <= r[10] <= 100
	assert 60 <= r[11] <= 79
	assert 40 <= r[12] <= 59
	assert 20 <= r[13] <= 49
	assert 0 <= r[14] <= 19

	return