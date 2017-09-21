from django.shortcuts import render
from django.http import HttpResponse
from panel_inter_app.models import *
import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule
import datetime


# Create your views here.
def interview(request):
    person_details = Panel_Inter.objects.all()
    person=person_details.filter(skills__icontains="java",outstation=False,weekend=True)
    avail_person=[q.name for q in person]
    print(avail_person)

    year=2017
    start_date=datetime.datetime(year,10,1)
    end_date=datetime.datetime(year,12,31)
    rr = rrule.rrule(rrule.WEEKLY,byweekday=relativedelta.SA,dtstart=start_date)
    weeks=[i.strftime('%d/%m/%Y') for i in rr.between(start_date,end_date,inc=True)]
    i=0
    for week in weeks:
       if (i==len(avail_person)):i=0
       print(avail_person[i],week)
       person, created= Schedule_Inter.objects.update_or_create(name=avail_person[i], date=week)
       i+=1
    dis=Schedule_Inter.objects.all()
    return HttpResponse([d.name for d in dis])             

#output ['09/02/2017', '09/09/2017', '09/16/2017', '09/23/2017', '09/30/2017', '10/07/2017', '10/14/2017', '10/21/2017', '10/28/2017', '11/04/2017', '11/11/2017', '11/18/2017', '11/25/2017', '12/02/2017', '12/09/2017', '12/16/2017', '12/23/2017', '12/30/2017']


#(u'soundar', u'python,java', False, True)(u'sk', u'java,c', True, True)(u'sa', u'java,c,python', False, True)
