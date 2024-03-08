from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response

# Create your views here.

class MovieListCreateView(generics.ListCreateAPIView):
    """
        List all movies or create a new movie.
    """
    queryset = Movie.objects.all() # The data retrieved using Movie.objects.all(), representing all Movie instances from the database.
    serializer_class = MovieSerializer # MovieSerializer, responsible for serializing and deserializing the Movie instances.

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        Retrieve, update, or delete a single movie instance.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class AllMoviesListView(generics.ListAPIView):
    """
        List all movies, but without the creation capability.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateView(generics.RetrieveUpdateAPIView):
    """
        Retrieve and update a single movie instance. Allows partial updates.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    partial = True # This allows for partial updates to the instance

class MovieDeleteView(generics.DestroyAPIView):
    """
        Delete a single movie instance.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'delete Movie'}, status=204)