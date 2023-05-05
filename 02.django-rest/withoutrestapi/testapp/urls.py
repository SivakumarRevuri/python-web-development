from django.urls import path
from testapp.views import html_view, json_view, json_view2
from testapp.views import EmployeeClassBasedView

urlpatterns = [
    path('html/', html_view),
    path('json/', json_view),
    path('json2/', json_view2),
    path('empclass/', EmployeeClassBasedView.as_view()),
]
