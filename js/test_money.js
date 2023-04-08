const assert = require('assert');

class Money {
    constructor(amount, currency) {
        this.amount = amount;
        this.currency = currency;
    }

    times(multiplier) {
        return new Money(this.amount * multiplier, this.currency);
    }

    divide(divider) {
        return new Money(this.amount / divider, this.currency)
    }
}

class Portfolio {
    constructor() {
        this.moneys = []
    }
    add(...money) {
        this.moneys = this.moneys.concat(money);
    }

    evaluate(currency) {
        let total = this.moneys.reduce((sum, money) => {
            return sum + money.amount;
        }, 0)
        return new Money(total, currency);
    }
}

let fiver = new Money(5, "USD");
let tenner = new Money(10, "USD");
assert.deepStrictEqual(fiver.times(2), tenner);

let tenEuros = new Money(10, "EUR");
let twentyEuros = new Money(20, "EUR");
assert.deepStrictEqual(tenEuros.times(2), twentyEuros);

let originalMoney = new Money(4002, "KRW");
let actualMoneyAfterDivision = originalMoney.divide(4)
let expectedMoneyAfterDivision = new Money(1000.5, "KRW")
assert.deepStrictEqual(actualMoneyAfterDivision, expectedMoneyAfterDivision)

let fifteenDollars = new Money(15, "USD");
let portfolio = new Portfolio();
portfolio.add(fiver, tenner);
assert.deepStrictEqual(portfolio.evaluate("USD"), fifteenDollars);
