import django_tables2 as tables
from django.utils.html import format_html

from .models import Tool, Lendlog

ATTRS = {"class": "table table-responsive table-striped table-hover"}


class LenditTable(tables.Table):
    class Meta:
        attrs = ATTRS


class LendLogTable(tables.Table):

    #status = tables.Column(order_by=("status",))
    image = tables.TemplateColumn('<img src="/media/{{record.tool.img}}" style="width:60px;"> ')
    my_column = tables.TemplateColumn(verbose_name='Auswählen',
                                      template_name='lendlog_table_button.html',
                                      orderable=False)  # orderable not sortable

    class Meta:
        model = Lendlog
        attrs = ATTRS
        fields = (
            'tool',
            'status',
            'from_date',
            'expected_end_date',
            'end_date',
            'lend_by'
        )
        sequence = (
            'image',
            'status',
            'tool',
            'from_date',
            'expected_end_date',
            'end_date',
            'lend_by'
        )

    def render_status(self, record):
        if record.status:
            return format_html('<input type="button" style=background-color:red></input>')
        else:
            return format_html('<input type="button" style=background-color:green></input>')


class ToolTable(tables.Table):

    image = tables.TemplateColumn('<img src="/media/{{record.img}}" style="width:60px;"> ')
    my_column = tables.TemplateColumn(verbose_name='Auswählen',
                                      template_name='tool_table_button.html',
                                      orderable=False)  # orderable not sortable

    class Meta:
        model = Tool
        attrs = ATTRS
        fields = (
            "name",
            "brand",
            "model",
            "owner",
            "description",
            "present_amount"
        )
        sequence = (
            'image',
            'name',
            'brand',
            'model',
            'owner',
            'description',
            'present_amount',
            'my_column'
        )

    def render_present_amount(self, record):
        if record.present_amount:
            return format_html('<input type="button" style=background-color:green value={}></input>', record.present_amount)
        else:
            return format_html('<input type="button" style=background-color:red value={}></input>', record.present_amount)


class UserTable(LenditTable):
    # We cannot use the definition via Meta here,
    # as the Usermodel cannot be imported, but needs
    # to be fetched with get_user_model()
    id = tables.Column()
    username = tables.Column()
    email = tables.Column()
