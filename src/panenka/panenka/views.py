import csv
import validate_email
from datetime import datetime

from django.shortcuts import render


def landing(request):
    if request.method == 'GET':
        return render(request, 'panenka/index.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        with open('customer_emails.csv', 'a+') as output_file:
            wr = csv.writer(output_file, delimiter=',', lineterminator='\n')
            if validate_email.validate_email(email):
                wr.writerow([email, datetime.now()])
        return render(request, 'panenka/404.html')
