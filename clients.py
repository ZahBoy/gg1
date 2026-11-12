class Client:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def can_pay(self, amount):
     return amount <= self.balance
  def pay(self, amount):
    pass
