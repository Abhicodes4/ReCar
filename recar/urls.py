from django.urls import path
from.import views

urlpatterns = [
    path('recar/', views.carlist),
    path('viewcar/<int:c_id>',views.carview),
    path('cata/<int:p_id>',views.carcat),
    path('create/',views.create),
    path('reg/',views.regfn),
    path('logout/',views.logoutfn),
    path('login/',views.loginfn),
    path('search/',views.searchfn),
    path('sellcar/',views.sellcarfn),
    path('editcar/<int:pro_id>',views.editcarfn),
    path('deletecar/<int:pro_id>',views.dltcarfn),
    path('SellcarfnNew/',views.SellcarfnNew.as_view()),
    path('carall/',views.Carall.as_view()),
    path('carview/<int:pk>',views.Carview.as_view()),
    path('catadd/',views.Catadd.as_view()),
    path('caradd/',views.Caradd.as_view()),
    path('Updatecars/<int:pk>',views.Updatecars.as_view()),
    path('deletecars/<int:pk>',views.Deletecars.as_view()),
    path('gallery/',views.gallery),
    path('fakestore/',views.fake),
    path('fakestoreview/<int:pid>',views.fakeview),
    path('categoryapi/',views.categoryapifn),
    path('carsapi/',views.carsviewfn),
    path('singlecarsapi/<int:cid>',views.singlecarsviewfn),
    path('addcategoryapi/',views.addcategoryapifn),
    path('editcategoryapi/',views.editcategoryapifn),
    path('apicall/',views.apicall),
    


          
]
