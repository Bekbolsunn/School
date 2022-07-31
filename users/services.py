# from rest_framework import serializers
#
#
# class PasswordField(serializers.CharField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault('style', {})
#
#         kwargs['style']['input_type'] = 'password'
#         kwargs['write_only'] = True
#
#         super().__init__(*args, **kwargs)
