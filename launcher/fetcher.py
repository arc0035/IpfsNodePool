from apscheduler.schedulers.blocking import BlockingScheduler

def fetch_job():
    pass

def run_fetcher():
    print('fetcher lunched!')
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_job, 'interval', seconds=5)
    scheduler.start()



