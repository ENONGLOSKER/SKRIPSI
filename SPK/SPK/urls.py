"""
URL configuration for SPK project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from spk_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('__debug__/', include('debug_toolbar.urls')),
    # admin
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard_admin, name='dashboard'),
    # jadwal
    path('dashboard/jadwal/', views.dashboard_jadwal, name='dashboard_jadwal'),
    path('dashboard/jadwal/create/', views.tambah_jadwal, name='tambah_jadwal'),
    path('dashboard/jadwal/update/<int:id>/', views.edit_jadwal, name='edit_jadwal'),
    path('dashboard/jadwal/delete/<int:id>/', views.hapus_jadwal, name='hapus_jadwal'),
    # kriteria
    path('dashboard/kriteria/', views.dashboard_kriteria, name='kriteria'),
    path('dashboard/kriteria/create/', views.tambah_kriteria, name='kriteria_create'),
    path('dashboard/kriteria/update/<int:id>/', views.edit_kriteria, name='kriteria_edit'),
    path('dashboard/kriteria/delete/<int:id>/', views.hapus_kriteria, name='kriteria_delete'),
    # subkriteria
    path('dashboard/kriteria/sub/<int:id>/', views.dashboard_subkriteria, name='subkriteria'),
    path('dashboard/kriteria/sub/create/', views.tambah_subkriteria, name='subkriteria_create'),
    path('dashboard/kriteria/sub/update/<int:id>/', views.edit_subkriteria, name='subkriteria_edit'),
    path('dashboard/kriteria/sub/delete/<int:id>/', views.hapus_subkriteria, name='subkriteria_delete'),

    # alternatif
    path('dashboard/alternatif/', views.dashboard_alternatif, name='alternatif'),
    path('dashboard/alternatif/create/', views.tambah_alternatif, name='alternatif_create'),
    path('dashboard/alternatif/update/<int:id>/', views.edit_alternatif, name='alternatif_edit'),
    path('dashboard/alternatif/delete/<int:id>/', views.hapus_alternatif, name='alternatif_delete'),
    path('dashboard/user/update/<int:id>/', views.edit_user, name='user_edit'),
    path('dashboard/user/delete/<int:id>/', views.hapus_user, name='user_delete'),
    
    # bobot
    path('dashboard/bobot', views.dashboard_bobot, name='bobot'),
    path('dashboard/bobot/create/', views.tambah_bobot, name='bobot_create'),
    path('dashboard/bobot/update/<int:id>/', views.edit_bobot, name='bobot_edit'),
    path('dashboard/bobot/delete/<int:id>/', views.hapus_bobot, name='bobot_delete'),

    # penilaian
    path('dashboard/penilaian', views.dashboard_penilaian, name='penilaian'),
    path('dashboard/penilaian/create/', views.tambah_penilaian, name='penilaian_create'),
    path('dashboard/penilaian/update/<int:id>/', views.edit_penilaian, name='penilaian_edit'),
    path('dashboard/penilaian/delete/<int:id>/', views.hapus_penilaian, name='penilaian_delete'),

    # perengkingan
    path('dashboard/rengking/', views.dashboard_rengking, name='rengking'),

    # penilaian
    path('dashboard/penilaian/gap/', views.penilaian_gap, name='penilaian_gap'),
    path('hitung-rengking/', views.hitung_rengking, name='hitung_rengking'),
    path('hitung-hasil/', views.hitung_hasil, name='hitung_hasil'),

    path('dashboard/penilaian/gap/reset', views.penilaian_gap_reset, name='penilaian_gap_reset'),
    path('dashboard/penilaian/rengking/reset', views.penilaian_rengking_reset, name='penilaian_rengking_reset'),
    path('dashboard/penilaian/hasil/reset', views.penilaian_hasil_reset, name='penilaian_hasil_reset'),

    # user
    path('user/detail/', views.detail_user, name='detail'),
    # auth
    path('', views.index, name='index'),
    path('signup/', views.create_custom_user, name='signup'),
    path('signin/', views.singin_user, name='signin'),
    path('signout/', views.signout_user, name='signout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


