""" Aqui se crea los endpoints para poder comunicarse atraves de la url, simpre van a devolver un JSON"""

from django.views import View
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse



from .models import ModelNumero
import json


def n_primo(num):
    """ingresa un número entero y Return un dict {'num': True} """
    primos = {}
    for x in range(2, num+1):
        for i in range(2, x):
            if(x % i) == 0:
                break
            else: continue

        else:
            primos[x] = True
    return primos


def primos_gemelos(primos):
    """Ingresa un dict{'num':True} y return  una lista con la pareja de números"""
    pri_ge = []
    for i in primos.keys():
        tofind = 2 + i
        try:
            if primos[tofind]:
                print(tofind, i)
                pri_ge.append([i, tofind])
        except:
            continue
    return pri_ge
 

class NumerosImpar(View):
    """Recibe el número y devuelve los números primos """
    def get(self, request, pk=None):
        if pk:
            lista_primos = list(n_primo(pk).keys())
            print(lista_primos)
            return JsonResponse(lista_primos, safe=False)
        else:
            lista_primos = None
            return JsonResponse(lista_primos, safe=False)


class NumerosImparGemelos(View):
    """Recibe el número y devuelve los números primos gemelos en parejitas"""
    def get(self, request, pk=None):
        if pk:
            lista_primos = n_primo(pk)
            lista_primos_gemelos = primos_gemelos(lista_primos)
            return JsonResponse(lista_primos_gemelos, safe=False)
        else:
            lista_primos = None
            return JsonResponse(lista_primos, safe=False)

class RegisterNumberImpar(View):
    """Recibe el número y registra un número en la Base de datos y devuelve los números primos """
    def get(self, request, pk):
        try: 
            query = ModelNumero.objects.get(pk=pk)
            json_primos = query.primos
            return JsonResponse(json_primos, safe=False)
        except:
            dict_primos = n_primo(pk)
            json_primos =  json.dumps(list(dict_primos.keys()))
            json_gemelos = json.dumps(primos_gemelos(dict_primos))
            obje = ModelNumero.objects.create(numero=pk, primos=json_primos,  primos_gemelos=json_gemelos)
            obje.save()
            return JsonResponse(json_primos, safe=False)


class RegisterNumberGemelo(View):
    """Recibe el número y registra un número en la Base de datos y devuelve los números primos """
    def get(self, request, pk):
        try: 
            query = ModelNumero.objects.get(pk=pk)
            json_gemelos = query.primos_gemelos
            return JsonResponse(json_gemelos, safe=False)
        except:
            dict_primos = n_primo(pk)
            json_primos =  json.dumps(list(n_primo(pk).keys()))
            json_gemelos = json.dumps(primos_gemelos(dict_primos))
            obje = ModelNumero.objects.create(numero=pk, primos=json_primos,  primos_gemelos=json_gemelos)
            obje.save()
            return JsonResponse(json_gemelos, safe=False)


