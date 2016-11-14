from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.contrib import messages

from .forms import AdminForm, HabitacionForm, ClienteForm, ReservaForm, PagoForm
from .models import Habitacion, Cliente, Admin, Reserva, Pago

def index(request):
    return render(request, "index.html")

#titulos
tituloa="Administradores"
tituloc="Clientes"
tituloh="Habitaciones"
titulor="Reservas"
titulop="Pagos"
# Administrador
class AdminList(ListView):
    model = Admin
    template_name = "admin_list.html"

def admin_create(request):
    form=AdminForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        nombre=form.cleaned_data.get("nombre_completo_admin")
        form.save()
        messages.success(request, "Administrador(a) %s, registrado(a) con exito. " %(nombre))
        return HttpResponseRedirect(request.path)
    return render(request,"create.html",{"titulo":tituloa,"form":form})

def admin_edit(request, pk):
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return HttpResponseRedirect(reverse("admin_listar"))
    if request.method == "GET":
        form = AdminForm(instance=admin)
    else:
        form = AdminForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            messages.success(request, "Administrador actualizado con exito.")
            return redirect("admin_listar")
    return render(request, "create.html", {"titulo":tituloa,"form":form})

# Cliente
class ClienteDetail(DetailView):
    model = Cliente
    template_name = "cliente_detail.html"

class ClienteList(ListView):
    model = Cliente
    template_name = "cliente_list.html"

def cliente_create(request):
    form=ClienteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        nombre=form.cleaned_data.get("nombre_cliente")
        form.save()
        messages.success(request, "Cliente %s, registrado con exito. " %(nombre))
        return HttpResponseRedirect(request.path)
    return render(request,"create.html",{"titulo":tituloc,"form":form})

def cliente_edit(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        return HttpResponseRedirect(reverse("cliente_listar"))
    if request.method == "GET":
        form = ClienteForm(instance=cliente)
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente actualizado con exito.")
            return redirect("cliente_listar")
    return render(request, "create.html", {"titulo":tituloc,"form":form})

# Habitacion
class HabitacionDetail(DetailView):
    model = Habitacion
    template_name = "habitacion_detail.html"

class HabitacionList(ListView):
    model = Habitacion
    template_name = "habitacion_list.html"

def habitacion_create(request):
    form=HabitacionForm(request.POST or None, request.FILES or None)
    queryset=Habitacion.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, "Habitación registrada con exito.")
        return HttpResponseRedirect(request.path)
    return render(request,"create.html",{"titulo":tituloh,"form":form})

def habitacion_edit(request, pk):
    try:
        habitacion = Habitacion.objects.get(pk=pk)
    except Habitacion.DoesNotExist:
        return HttpResponseRedirect(reverse("habitacion_listar"))
    if request.method == "GET":
        form = HabitacionForm(instance=habitacion)
    else:
        form = HabitacionForm(request.POST, instance=habitacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Habitación actualizada con exito.")
            return redirect("habitacion_listar")
    return render(request, "create.html", {"titulo":tituloh,"form":form})

# Reserva
class ReservaDetail(DetailView):
    model = Reserva
    template_name = "reserva_detail.html"

class ReservaList(ListView):
    model = Reserva
    template_name = "reserva_list.html"

def validar_fecha(request,form,queryset):
    fechain=form.cleaned_data.get("fecha_in")
    fechaout=form.cleaned_data.get("fecha_out")
    habit=form.cleaned_data.get("habitacion")
    ban=0
    if fechain <= fechaout:
        for reserva in queryset:
            if habit==reserva.habitacion \
                and ((fechain >= reserva.fecha_in and fechain <= reserva.fecha_out and fechaout >= reserva.fecha_in and fechaout <= reserva.fecha_out) \
                or (fechain < reserva.fecha_in and fechaout > reserva.fecha_out) \
                or (fechain <= reserva.fecha_out and fechain >= reserva.fecha_in and fechaout >= reserva.fecha_out) \
                or (fechaout <= reserva.fecha_out and fechaout >= reserva.fecha_in and fechain <= reserva.fecha_in)):
                ban=1
    else:
        ban=2
    return ban

def reserva_create(request):
    form=ReservaForm(request.POST or None, request.FILES or None)
    queryset=Reserva.objects.all()
    if form.is_valid():
        ban=validar_fecha(request, form,queryset)
        if ban==2:
            messages.warning(request, "Las fechas no son validas.")
        if ban==1:
            messages.warning(request, "La habitacion ya esta reservada en esas fechas.")
        if ban==0:
            form.save()
            messages.success(request, "Reserva registrada con exito.")
            return HttpResponseRedirect(request.path)
    return render(request,"create.html",{"titulo":titulor,"form":form})

def reserva_edit(request, pk):
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return HttpResponseRedirect(reverse("reserva_listar"))
    if request.method == "GET":
        form = ReservaForm(instance=reserva)
    else:
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            queryset=Reserva.objects.all().exclude(pk=pk)
            ban=validar_fecha(request,form,queryset)
            if ban==2:
                messages.warning(request, "Las fechas no son validas.")
            if ban==1:
                messages.warning(request, "La habitacion ya esta reservada en esas fechas.")
            if ban==0:
                form.save()
                messages.success(request, "Reserva actualizada con exito.")
                return redirect("reserva_listar")
    return render(request, "create.html", {"titulo":titulor,"form":form})

# Pago
class PagoDetail(DetailView):
    model = Pago
    template_name = "pago_detail.html"

class PagoList(ListView):
    model = Pago
    template_name = "pago_list.html"

def pago_create(request):
    titulo="Pagos"
    form=PagoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Pago registrado con exito.")
        return HttpResponseRedirect(request.path)
    return render(request,"create.html",{"titulo":titulop,"form":form})

def pago_edit(request, pk):
    try:
        pago = Pago.objects.get(pk=pk)
    except Pago.DoesNotExist:
        return HttpResponseRedirect(reverse("pago_listar"))
    if request.method == "GET":
        form = PagoForm(instance=pago)
    else:
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            messages.success(request, "Pago actualizado con exito.")
            return redirect("pago_listar")
    return render(request, "create.html", {"titulo":titulop,"form":form})