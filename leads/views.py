from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from django.core.mail import send_mail

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# CRUD: Create, Read, Update, Delete

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(generic.ListView):
    template_name = 'lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads'


class LeadDetailView(generic.DetailView):
    template_name = 'lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = 'lead'


class LeadCreateView(generic.CreateView):
    template_name = 'lead_create.html'
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse('leads:lead_list')

    def form_valid(self, form):
        # TODO: send an email
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see the new lead.",
            from_email="test@test.com",
            recipient_list=["test2@test.com",]
        )
        return super(LeadCreateView, self).form_valid(form)



class LeadUpdateView(generic.UpdateView):
    template_name = 'lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead_list')


class LeadDeleteView(generic.DeleteView):
    template_name = 'lead_delete.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse('leads:lead_list')




# def landing_page(request):
#     return render(request, 'landing.html')


# def lead_list(request):
#     # return HttpResponse("<h1>Hello World</h1>")
#     leads = Lead.objects.all()
#     context = {
#         'leads': leads
#     }
#     return render(request, 'lead_list.html', context)



# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         'lead': lead
#     }
#     return render(request, 'lead_detail.html', context)


# def lead_create(request):
#     agents = Agent.objects.all()
#     form = LeadModelForm() # GET request

#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         print("Receive a new creation request")
#         if form.is_valid():
#             print("Validate a new lead")
#             form.save()
#             return redirect('/leads/')

#     context = {
#         'form': form,
#         'agents': agents,
#     }
#     return render(request, 'lead_create.html', context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)

#         if form.is_valid():
#             form.save()
#             return redirect('/leads/')
    
#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, 'lead_update.html', context)


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads/')



# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)

#     form = LeadForm() # GET request

#     if request.method == 'POST':
#         print('Reveiving a post request')
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()

#             return redirect('/leads/')

#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, 'lead_update.html', context)





# def lead_create(request):
#     form = LeadForm() # GET request

#     if request.method == 'POST':
#         print('Reveiving a post request')
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name, 
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             return redirect('/leads/')

#     context = {
#         'form': form
#     }
#     return render(request, 'lead_create.html', context)