from flet import Page, SnackBar, Text


def show_snackbar(page: Page, message: str | None = None, bgcolor: str | None = None):
    page.snack_bar = SnackBar(Text(message), bgcolor=bgcolor)
    page.snack_bar.open = True
    page.update()
