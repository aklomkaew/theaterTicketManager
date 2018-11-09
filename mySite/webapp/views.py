from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
# from ..webapp.forms import PaymentForm

def index(request) :
    return render(request, 'webapp/home.html')

def performance(request) :
    return render(request, 'webapp/performance.html')

def contact(request) :
    return render(request, 'webapp/contact.html')

def buySeasonTicket(request) :
    return render(request, 'webapp/buySeasonTicket.html')

def payment(request) :
    return render(request, 'webapp/payment.html')

def echo(request) :
    return render(echo, 'webapp/echo.html')

def seatSelection(request):
    return render(request, 'webapp/seatSelection.html')

# class PaymentView(TemplateView):
#     template_name = 'webapp/echo.html'
#
#     def get(self, request):
#         form = PaymentForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self,request):
#         form = PaymentForm(request.POST)
#         if(form.is_valid()) :
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#
#             text = form.cleaned_data['post']
#             form = PaymentForm()
#             redirect('webapp:payment')
#
#         args = {'form': form, 'text': text}
#         return render(request, self.template_name, args)

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

