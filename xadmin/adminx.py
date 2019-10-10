import xadmin
from stu.models import StudentInfo
from xadmin.views import BaseAdminView, CommAdminView


class StudentInfoAdmin:
    # 在列表页中需要显示的内容
    list_display = ['no', 'name', 'age', 'classes_begin_date', 'city']
    # 在列表页可以修改的数据参数
    list_editable = ['name', 'age', 'classes_begin_date', 'city']
    # 添加按字段搜索功能
    search_fields = ['name', 'classes_begin_date', 'age', 'city', 'native_place']
    # 过滤功能,提供范围查找功能
    list_filter = ['age', 'classes_begin_date']
    # 排序（默认按照id逆序排序）
    ordering = ['id']
    # 分页
    list_per_page = 5


class SettingAdmin:
    site_title = "人通后台管理"
    site_footer = site_title
    menu_style = 'accordion'


class MyBaseAdmin:
    # 开启主题
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(StudentInfo, StudentInfoAdmin)
xadmin.site.register(BaseAdminView, MyBaseAdmin)
xadmin.site.register(CommAdminView, SettingAdmin)
