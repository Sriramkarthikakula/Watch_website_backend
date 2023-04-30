from django.urls import path
from . import views

urlpatterns = [
    path('cart',views.cart,name='cart'),
    path('fastrack',views.fastrack,name="fastrack"),
    path('titan',views.titan,name="titan"),
    path('trendintt11',views.trendintt11,name="trendintt11"),
    path('fastopac',views.fastopac,name="fastopac"),
    path('blackmetal',views.blackmetal,name="blackmetal"),
    path('yachtmaster',views.yachtmaster,name="yachtmaster"),
    path('rec1',views.rec1,name="rec1"),
    path('rec2',views.rec2,name="rec2"),
    path('rec3',views.rec3,name="rec3"),
    path('rec4',views.rec4,name="rec4"),
    path('rolextrend1',views.rolextrend1,name="rolextrend1"),
    path('trendfast1',views.trendfast1,name="trendfast1"),
    path('trendfast2',views.trendfast2,name="trendfast2"),
    path('sel1',views.sel1,name="sel1"),
    path('sel2',views.sel2,name="sel2"),
    path('sel3',views.sel3,name="sel3"),
    path('sel4',views.sel4,name="sel4"),
    path('payment',views.payment,name="payment")
]