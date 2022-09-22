from apscheduler.schedulers.blocking import BlockingScheduler
import fetch.fetchers as fetchers
from fetch.fetcher_interface import FetcherInterface
def fetch_job():
    for f in fetchers.fetcher_list:
        f.fetch()

def run_fetcher():
    print('fetcher lunched!')
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_job, 'interval', seconds=5)
    scheduler.start()



