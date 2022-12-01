"""
--> Develope a python code for a simple calculator, which contains the methods for
    addition, subtraction, multiplication and divison. Your code must be written in
    OOPs based structure.

--> Write a unit testing code using pytest framework for each developed function i.e. addition,
    subtraction, multiplication and division. Test the functions using all various possible
    values, fetch the test inputs from csv/ excel test input sheet

    Take function name and input values from csv file, fetch expected output and execute the test.
    i.e. function name is addition, input values are 4, 5 and expected value is 9.
    test the addition function using given inputs and declare the pass/ fail result

--> Please refer to the given unit_testing_exercise.xls sample input csv file.
    Please add more test cases for addition function and for the remaining functions.

--> Dump each function test data into individual csv/ excel output file i.e. unittest_addition_result.csv

    Please refer to the given sample output csv file addition function tests
"""
import pandas as pd
import Calculator
import pytest
import csv
import numpy as np
import xlrd

df = pd.read_excel(r'/home/softnautics/unit_testing_exercise.xls')
cal = Calculator.mathOperations()


def addTest():
    opFunction = df.loc[df['TestFunction'] == 'Addition']
    finalInput = opFunction['TestInputs'].str.split(',', expand=True).astype(float)
    output = opFunction['ExcpectedValue']
    add = lambda row: cal.addition(row[0], row[1])
    opFunction['ActualValue'] = finalInput.apply(add, axis=1)
    opFunction['Result'] = np.where(opFunction['ExcpectedValue'] == opFunction['ActualValue'], 'Pass', 'Fail')
    opFunction.to_csv('unittesting_addition_result.csv')
    result = pd.concat([finalInput, output], axis=1, join='outer')
    #dff=pd.DataFrame(finalInput,output)
   # finalOutput = result.to_numpy().tolist()
    finalOutput = [tuple(ele) for ele in result]
    return finalOutput


def subtractTest():
    opFunction = df.loc[df['TestFunction'] == 'Substraction']
    finalInput = opFunction['TestInputs'].str.split(',', expand=True).astype(float)
    output = opFunction['ExcpectedValue']
    subtract = lambda row: cal.subtraction(row[0], row[1])
    opFunction['ActualValue'] = finalInput.apply(subtract, axis=1)
    opFunction['Result'] = np.where(opFunction['ExcpectedValue'] == opFunction['ActualValue'], 'Pass', 'Fail')
    opFunction.to_csv('unittesting_subtraction_result.csv')
    result = pd.concat([finalInput, output], axis=1, join='outer')
    finalOutput = result.to_numpy().tolist()
    finalOutput = [tuple(ele) for ele in finalOutput]
    return finalOutput


def multiplyTest():
    opFunction = df.loc[df['TestFunction'] == 'Multiplication']
    finalInput = opFunction['TestInputs'].str.split(',', expand=True).astype(float)
    output = opFunction['ExcpectedValue']
    multiply = lambda row: cal.multiplication(row[0], row[1])
    opFunction['ActualValue'] = finalInput.apply(multiply, axis=1)
    opFunction['Result'] = np.where(opFunction['ExcpectedValue'] == opFunction['ActualValue'], 'Pass', 'Fail')
    opFunction.to_csv('unittesting_multiplication_result.csv')
    result = pd.concat([finalInput, output], axis=1, join='outer')
    finalOutput = result.to_numpy().tolist()
    finalOutput = [tuple(ele) for ele in finalOutput]
    return finalOutput


def divisionTest():
    opFunction = df.loc[df['TestFunction'] == 'Division']
    finalInput = opFunction['TestInputs'].str.split(',', expand=True).astype(float)
    output = opFunction['ExcpectedValue']
    division = lambda row: cal.division(row[0], row[1])
    opFunction['ActualValue'] = finalInput.apply(division, axis=1)
    opFunction['Result'] = np.where(opFunction['ExcpectedValue'] == opFunction['ActualValue'], 'Pass', 'Fail')
    opFunction.to_csv('unittesting_division_result.csv')
    result = pd.concat([finalInput, output], axis=1, join='outer')
    finalOutput = result.to_numpy().tolist()
    finalOutput = [tuple(ele) for ele in finalOutput]
    return finalOutput


@pytest.mark.parametrize("firstNumber,secondNumber,expected", addTest())
def test_addition(firstNumber, secondNumber, expected):
    assert Calculator.addition(firstNumber, secondNumber) == expected


@pytest.mark.parametrize("firstNumber,secondNumber,expected", subtractTest())
def test_subtraction(firstNumber, secondNumber, expected):
    assert Calculator.subtraction(firstNumber, secondNumber) == expected


@pytest.mark.parametrize("firstNumber,secondNumber,expected", multiplyTest())
def test_multiplication(firstNumber, secondNumber, expected):
    assert Calculator.multiplication(firstNumber, secondNumber) == expected


@pytest.mark.parametrize("firstNumber,secondNumber,expected", divisionTest())
def test_division(firstNumber, secondNumber, expected):
    assert Calculator.division(firstNumber, secondNumber) == expected
