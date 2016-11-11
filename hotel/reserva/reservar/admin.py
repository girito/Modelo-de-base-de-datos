from django.contrib import admin

from .models import Habitacion, Cliente, Admin, Reserva, Pago
from .forms import ReservaForm, HabitacionForm, ClienteForm, AdminForm, PagoForm

class AdminHabitacion(admin.ModelAdmin):
    list_display=["__str__", "nombre_habitacion","descripcion","capacidad","precio","estado"]
    form=HabitacionForm
admin.site.register(Habitacion, AdminHabitacion)

class AdminCliente(admin.ModelAdmin):
    list_display=["__str__", "dni_cliente","nombre_cliente","apellidos_cliente"]
    form=ClienteForm
admin.site.register(Cliente, AdminCliente)

class AdminAdmin(admin.ModelAdmin):
    list_display=["__str__", "nombre_completo_admin"]
    form=AdminForm
admin.site.register(Admin, AdminAdmin)

class AdminReserva(admin.ModelAdmin):
    list_display=["__str__", "admin","cliente","habitacion","fecha_in","fecha_out"]
    form=ReservaForm
admin.site.register(Reserva, AdminReserva)

class PagoReserva(admin.ModelAdmin):
    list_display=["__str__", "reserva","tpago"]
    form=PagoForm
admin.site.register(Pago, PagoReserva)
