# Подключаем статус
from rest_framework import status

# Подключаем компонент для ответа
from rest_framework.response import Response

# Подключаем компонент для создания данных
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView

# Подключаем компонент для прав доступа
from rest_framework.permissions import AllowAny

# Подключаем модель User
from .models import Teacher

# Подключаем UserRegistrSerializer
from .serializers import UserRegisterSerializer, LoginSerializer


# Создаём класс RegistrUserView
class RegistrationAPIView(CreateAPIView):
    # Добавляем в queryset
    queryset = Teacher.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)

        # data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"status": "User register successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            data = serializer.errors
            return Response(data)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    # renderer_classes = (UserJSONRenderer,)
    def post(self, request):
        data = {"error": status.HTTP_400_BAD_REQUEST}
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data)
