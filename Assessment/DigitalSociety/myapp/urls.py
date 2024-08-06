from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.base),
    path('signup/',views.signup),
    path('dashboard/',views.dashboard,name='dashboard'),

    # members
    path('members/',views.members),
    path('showmembers/',views.showmembers,name='showmembers'),
    path('updatemember/<int:id>',views.updatemember),
    path('deletemember/<int:id>',views.deletemember),

    # notices
    path('addnotices/',views.addnotices),
    path('shownotices/',views.shownotices,name='shownotices'),
    path('updatenotices/<int:id>',views.updatenotices),
    path('deletenotices/<int:id>',views.deletenotices),

    # Transactions
    path('transactions/',views.transactions),
    path('showtransactions/',views.showtransactions,name='showtransactions'),
    path('deletetransactions/<int:id>',views.deletetransactions),
    path('updatetransactions/<int:id>',views.updatetransactions),

    # Watchman
    path('watchman/',views.watchman),
    path('showwatchman/',views.showwatchman,name='showwatchman'),
    path('deletewatchman/<int:id>',views.deletewatchman),
    path('updatewatchman/<int:id>',views.updatewatchman),

    # Visitors
    path('visitors/',views.visitors),
    # path('showvisitors/',views.visitors,name='showvisitors'),
    # path('deletevisitors/<int:id>',views.deletevisitors),
    # path('updatevisitors/<int:id>',views.updatevisitors),
]
