from datetime import datetime,timedelta

date1str=input()
date2str=input()

date1t=datetime.strptime(date1str,"%Y-%m-%d")
date2t=datetime.strptime(date2str,"%Y-%m-%d")

dif=(date1t-date2t).total_seconds()

print(dif)