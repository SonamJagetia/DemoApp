from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

@login_required
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST':
		token = request.POST['stripeToken']
		# Charge the user's card:
		try:
			stripe.Charge.create(
  		    	amount=1000,
  		    	currency="usd",
  		  		description="Example charge",
  		 		source=token,
		)
		except stripe.CardError:
		# the card has been declined
			pass
		# Create the charge on stripe's server

	context = {'publishKey': publishKey } 
	template = 'checkout.html'
	return render(request,template,context)