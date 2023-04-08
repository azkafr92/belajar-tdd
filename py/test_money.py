import functools
import operator
import unittest


class Money:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divider):
        return Money(self.amount / divider, self.currency)
    
    def __eq__(self, __value) -> bool:
        return self.amount == __value.amount and self.currency == __value.currency


class Portfolio:
    def __init__(self) -> None:
        self.moneys = []
    
    def add(self, *money):
        self.moneys.extend(money)
    
    def evaluate(self, currency):
        total = functools.reduce(
            operator.add, map(lambda m: m. amount, self.moneys)
        )
        return Money(total, currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")
        self.assertEqual(fiver.times(2), tenner)

    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(tenEuros.times(2), twentyEuros)
    
    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(originalMoney.divide(4), expectedMoneyAfterDivision)
    
    def testAddition(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiver, tenner)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))


if __name__ == "__main__":
    unittest.main()
