from django.urls import path, reverse_lazy
from .views import NumerosImpar, NumerosImparGemelos, RegisterNumberGemelo, RegisterNumberImpar

app_name='numeros'

urlpatterns = [
    path('impar/<int:pk>', NumerosImpar.as_view(), name='numeros_impar'),
    path('gemelos/<int:pk>', NumerosImparGemelos.as_view(), name='numeros_impar_gemelo'),
    path('regi-impar/<int:pk>', RegisterNumberImpar.as_view(), name='numero_impar'),
    path('regi-gemelos/<int:pk>', RegisterNumberGemelo.as_view(), name='numero_gemelo')

]