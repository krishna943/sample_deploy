from django.shortcuts import render, redirect,HttpResponse
import csv
from django.db import models
from .forms import UploadForm
from .models import FileUpload

import pandas as pd
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.management.base import BaseCommand
from django.views.generic import View
from .models import FileUpload

"""
class Command(BaseCommand):
    help = 'Create models dynamically from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        df = pd.read_csv(csv_file)

        # Loop through each column and determine the field type
        fields = {}
        for column in df.columns:
            if df[column].dtype == int:
                fields[column] = models.IntegerField()
            elif df[column].dtype == float:
                fields[column] = models.FloatField()
            else:
                fields[column] = models.CharField(max_length=255)

        # Dynamically create the model class
        model = type('DynamicModel', (models.Model,), fields)

        # Create the model in the database
        ContentType.objects.get_or_create(model=model, app_label='your_app_label')
         return HttpResponse("Model Created")

def Command(request):
    df = pd.read_csv('/Users/ksah/PycharmProjects/CSVuploader/csv1/csvuploader/username.csv')

    # Get the column names and datatypes from the dataframe
    columns = list(df.columns)
    dtypes = dict(df.dtypes)

    # Define a new model class based on the dataframe information
    model_name = "MyModel"
    attrs = {
        column: models.Field(
            type=models.__dict__.get(dtypes[column].name, models.CharField)
        ) for column in columns
    }
    model = type(model_name, (models.Model,), attrs)

    # Register the model with Django
    globals()[model_name] = model
    return HttpResponse("Model created Sucessfully")
    
    
    #other part
        if request.method == "POST":
        file2 = request.FILES["file"]
        document = FileUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("Your File is uploaded sucessfully")
    return render(request,"home.html")
    """


class Meta:
    app_label = 'csvuploaders'
def homes(request):
        # app_label must be set using the Meta inner class
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)
            reader = csv.reader(file)
            #header = next(reader)
            columns = list(df.columns)
            dtypes = dict(df.dtypes)
            fields = {
                '__module__': 'csvuploaders.models'
            }
            for column in df.columns:
                if df[column].dtype == int:
                    fields[column] = models.IntegerField()
                elif df[column].dtype == float:
                    fields[column] = models.FloatField()
                else:
                    fields[column] = models.CharField(max_length=255)

            # Dynamically create the model class
            #model = type('DynamicModel', (models.Model,), fields)
            DynamicModel = type('DynamicModel', (models.Model,), fields)
            for row in reader:
                obj = DynamicModel(**{field_name: field_value for field_name, field_value in zip(columns, row)})
                obj.save()
            return HttpResponse("Model created sucessfully")
    else:
        form = UploadForm()
    return render(request, 'home.html', {'form': form})

