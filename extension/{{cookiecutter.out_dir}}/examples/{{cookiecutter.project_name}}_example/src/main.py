import flet as ft

from {{cookiecutter.project_name}} import {{cookiecutter.control_name}}


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=300, width=300, bgcolor=ft.colors.BLUE_100, content={{cookiecutter.control_name}}(
                    tooltip="My new {{cookiecutter.control_name}} Control tooltip",
                    value = "My new {{cookiecutter.control_name}} Flet Control", 
                    color=ft.Colors.RED,
                ),),

    )


ft.app(main)
