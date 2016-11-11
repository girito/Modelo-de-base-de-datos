"""reserva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from reservar.views import index, AdminList, admin_create, admin_edit, \
    ClienteDetail, ClienteList, cliente_create, cliente_edit, \
    HabitacionDetail, HabitacionList, habitacion_create, habitacion_edit, \
    ReservaDetail, ReservaList, reserva_create, reserva_edit, \
    PagoDetail, PagoList, pago_create, pago_edit

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^nuevoadmin$', admin_create, name='admin_crear'),
    url(r'^listaradmin', AdminList.as_view(), name='admin_listar'),
    url(r'^editaradmin/(?P<pk>\d+)/$', admin_edit, name='admin_editar'),
    url(r'^nuevocliente$', cliente_create, name='cliente_crear'),
    url(r'^listarcliente', ClienteList.as_view(), name='cliente_listar'),
    url(r'^cliente/(?P<pk>\d+)$', ClienteDetail.as_view(), name='cliente_detail'),
    url(r'^editarcliente/(?P<pk>\d+)/$', cliente_edit, name='cliente_editar'),
    url(r'^nuevohabitacion$', habitacion_create, name='habitacion_crear'),
    url(r'^listarhabitacion', HabitacionList.as_view(), name='habitacion_listar'),
    url(r'^habitacion/(?P<pk>\d+)$', HabitacionDetail.as_view(), name='habitacion_detail'),
    url(r'^editarhabitacion/(?P<pk>\d+)/$', habitacion_edit, name='habitacion_editar'),
    url(r'^nuevoreserva$', reserva_create, name='reserva_crear'),
    url(r'^listarreserva', ReservaList.as_view(), name='reserva_listar'),
    url(r'^reserva/(?P<pk>\d+)$', ReservaDetail.as_view(), name='reserva_detail'),
    url(r'^editarreserva/(?P<pk>\d+)/$', reserva_edit, name='reserva_editar'),
    url(r'^nuevopago$', pago_create, name='pago_crear'),
    url(r'^listarpago', PagoList.as_view(), name='pago_listar'),
    url(r'^pago/(?P<pk>\d+)$', PagoDetail.as_view(), name='pago_detail'),
    url(r'^editarpago/(?P<pk>\d+)/$', pago_edit, name='pago_editar'),
]
