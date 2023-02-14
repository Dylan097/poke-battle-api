from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tutorial_level = serializers.ReadOnlyField()
    trainer_type = serializers.ReadOnlyField()
    elite_level = serializers.ReadOnlyField()
    balance = serializers.ReadOnlyField()
    gym_category = serializers.ReadOnlyField()
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'name', 'content',
            'profile_image', 'balance', 'gym_category',
            'tutorial_level', 'trainer_type', 'is_owner', 'elite_level'
        ]
