from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv, io
from .models import Experiment
from django.db.models import Avg

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        dataset = csv_file.read().decode('utf-8')
        io_string = io.StringIO(dataset)
        next(io_string)  # Skip the header
        for column in csv.reader(io_string, delimiter=',', quotechar='"'):
            _, created = Experiment.objects.update_or_create(
                name=column[0],
                date=column[1],
                observation_type=column[2],
                value=float(column[3])
            )
        return redirect('display_data')  # Redirect to the display_data URL
    return render(request, 'experiment_data_processor/upload_csv.html')

def display_data(request):
    data = Experiment.objects.values('name', 'date', 'observation_type').annotate(avg_value=Avg('value')).order_by('name', 'date', 'observation_type')
    return render(request, 'experiment_data_processor/display_data.html', {'data': data})

