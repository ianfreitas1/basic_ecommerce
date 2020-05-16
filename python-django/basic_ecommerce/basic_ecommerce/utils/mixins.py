from django.shortcuts import get_object_or_404


class GetObjectMixin(object):

    def get_object(self, id):
        obj = get_object_or_404(self.queryset, pk=id)

        return obj
