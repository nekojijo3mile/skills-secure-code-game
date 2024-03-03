'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_EXPENSE = 100000

def validorder(order: Order):
    expenses = Decimal("0")
    payments = Decimal("0")

    for item in order.items:
        amount = Decimal(str(item.amount))
        quantity = Decimal(str(item.quantity))

        if item.type == 'payment':
            payments += amount
        elif item.type == 'product':
            expenses += amount * quantity
        else:
            return "Invalid item type: %s" % item.type

    if expenses > MAX_EXPENSE:
        return "Total amount payable for an order exceeded"

    if expenses != payments:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payments - expenses)
    else:
        return "Order ID: %s - Full payment received!" % order.id