import sys
import os
import django

sys.path.append("../nycCivilServiceJobs")  # here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nycCivilServiceJobs.settings")
django.setup()

from examresults.models import ExamSchedule
import pandas as pd
import tabula
import csv
import datetime


def get_upcoming_exams():
    file = "https://www1.nyc.gov/assets/dcas/downloads/pdf/noes/yearly_examschedule_alpha.pdf"
    tabula.convert_into(
        file, "upcoming_exams.csv", output_format="csv", stream=True, pages="all"
    )
    exam_csv = "upcoming_exams.csv"
    return exam_csv


def save_upcoming_exams():
    exam_csv = get_upcoming_exams()
    exams = []
    db_count = ExamSchedule.objects.count()
    with open(exam_csv) as f:
        reader_exams = csv.reader(f, delimiter=",")

        # Skip first two rows: 1st - meta data, 2nd - header
        next(reader_exams)
        next(reader_exams)

        for row in reader_exams:
            try:
                val_in_db = ExamSchedule.objects.filter(
                    # exam_title=row[0],
                    exam_title_civil_service_title=row[0],
                    exam_number=row[1],
                    application_start_date=convertDateFormat(row[3]),
                    application_end_date=convertDateFormat(row[4]),
                    exam_type=row[5],
                )

                if val_in_db.exists():
                    break

                exams.append(
                    ExamSchedule(
                        # row[2] is always "" so skip
                        # exam_title=row[0],
                        exam_title_civil_service_title=row[0],
                        exam_number=row[1],
                        application_start_date=convertDateFormat(row[3]),
                        application_end_date=convertDateFormat(row[4]),
                        exam_type=row[5],
                    )
                )
            except Exception as e:
                print("Error", e)

    # print to console data extracted
    print("Found Exam records: ", len(exams))
    ExamSchedule.objects.bulk_create(exams, ignore_conflicts=True)
    print(".", end="", flush=True)
    print("\nInserted Exam records: ", ExamSchedule.objects.count() - db_count)
    os.remove("upcoming_exams.csv")


def convertDateFormat(inputDate):
    if not inputDate:
        return
    return datetime.datetime.strptime(inputDate, "%m/%d/%Y").strftime("%Y-%m-%d")


if __name__ == "__main__":
    save_upcoming_exams()