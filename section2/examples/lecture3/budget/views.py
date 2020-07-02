from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class NewCategoryForm(forms.Form):
    category = forms.CharField(label="New Category", required=True)
    # allowance = forms.IntegerField(label="Allowance", min_value=1, max_value=1000)


# Create your views here.
def index(request):
    if "categories" not in request.session:
        request.session["categories"] = []
    return render(request, "budget/index.html", {
        "categories": request.session["categories"]
    })


@csrf_exempt
def add(request):
    if request.method == "POST":
        # Fetch the form ...
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data["category"]
            request.session["categories"] += [category]
            return HttpResponseRedirect(reverse("budget:index"))

        else:
            return render(request, "budget/add.html", {
                "form": form
            })
    else:
        return render(request, "budget/add.html", {
            "form": NewCategoryForm()
        })
