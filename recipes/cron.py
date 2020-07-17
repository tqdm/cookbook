#!/bin/python3
"""Using APScheduler with Bottle."""

from apscheduler.schedulers.background import BackgroundScheduler
from bottle import route, run


def job():
    """Run job."""
    print("Scheduler is alive!")


@route("/")
def index():
    """Return index route for bottle."""
    return "<b>Hello world!</b>"


if __name__ == "__main__":
    cron = BackgroundScheduler(daemon=True)
    cron.add_job(job, "interval", seconds=5)
    cron.start()
    run(host="localhost", port=8080)
