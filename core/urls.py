from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin Dashboard
    path('admin/', views.admin_dashboard, name='admin_dashboard'),

    # Haydovchilar
    path('admin/drivers/', views.admin_drivers, name='admin_drivers'),
    path('admin/drivers/add/', views.admin_driver_add, name='admin_driver_add'),
    path('admin/drivers/<int:pk>/edit/', views.admin_driver_edit, name='admin_driver_edit'),
    path('admin/drivers/<int:pk>/delete/', views.admin_driver_delete, name='admin_driver_delete'),
    path('admin/drivers/<int:pk>/', views.admin_driver_detail, name='admin_driver_detail'),
    path('admin/drivers/<int:pk>/sms/', views.admin_driver_sms, name='admin_driver_sms'),

    # Putyovkalar
    path('admin/putyovkalar/', views.admin_putyovkalar, name='admin_putyovkalar'),
    path('admin/putyovkalar/add/', views.admin_putyovka_add, name='admin_putyovka_add'),
    path('admin/putyovkalar/<int:pk>/edit/', views.admin_putyovka_edit, name='admin_putyovka_edit'),
    path('admin/putyovkalar/<int:pk>/delete/', views.admin_putyovka_delete, name='admin_putyovka_delete'),
    path('admin/putyovkalar/<int:pk>/tolov/', views.admin_putyovka_tolov, name='admin_putyovka_tolov'),
    path('admin/putyovkalar/<int:pk>/word/', views.putyovka_word, name='putyovka_word'),
    path('admin/putyovkalar/<int:pk>/activate/', views.admin_putyovka_activate, name='admin_putyovka_activate'),

    # TIRlar
    path('admin/tirlar/', views.admin_tirlar, name='admin_tirlar'),
    path('admin/tirlar/add/', views.admin_tir_add, name='admin_tir_add'),
    path('admin/tirlar/<int:pk>/edit/', views.admin_tir_edit, name='admin_tir_edit'),
    path('admin/tirlar/<int:pk>/delete/', views.admin_tir_delete, name='admin_tir_delete'),
    path('admin/tirlar/<int:pk>/finish/', views.admin_tir_finish, name='admin_tir_finish'),
    path('admin/tirlar/<int:pk>/tolov/', views.admin_tir_tolov, name='admin_tir_tolov'),
    path('admin/tirlar/<int:pk>/activate/', views.admin_tir_activate, name='admin_tir_activate'),

    # Dazvollar
    path('admin/dazvollar/', views.admin_dazvollar, name='admin_dazvollar'),
    path('admin/dazvollar/add/', views.admin_dazvol_add, name='admin_dazvol_add'),
    path('admin/dazvollar/<int:pk>/edit/', views.admin_dazvol_edit, name='admin_dazvol_edit'),
    path('admin/dazvollar/<int:pk>/delete/', views.admin_dazvol_delete, name='admin_dazvol_delete'),
    path('admin/dazvollar/<int:pk>/finish/', views.admin_dazvol_finish, name='admin_dazvol_finish'),
    path('admin/dazvollar/<int:pk>/tolov/', views.admin_dazvol_tolov, name='admin_dazvol_tolov'),
    path('admin/dazvollar/<int:pk>/activate/', views.admin_dazvol_activate, name='admin_dazvol_activate'),

    # Litsenziyalar
    path('admin/litsenziyalar/', views.admin_litsenziyalar, name='admin_litsenziyalar'),
    path('admin/litsenziyalar/add/', views.admin_litsenziya_add, name='admin_litsenziya_add'),
    path('admin/litsenziyalar/<int:pk>/edit/', views.admin_litsenziya_edit, name='admin_litsenziya_edit'),
    path('admin/litsenziyalar/<int:pk>/delete/', views.admin_litsenziya_delete, name='admin_litsenziya_delete'),
    path('admin/litsenziyalar/<int:pk>/finish/', views.admin_litsenziya_finish, name='admin_litsenziya_finish'),
    path('admin/litsenziyalar/<int:pk>/tolov/', views.admin_litsenziya_tolov, name='admin_litsenziya_tolov'),
    path('admin/litsenziyalar/<int:pk>/activate/', views.admin_litsenziya_activate, name='admin_litsenziya_activate'),

    # Ijara
    path('admin/ijara/', views.admin_ijara, name='admin_ijara'),
    path('admin/ijara/add/', views.admin_ijara_add, name='admin_ijara_add'),
    path('admin/ijara/<int:pk>/edit/', views.admin_ijara_edit, name='admin_ijara_edit'),
    path('admin/ijara/<int:pk>/delete/', views.admin_ijara_delete, name='admin_ijara_delete'),
    path('admin/ijara/<int:pk>/finish/', views.admin_ijara_finish, name='admin_ijara_finish'),
    path('admin/ijara/<int:pk>/tolov/', views.admin_ijara_tolov, name='admin_ijara_tolov'),
    path('admin/ijara/<int:pk>/activate/', views.admin_ijara_activate, name='admin_ijara_activate'),

    # Chiqimlar
    path('admin/chiqimlar/', views.admin_chiqimlar, name='admin_chiqimlar'),
    path('admin/chiqimlar/add/', views.admin_chiqim_add, name='admin_chiqim_add'),
    path('admin/chiqimlar/<int:pk>/delete/', views.admin_chiqim_delete, name='admin_chiqim_delete'),


    # Admin management
    path('admin/admins/', views.admin_add_admin, name='admin_add_admin'),
    path('admin/admins/<int:pk>/delete/', views.admin_delete_admin, name='admin_delete_admin'),
    # Driver
    path('driver/', views.driver_dashboard, name='driver_dashboard'),

    # Word export for driver
    path('admin/drivers/<int:pk>/blanka/', views.driver_blanka_word, name='driver_blanka_word'),
    path('admin/drivers/<int:pk>/doverennost/', views.driver_doverennost_word, name='driver_doverennost_word'),
]
