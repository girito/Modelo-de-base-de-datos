from django import forms
from .models import Habitacion, Cliente, Admin, Reserva, Pago

class HabitacionForm(forms.ModelForm):
    class Meta:
        model=Habitacion
        fields=["nombre_habitacion","descripcion","capacidad","precio","estado"]

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=["dni_cliente","nombre_cliente","apellidos_cliente", "email"]

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields=["nombre_completo_admin"]

class ReservaForm(forms.ModelForm):
    class Meta:
        model=Reserva
        fields=["admin","cliente","habitacion","fecha_in","fecha_out"]

class PagoForm(forms.ModelForm):
    class Meta:
        model=Pago
        fields=["reserva","tpago"]