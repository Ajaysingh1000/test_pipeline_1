from rest_framework import serializers
# from django.contrib.auth.models import User
# from django.db import IntegrityError
# import django


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=4, max_length=20)
    email = serializers.EmailField()
    password = serializers.CharField(
        min_length=8, write_only=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords must match."})
        return data

    # def create(self, validated_data):
    #     validated_data.pop('confirm_password')
    #     try:
    #         user = User.objects.create_user(**validated_data)
    #         return user
    #     except IntegrityError as e:
    #         if 'username' in str(e):
    #             raise serializers.ValidationError({"username": "This username already exists."})
    #         elif 'email' in str(e):
    #             raise serializers.ValidationError({"email": "This email already exists."})
    #         raise e


data = {
    "username": "ajay",
    "email": "ajay@gmail.com",
    "password": "ajay@156",
    "confirm_password": "ajay@156",
}
st = UserRegistrationSerializer(data=data)
st.is_valid(raise_exception=True)
print(st.validated_data)  # Will show data without confirm_password
# user = st.save()  # Now properly returns the user object