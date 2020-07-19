from django.shortcuts import render,redirect
from . models import Customer
from . models import Individual
from . forms import CustomerForm
from . forms import IndividualForm

# Create your views here.




def customer_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = CustomerForm()
        else:
            customer = Individual.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,'customer_form.html',{'form':form})

    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Individual.objects.get(pk=id)
            form = CustomerForm(request.POST, instance=customer)

        if form.is_valid():
            form.save()
        return redirect('/customers/list')




def customer_list(request):
    context = {'customer_list': Individual.objects.all()}
    return render(request,'customer_list.html',context)



def individual_customer(request,id):

    if request.method == 'GET':

        # For showing details of the customer

        customer_context = Individual.objects.get(pk=id)
        customer_details = {'fullname': customer_context.fullname, 'address': customer_context.address,
                            'mobile': customer_context.mobile, 'balence': customer_context.balence}
        print(customer_details)

        form = IndividualForm()

        # For one previous transactions
        previous =  Individual.objects.get(pk=id)
        previous_transactions = {'product' : previous.product,'price' : previous.price ,'date_created' : previous.date_created }
        print(previous_transactions)

        return render(request, 'individual.html', {'form': form, 'customer_details': customer_details,'previous_transactions' : previous_transactions})

    else:
        customer = Individual.objects.get(pk=id)
        form = IndividualForm(request.POST, instance=customer)


        if form.is_valid():
            form.save()
        return redirect('/customers/list/')



def customer_delete(request,id):
    customer = Individual.objects.get(pk=id)
    customer.delete()
    return redirect('/customers/list')