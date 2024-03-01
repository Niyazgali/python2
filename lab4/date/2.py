import datetime
today = datetime.datetime.now()
yest = today - datetime.timedelta(days=1)
tom = today + datetime.timedelta(days=1)
print(yest)
print(today)
print(tom)
