from django.shortcuts import render
from django.views import generic

from matcher.models import *
from matcher.repository import *

class IndexView(generic.ListView):
    template_name = 'matcher/jobs.html'
    context_object_name = 'jobs_list'

    def get_queryset(self):
        return Job.objects.all();

def findMatchingCandidatesForJob(request, job_id):
    job = getJob(job_id)
    number_of_top_matching_candidates = int(request.GET.get('top', 50))
    candidates = findTopMatchingCandidatesForJob(job_id, number_of_top_matching_candidates)
    return render(request, 'matcher/results.html', {
        'job': job,
        'matching_candidates': candidates
    })
    