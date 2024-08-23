from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer  # Assuming user is logged in
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def track_requests(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_requests.html', {'service_requests': service_requests})


# Create your views here.
