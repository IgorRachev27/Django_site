from django.shortcuts import render
from .models import Order
from .forms import OrderForm, OrderForm2
from telebot.sendmessage import sendTelegram

# Create your views here.
def main_page(request):
    form = OrderForm()
    form2=OrderForm2()
    dict_obj = {'form':form,'form2':form2}
    return render(request, "./maga_autoservice.html", dict_obj)

def thanks(request):
    if request.POST:
        form = OrderForm()
        form2 = OrderForm2()
        name = request.POST['name']
        phone = request.POST['phone']
        date = request.POST['date']
        element = Order(order_name=name, order_phone=phone, coming_date=date)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone, tg_coming_date=date)
        return render(request, './thanks.html', {"form":form,'form2':form2})
    else:
        return render(request, './thanks.html')

def gallery(request):
    form = OrderForm()
    return render(request, './gallery.html',{"form":form})