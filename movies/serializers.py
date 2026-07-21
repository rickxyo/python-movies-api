from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
    def validate_release_date(self, value):
        if value.year < 1895:
            raise serializers.ValidationError('Release date cannot be earlier than 1895.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Description cannot exceed 200 characters')
        return value