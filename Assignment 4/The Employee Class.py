class Employee:
    def __init__(self, id, firstName, lastName, salary):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getName(self):
        return self.firstName, self.lastName

    def getSalary(self):
        return self.salary

    def getAnnualSalary(self):
        return self.salary * 12

    def raiseSalary(self, percent):
        self.salary = self.salary * percent
        return self.salary

    def toString(self):
        ret = "Employee[id=" + self.id + ",name="\
              + self.firstName+" " + self.lastName + ", salary =" + self.salary + "]"
        return ret

class InvoiceItem:
    def __init__(self, id, desc, qty, unitPrice):
        self.id = id
        self.desc = desc
        self.qty = qty
        self.unitPrice = unitPrice

    def getID(self):
        return self.id

    def getDesc(self):
        return self.desc

    def getQty(self):
        return self.qty

    def setQty(self, val):
        self.qty = val

    def getUnitPrice(self):
        return self.unitPrice

    def setUnitPrice(self, val):
        self.unitPrice = val

    def getTotal(self):
        return self.unitPrice * self.qty

    def toString(self):
        ret = "InvoiceItem[id="+ self.id + ",desc="\
              +self.desc+", qty " + self.qty + ", unitPrice ="+ self.unitPrice +"]"
        return ret

class Account:
    def __init__(self, id, name, balance = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def credit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Amount exceeded balance")
        return self.balance

    def transferTo(self, Account, amount):
        if amount <= self.balance:
            self.balance -= amount
            Account.balance += amount
        else:
            print("Amount exceeded balance")
        return self.balance

    def toString(self):
        ret = "Account[id=" + self.id + ",name=" + self.name + ",balance=" + self.balance + "]"
        return ret

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def toString(self):
        ret = "" + self.day + "/" + self.month + "/" + self.year
        return ret

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setHour(self, hour):
        self.hour = hour

    def setMinute(self, minute):
        self.minute = minute

    def setSecond(self, second):
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def toString(self):
        ret = "" + self.hour + ":" + self.minute + ":" + self.second
        return ret

    def nextSecond(self):
        self.second += 1
        return self

    def previousSecond(self):
        self.second -= 1
        return self
