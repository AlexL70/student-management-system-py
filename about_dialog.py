from PyQt6.QtWidgets import QMessageBox


class AboutDialog(QMessageBox):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("About")
        content = """\
        This is a simple student management system. It is created as a part or the Python Mega Course on Udemy. \
        Here is the link to the course: https://www.udemy.com/course/the-python-mega-course/
        Please feel free to use this code for educational purposes.
        """
        self.setText(content)
        info = """
        Developed by: Alex Levinson
        alexander.levinson.70@gmail.com
        """
        self.setInformativeText(info)
        self.setIcon(QMessageBox.Icon.Information)
