from typing import Any
from django.views.generic import TemplateView

class IndexDashboardTemplateView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

