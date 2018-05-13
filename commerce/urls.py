from django.urls import path
from.import views
app_name="commerce"
urlpatterns=[
      path("accueil/",views.accueil, name='accueil'),
      path("detail/<product_id>",views.detail,name='detail'),
      path("product/<product_id>",views.display_product, name='display_product'),
      path("commande/<product_id>",views.commande,name="commande"),
       ]

