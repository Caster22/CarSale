from django.shortcuts import render

def  Car_list(request):
	return render(request, 'CarSale/Car_list.html', {})