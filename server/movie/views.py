from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response

# Create your views here.

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class AllMoviesListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    partial = True

class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'delete Movie'}, status=204)