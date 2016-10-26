from django.db import models

class Habitacion(models.Model):
	estado_choices = (
        ('1', 'Ocupada'),
        ('0', 'Desocupada'),
    )
	nombre_habitacion = models.CharField(max_length=50)
	descripcion=models.CharField(max_length=200)
	capacidad=models.IntegerField()
	precio=models.DecimalField(max_digits=5, decimal_places=2)
	estado = models.CharField(max_length=1,choices=estado_choices,default='0')

	def __str__(self):
		return self.nombre_habitacion

class Cliente(models.Model):
    dni_cliente=models.IntegerField()
    nombre_cliente = models.CharField(max_length=50)
    apellidos_cliente = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_cliente

class Admin(models.Model):
    nombre_completo_admin = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_completo_admin

class Fecha(models.Model):
    dia = models.IntegerField()
    mes = models.IntegerField()
    año=models.IntegerField()
    def __str__(self):
        return self.dia+'/'+self.mes+'/'+self.año

class Reserva(models.Model):
    admin= models.ForeignKey(Admin)
    cliente= models.ForeignKey(Cliente)
    habitacion= models.ForeignKey(Habitacion)
    fecha_in=models.ForeignKey(Fecha, related_name = 'fecha_in')
    fecha_out=models.ForeignKey(Fecha, related_name = 'fecha_out')
    def __str__(self):
        return self.fecha_in+', '+self.fecha_out

class TipoPago(models.Model):
	tpago_choices = (
        ('E', 'Efectivo'),
        ('T', 'Tarjeta'),
    )
	tpago= models.CharField(max_length=1,choices=tpago_choices)

class Pago(models.Model):
    reserva= models.OneToOneField(Reserva)
    fecha=models.ForeignKey(Fecha)
    tipopago=models.ForeignKey(TipoPago)
    def __str__(self):
        return self.reserva

