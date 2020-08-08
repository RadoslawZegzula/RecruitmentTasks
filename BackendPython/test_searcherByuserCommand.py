import pytest
from searcherByUserCommand import SearcherByUserCommand

#Tests in this file are working only with intact state of database.

def test_printUsersFromBirthDateRange_ValidLengthOfResultList(leftDate = "1997-07-26", rightDate ="1998-04-03"):
    sbuc = SearcherByUserCommand()
    result = sbuc.printUsersFromBirthDateRange(leftDate, rightDate)
    assert len(result) == 25

def test_printSafestPassword():
    sbuc = SearcherByUserCommand()
    result = sbuc.printSafestPassword()
    assert result == "intercourse"

def test_printNMostPopularPassword(n = 4):
    sbuc = SearcherByUserCommand()
    result = sbuc.printNMostPopularPassword(n)
    expected = [('edward1', 3), ('fight', 3), ('wonder', 3), ('zxczxc', 3)]
    assert result == expected

def test_printNMostPopularCities(n = 4):
    sbuc = SearcherByUserCommand()
    result = sbuc.printNMostPopularCities(n)
    expected = [('Auckland', 12), ('Stirling', 7), ('شیراز', 7), ('Lyon', 7)]
    assert result == expected

def test_printWantedAvgAge_males(firstOptional = "male"):
    sbuc = SearcherByUserCommand()
    result = sbuc.printWantedAvgAge(firstOptional)
    expected = 48.64187866927593
    assert result == expected

def test_printWantedAvgAge_females(firstOptional = "female"):
    sbuc = SearcherByUserCommand()
    result = sbuc.printWantedAvgAge(firstOptional)
    expected = 48.75562372188139
    assert result == expected

def test_printWantedAvgAge_all(firstOptional = "all"):
    sbuc = SearcherByUserCommand()
    result = sbuc.printWantedAvgAge(firstOptional)
    expected = 48.6975 
    assert result == expected  

def test_printWantedAvgAge_all():
    sbuc = SearcherByUserCommand()
    result = sbuc.printPersonPercentes()
    expected = ("51%","49%")
    assert result == expected        