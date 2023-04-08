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

if __name__ == "__main__":
    unittest.main()
