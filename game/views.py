from django.shortcuts import render
from django.views import View

# Create your views here.
class RoundsPlayed(View):
    def get(self, request):
        pass

class CreateRound(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class GetRound(View):
    def get(self, request, pk):
        pass

class SendInvite(View):
    def get(self, request):
        pass

    def post(self, request):
        pass

class AcceptInvite(View):
    def get(self, request, uidb64, token):
        pass


class RejectInvite(View):
    def get(self, request, uidb64, token):
        pass