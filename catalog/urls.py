from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, PublisherViewSet, BookViewSet, BorrowerViewSet, LoanViewSet, UserLoginView, home


router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrowers', BorrowerViewSet)
router.register(r'loans', LoanViewSet)


urlpatterns =[
    # path('', home),
    path('', include(router.urls)),
    path('login', UserLoginView.as_view()),
    # path('catalog/', include(router.urls))

]

