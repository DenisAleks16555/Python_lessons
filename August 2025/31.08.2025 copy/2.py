from apscheduler.schedulers.blocking import BlockingScheduler # BlockingScheduler - операция блокирующая
from datetime import datetime



def say_hello():
    print("Hello from code, time:", datetime.now().time())


def inform():
    print("----INFORMASHION----")


scheduler =  BlockingScheduler()
scheduler.add_job(say_hello, 'interval', seconds=5)
scheduler.add_job(inform, 'interval', seconds=2)
scheduler.start()
