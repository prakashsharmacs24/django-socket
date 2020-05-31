from django.views.generic import TemplateView


class ItemsListView(TemplateView):
    template_name = "items.html"
