from django.urls import path
from authapp import views

urlpatterns = [
    path('ati',views.ati,name='ati'),
    path('atreg',views.atreg,name='atreg'),
    path('atlog',views.atlog,name='atlog'),
    path('atregdata',views.atregdata,name='atregdata'),
    path('atlogdata',views.atlogdata,name='atlogdata'),
    path('atlogout',views.atlogout,name='atlogout'),
    path('ataprs',views.ataprs,name='ataprs'),
    path('atdecs',views.atdecs,name='atdecs'),
    path('atapnreq',views.atapnreq,name='atapnreq'),
    path('atapna',views.atapna,name='atapna'),
    path('atapnapr/<int:id>',views.atapnapr,name='atapnapr'),
    path('atapnd',views.atapnd,name='atapnd'),
    path('atapndec/<int:id>',views.atapndec,name='atapndec'),
]