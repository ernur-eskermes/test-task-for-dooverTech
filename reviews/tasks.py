from celery import shared_task

from .scripts.check_reviews import check_reviews


@shared_task
def check_reviews_task():
    check_reviews()
