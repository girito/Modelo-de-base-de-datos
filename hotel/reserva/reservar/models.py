from django.db import models

class Habitacion(models.Model):
	estado_choices = (
        ('O', 'Ocupada'),
        ('D', 'Desocupada'),
    )
	nombre_habitacion = models.CharField(max_length=50)
	descripcion=models.CharField(max_length=200)
	capacidad=models.IntegerField()
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	estado = models.CharField(max_length=1,choices=estado_choices,default='D')
	def __str__(self):
		return self.nombre_habitacion

class Cliente(models.Model):
    dni_cliente=models.CharField(max_length=8)
    nombre_cliente = models.CharField(max_length=50)
    apellidos_cliente = models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.nombre_cliente +" "+self.apellidos_cliente

class Admin(models.Model):
    nombre_completo_admin = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_completo_admin

class Reserva(models.Model):
    admin= models.ForeignKey(Admin)
    cliente= models.ForeignKey(Cliente)
    habitacion= models.ForeignKey(Habitacion)
    fecha_in=models.DateField()
    fecha_out=models.DateField()
    def __str__(self):
        return 'Cliente: '+ str(self.cliente)+' / Habit '+ str(self.habitacion)+' / Ingreso: '+str(self.fecha_in)+' / Salida: '+str(self.fecha_out)

class Pago(models.Model):
    tpago_choices = (
        ('E', 'Efectivo'),
        ('T', 'Tarjeta'),
    )
    reserva= models.OneToOneField(Reserva)
    fecha_pago=models.DateTimeField(auto_now_add=True,auto_now=False)
    tpago= models.CharField(max_length=1,choices=tpago_choices)

