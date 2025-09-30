from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Petition, PetitionVote
from .forms import PetitionForm

@login_required
def petition_list(request):
    petitions = Petition.objects.all().order_by("-created_at")
    return render(request, "petitions/petition_list.html", {"petitions": petitions})

@login_required
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect("petition_list")
    else:
        form = PetitionForm()
    return render(request, "petitions/petition_form.html", {"form": form})

@login_required
def petition_vote(request, pk):
    petition = get_object_or_404(Petition, id=pk)
    vote_value = request.GET.get('vote')  # '1' or '0'
    vote_bool = True if vote_value == '1' else False

    # Create or update the vote for this user
    vote, created = PetitionVote.objects.update_or_create(
        petition=petition,
        user=request.user,
        defaults={'value': vote_bool}
    )

    return redirect('petition_list')