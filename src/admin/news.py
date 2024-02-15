from typing import Any

from fastapi import Request
from sqladmin import ModelView
from wtforms import Form

from src.admin.commons.formatters import (
    MediaFormatter,
    format_date,
    format_quill,
    format_array_of_string,
    format_string_left,
)
from src.admin.commons.utils import CustomSelect2TagsField, model_change_for_editor
from src.news.models import News
from src.our_team.models import OurTeam

relation_team_fields = ["authors", "editors", "photographers"]


class NewsAdmin(ModelView, model=News):
    is_async = True

    name_plural = "Новини"
    icon = "fa-solid fa-kiwi-bird"

    can_export = False

    column_list = [
        News.title,
        News.content,
        News.slider_caption,
        News.authors,
        News.editors,
        News.photographers,
        News.preview_photo,
        News.location,
        News.category,
        News.created_at,
    ]
    column_labels = {
        News.title: "Заголовок",
        News.content: "Контент",
        News.slider_caption: "Підпис до слайдера",
        News.authors: "Автори",
        News.editors: "Редактори",
        News.photographers: "Світлини",
        News.preview_photo: "Фото прев'ю",
        News.location: "Розташування",
        News.category: "Категорія",
        News.created_at: "Дата публікації",
    }
    form_columns = [
        News.created_at,
        News.category,
        News.title,
        News.authors,
        News.editors,
        News.photographers,
        News.content,
    ]
    column_formatters = {
        News.title: format_string_left,
        News.created_at: format_date,
        News.content: format_quill,
        News.authors: format_array_of_string,
        News.editors: format_array_of_string,
        News.photographers: format_array_of_string,
        News.preview_photo: MediaFormatter(),
    }
    form_overrides = {
        **{field: CustomSelect2TagsField for field in relation_team_fields}
    }
    form_args = {
        **{field: {"model": OurTeam} for field in relation_team_fields},
    }
    form_ajax_refs = {
        "category": {
            "fields": ("name",),
            "order_by": "id",
        },
    }

    async def scaffold_form(self) -> type[Form]:
        form = await super().scaffold_form()
        form.is_editor_field = [
            "content",
        ]
        del form.content.kwargs["validators"][-1]
        return form

    async def on_model_change(
        self, data: dict, model: Any, is_created: bool, request: Request
    ) -> None:
        await model_change_for_editor(data, model, field_name="content")
        return await super().on_model_change(data, model, is_created, request)
