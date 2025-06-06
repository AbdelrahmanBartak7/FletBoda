import flet as ft

def main(page: ft.Page):
    page.title = "قائمة المهام"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20
    page.window.width = 400
    page.window.height = 600
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(ft.Colors.BLUE_700))

    tasks = []

    task_list = ft.Column()

    def update_task_list():
        task_list.controls.clear()
        for i, task in enumerate(tasks):
            task_item = ft.Row(
                [
                    ft.Checkbox(
                        label=task["name"],
                        value=task["done"],
                        on_change=lambda e, index=i: toggle_done(index),
                        expand=True,
                        
                        
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color=ft.Colors.RED,
                        tooltip="حذف المهمة",
                        on_click=lambda e, index=i: delete_task(index),
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=10,
                height=40
            )
            task_list.controls.append(task_item)
        page.update()

    def add_task(e):
        task_name = task_input.value
        if task_name:
            tasks.append({"name": task_name, "done": False})
            task_input.value = ""
            update_task_list()

    def toggle_done(index):
        tasks[index]["done"] = not tasks[index]["done"]
        update_task_list()

    def delete_task(index):
        del tasks[index]
        update_task_list()

    task_input = ft.TextField(
        hint_text="أدخل مهمة جديدة...",
        expand=True,
        on_submit=add_task,
        border_radius=25,
        border_color=ft.Colors.BLUE_700,
        cursor_color=ft.Colors.BLUE_700
    )

    add_button = ft.IconButton(
        icon=ft.icons.ADD,
        icon_color=ft.Colors.BLUE_700,
        tooltip="إضافة مهمة جديدة",
        on_click=add_task,
    )

    page.add(
        ft.Text("قائمة المهام السريعة", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
        ft.Row([task_input, add_button], spacing=10),
        ft.Divider(height=20),
        task_list,
    )

if __name__ == "__main__":
    ft.app(target=main)
