from inlineedit.adaptors.basic import BasicAdaptor
from django.forms import Field as DjangoFormField
from django.db.models import Model as DjangoModel, Field as DjangoField
from django.utils.html import format_html
from django.contrib.auth.models import User, AnonymousUser
from typing import Union, Optional
from ckeditor.widgets import CKEditorWidget


class CKEditorAdaptor(BasicAdaptor):
    ADAPTOR_NAME = "ckeditor"

    def __init__(
            self,
            model_object: DjangoModel,
            field: DjangoField,
            user_object: Optional[Union[User, AnonymousUser]] = None,
            ckeditor_config: str = "default"
    ):
        super().__init__(model_object, field, user_object)
        self._ckeditor_config = ckeditor_config

    def form_field(self) -> DjangoFormField:
        form_field = super().form_field()
        form_field.widget = CKEditorWidget(config_name=self._ckeditor_config)
        return form_field

    def display_value(self) -> str:
        return format_html(self.db_value())