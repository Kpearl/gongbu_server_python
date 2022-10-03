from rest_framework import serializers
from users.models import Users


class UsersSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    nickname = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    birth = serializers.CharField(required=False)

    class Meta:
        model = Users
        fields = ('email', 'password', 'nickname', 'phone', 'birth')

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.birth = validated_data.get('birth', instance.birth)

        instance.save()
        return instance