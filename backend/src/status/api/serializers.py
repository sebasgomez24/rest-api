from rest_framework import serializers

from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    # def validate_content(self, value):
    #     content - data.get('content', None)
    #     if len(content) > 240
    #         raise forms.ValidationError("Content is too long")
    #     return content

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data