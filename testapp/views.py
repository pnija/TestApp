import json
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView
from django.db.models import Min,Count
from datetime import datetime
from testapp.models import Location
from testapp.forms import LocationForm


class LocationCreate(CreateView):
    '''Creates a record of data
    
    '''
    form_class = LocationForm
    template_name = "home.html"
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        details = LocationForm(self.request.POST)
        if (details.is_valid()):
            detailsObj = details.save(commit=False)          
            detailsObj.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data,
                                           details=details)  


class LocationList(ListView):
    '''Lists all Location IDs
    
    Avoids redundancy of Location IDs
    '''
    form_class = LocationForm
    model = Location
    template_name = "location_list.html"

    def get_context_data(self,**kwargs):
        allset = Location.objects.values_list('location_id',
                                              flat=True).distinct().order_by(
                                                  'location_id')
        context = {
            'allset': allset
        }
        return context        


class FluctuationView(View):
    '''Returns json data
    
    Get count of selected Location IDs and displays fluctuations
    '''
    def get(self, request, *args, **kwargs):
        data={}
        date_list = []
        location_data = []
        data = request.GET['id']
        allset = Location.objects.filter(location_id=data)
        time_list = allset.values_list('timestamp',
                                       flat=True).distinct().order_by(
                                           'timestamp')
        for times in time_list:
            date_list.append(times.date().isoformat())
        date_list = list(set(date_list))
        date_list.sort()
        for i in date_list:
            queryset = allset.filter(timestamp__icontains=i)
            count_data = queryset.count()
            dates = i
            loc_id = queryset[0].location_id 
            data_dict = {dates:count_data}
            location_data.append(dict(data_dict))
        return HttpResponse(json.dumps(location_data))