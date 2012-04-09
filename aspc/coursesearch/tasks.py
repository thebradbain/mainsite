from celery.task import task
import pyodbc
from django.conf import settings

@task
def update_catalog():
    logger = update_catalog.get_logger()
    logger.info("Starting full catalog update")
    logger.info("Connecting to {0}".format(settings.COURSE_DATA_DB['HOST']))
    cursor = pyodbc.connect(
      driver="FreeTDS",
      server=settings.COURSE_DATA_DB['HOST'],
      database=settings.COURSE_DATA_DB['NAME'],
      uid=settings.COURSE_DATA_DB['USER'],
      pwd=settings.COURSE_DATA_DB['PASSWORD']
    )
    logger.info("Full catalog update finished")

@task
def update_enrollments():
    logger = update_registration.get_logger()
    logger.info("Starting update of course enrollments")
    logger.info("Course enrollments update finished")
