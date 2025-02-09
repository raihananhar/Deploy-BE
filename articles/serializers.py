from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_title(self, value):
        if len(value) < 5:  
            raise serializers.ValidationError("Title minimal 5 karakter.")
        return value

    def validate_content(self, value):
        if len(value) < 50: 
            raise serializers.ValidationError("Content minimal 50 karakter.")
        return value

    def validate_category(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category minimal 3 karakter.")
        return value

    def validate_status(self, value):
        if value not in ["publish", "draft", "trash"]:
            raise serializers.ValidationError("Status harus 'publish', 'draft', atau 'trash'.")
        return value
