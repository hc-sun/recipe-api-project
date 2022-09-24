from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    '''
    To authenticate:
    receive TOKEN RESPONSE in /api/user/token/
    authorize "Token TOKEN RESPONSE" in tokenAuth
    '''
    # serializer_class = serializers.RecipeSerializer
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return self.request.user
        # filter authenticated user
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        # override to save authticated user recipe
        serializer.save(user=self.request.user)
