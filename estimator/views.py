from django.shortcuts import render
from django.http import JsonResponse
from . models import PredResults
import pandas as pd



def estimator(request):
    return render(request, 'estimate.html')


def estimate_chances(request):

    if request.POST.get('action') == 'post':

        age=int(request.POST.get('age'))
        bmi=float(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        sex_female=int(request.POST.get('sex_female'))
        sex_male=int(request.POST.get('sex_male'))
        smoke_no=int(request.POST.get('smoke_no'))
        smoke_yes=int(request.POST.get('smoke_yes'))

        model = pd.read_pickle('/Users/jordanmoore/Desktop/DS/healthcare_cost_prediction/new_model.pickle') 

        result = model.predict([[age, bmi, children, sex_female, sex_male, smoke_no, smoke_yes]])

        charges = result[0]

        PredResults.objects.create(age=age, bmi=bmi, children=children, sex_female=sex_female, sex_male=sex_male, smoke_no=smoke_no, smoke_yes=smoke_yes, charges=charges)

        return JsonResponse({'result': charges, 'age': age, 'bmi': bmi, 'children': children, 'sex_female': sex_female, 'sex_male': sex_male, 'smoke_no': smoke_no, 'smoke_yes': smoke_yes}, safe=False)

def view_results(request):
    data = {'dataset': PredResults.objects.all()}
    return render(request, 'results.html', data)