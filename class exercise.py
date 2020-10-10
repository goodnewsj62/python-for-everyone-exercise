

class Flower:

    def __init__(self,name,number,price):
        self._Fname = name
        self._Fnumber = int(number)
        self._Fprice = float(price)

    def getprice(self):
       return self._Fprice
    def get_name(self):
        return self._Fname
    def get_number(self):
        return self._Fnumber

    def set_price(self,price):
        self._Fprice = float(price)
    def set_name(self,name):
        self._Fname = name

    def set_number(self, number):
        self._Fnumber = number

class CreditCard:
    """A consumer credit card."""

    def __init__ (self, customer, bank, acnt, limit, bal = 0):
        """Create a new credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = bal

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return the bank s name."""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self):
        """Return current credit limit."""
        return self._limit

    def get_balance(self):
        """Return current balance."""
        return self._balance
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """
        if price + self. balance > self. limit: # if charge would exceed limit,
            return False # cannot accept charge
        else:
            self. balance += price
            return True

    def make_payment(self, amount):
        check = str(amount)
        """Process customer payment that reduces balance."""
        if check.startswith("-"):
            raise ValueError("you cant pay a negative number")
        else:
            self._balance -= amount



# testing = CreditCard('goodnews','uba','588698606',1000)
# print(testing.get_balance())
#
# testing = CreditCard('goodnews','uba','588698606',1000,50)
# print(testing.get_balance())