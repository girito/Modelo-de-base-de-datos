from django.contrib import admin

from .models import Habitacion
from .models import Cliente
from .models import Admin
from .models import Fecha
from .models import Reserva
from .models import TipoPago
from .models import Pago

class AdminHabitacion(admin.ModelAdmin):
	list_display=["__str__", "nombre_habitacion","descripcion","capacidad","precio","estado"]
	class Meta:
		model=Habitacion
	# search_fields=["nombre_habitacion"]
	# ordering =["nombre_habitacion"]

admin.site.register(Habitacion, AdminHabitacion)

class AdminCliente(admin.ModelAdmin):
	list_display=["__str__", "nombre_cliente","apellidos_cliente","dni_cliente"]
	class Meta:
		model=Cliente

admin.site.register(Cliente, AdminCliente)

class AdminAdmin(admin.ModelAdmin):
	list_display=["__str__", "nombre_completo_admin"]
	class Meta:
		model=Admin

admin.site.register(Admin, AdminAdmin)

class AdminFecha(admin.ModelAdmin):
	list_display=["__str__", "dia","mes","año"]
	class Meta:
		model=Fecha

admin.site.register(Fecha, AdminFecha)

class AdminReserva(admin.ModelAdmin):
	list_display=["__str__", "admin","cliente","habitacion","fecha_in","fecha_out"]
	class Meta:
		model=Reserva

admin.site.register(Reserva, AdminReserva)

class AdminTipoPago(admin.ModelAdmin):
	list_display=["__str__", "tpago"]
	class Meta:
		model=TipoPago

admin.site.register(TipoPago, AdminTipoPago)

class AdminPago(admin.ModelAdmin):
	list_display=["__str__", "reserva","fecha","tipopago"]
	class Meta:
		model=Pago

admin.site.register(Pago, AdminPago)
