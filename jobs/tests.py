from django.test import TestCase

# from sodapy import Socrata
from django.urls import reverse
from django.db.models import QuerySet
from jobs.models import job_record
from django.utils import timezone
from jobs.views import SearchResultsView

# client_socrata = Socrata(
#     "data.cityofnewyork.us",
#     "m7QHRP2U6tqRR7XCge8TzIRUW",
#     username="nycCivilService.csgy6063@gmail.com",
#     password="team4Pythonpir@tes",
#     timeout=30,
# )

# Create your tests here.


class JobDataTest(TestCase):
    def setUp(self):
        self.createJob()

    def createJob(self):
        job = job_record(
            job_id=100,
            agency="test_agency",
            posting_type="test_posting_type",
            num_positions=10,
            business_title="test_business_title",
            civil_service_title="test_civil_service_title",
            title_classification="test_title_classification",
            title_code_no="test_title_code_no",
            level="test_level",
            job_category="test_job_category",
            full_time_part_time_indicator="test_full_time",
            career_level="test_career_level",
            salary_range_from=100000,
            salary_range_to=120000,
            salary_frequency="test_salary_frequency",
            work_location="test_work_location",
            division_work_unit="test_division_work_unit",
            job_description="test_job_description",
            minimum_qual_requirements="test_minimum_qual_requirements",
            preferred_skills="test_preferred_skills",
            additional_information="test_additional_information",
            to_apply="test_to_apply",
            hours_shift="test_hours_shift",
            work_location_1="test_work_location_1",
            recruitment_contact="test_recruitment_contact",
            residency_requirement="test_residency_requirement",
            posting_date=timezone.now(),
            post_until=None,
            posting_updated=None,
            process_date=timezone.now(),
        )
        job.save()

    def test_jobs_page(self):
        response = self.client.get(reverse("jobs:jobs"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/jobs.html")
        self.assertTemplateUsed(response, "landing_base.html")

    def test_jobs_GET_response_returns_a_queryset(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        self.assertTrue("jobs" in response.context)
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_jobs_GET_response_retains_search_data(self):
        response = self.client.get(reverse("jobs:jobs"), data={"q": "manager"})
        self.assertContains(response, "manager")

    def test_jobs_GET_response_returns_correct_queryset(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        correct_queryset = job_record.objects.all()
        self.assertListEqual(list(correct_queryset), list(response.context["jobs"]))

    def test_jobs_GET_response_returns_correct_job(self):
        response = self.client.get(reverse("jobs:jobs"))
        db_job_id = job_record.objects.all()[0].job_id
        response_job_id = response.context["jobs"][0].job_id
        self.assertEqual(db_job_id, response_job_id)

    def test_search_jobs_results_page(self):
        response = self.client.get(reverse("jobs:results"), data={"q": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "jobs/search.html")
        self.assertTemplateUsed(response, "landing_base.html")

    def test_search_jobs_GET_response_returns_correct_view_in_context(self):
        response = self.client.get(reverse("jobs:results"), data={"q": ""})
        self.assertIsInstance(response.context["view"], SearchResultsView)

    def test_search_jobs_GET_response_retains_search_data(self):
        response = self.client.get(reverse("jobs:results"), data={"q": "manager"})
        self.assertContains(response, "manager")

    def test_search_jobs_GET_response_returns_correct_queryset_with_business_title(
        self,
    ):
        response = self.client.get(
            reverse("jobs:results"), data={"q": "test_business_title"}
        )
        correct_queryset = job_record.objects.filter(
            business_title__icontains="test_business_title"
        ).order_by("-posting_date")
        self.assertListEqual(
            list(correct_queryset), list(response.context["object_list"])
        )
