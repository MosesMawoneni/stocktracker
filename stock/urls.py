from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("items", views.ItemViewSet)
router.register("workers", views.WorkerViewSet)
router.register("issues", views.IssueViewSet)
router.register("personnel", views.PersonnelViewSet)

urlpatterns = []

urlpatterns += router.urls
