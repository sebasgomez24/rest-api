from rest_framework import generics

from status.models import Status
from .serializers import StatusSerializer

class StatusAPIView(generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' #slug

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get()

class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' #slug

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Status.objects.all()
    serializer_class            = StatusSerializer
    lookup_field                = 'id' #slug
