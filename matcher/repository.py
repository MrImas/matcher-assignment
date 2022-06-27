from django.shortcuts import get_object_or_404, render
from django.db.models import Count, Case, When, IntegerField, Value

from matcher.models import *


def getJob(id): 
    job = get_object_or_404(Job, pk=id)
    return job;


def findTopMatchingCandidatesForJob(job_id, number_of_top_candidates):
    job = get_object_or_404(Job, pk=job_id)
    candidates =  Candidate.objects.filter(title=job.title).annotate(
        num_matching_skills=Count(Case(
            When(skill__in=job.skill.all(), then=Value(1)),
            output_field=IntegerField()
        ))
    ).values('id', 'title', 'num_matching_skills').order_by('-num_matching_skills')[:number_of_top_candidates]
    return candidates;
    