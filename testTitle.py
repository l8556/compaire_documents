# title = win32gui.GetWindowText(hwnd)
# print(title)
#
# def winEnumHandler(hwnd, ctx):
#     if win32gui.IsWindowVisible(hwnd):
#         if win32gui.GetWindowText(hwnd) == 'Word' and win32gui.GetWindowText(hwnd) == 'Пароль':
#             print(hex(hwnd), win32gui.GetWindowText(hwnd))
#         elif win32gui.GetWindowText(
#                 hwnd) == 'Alimentaire_Etude_Planning_StrategiqueKM_2010.docx [Режим ограниченной функциональности] - Word':
#             print(hex(hwnd), win32gui.GetClassName(hwnd))

import win32gui


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        if win32gui.GetClassName(hwnd) == '#32770':
            print(f'class name  {win32gui.GetClassName(hwnd)}')
            print(f'Text name {win32gui.GetWindowText(hwnd)}')
            print(f'GetCapture {win32gui.GetCapture()}')
            print(f'DesktopWindow {win32gui.GetDesktopWindow()}')
            print(f'ForegroundWindow {win32gui.GetForegroundWindow()}')
            print(f'GetMenu {win32gui.GetMenu(hwnd)}')
            print(f'GetMenuItemCount {win32gui.GetMenuItemCount(hwnd)}')
            print(f'GetParent {win32gui.GetParent(hwnd)}')
            # print(f'G {win32gui.GetTextAlign(hwnd)}')
            print(f'GetTextColor {win32gui.GetTextColor(hwnd)}')
            # print(f'G {win32gui.GetTextFace(hwnd)}')
            # print(f'G {win32gui.GetTextMetrics(hwnd)}')
            print(f'GetWindowDC {win32gui.GetWindowDC(hwnd)}')
            print(f'GetWindowPlacement {win32gui.GetWindowPlacement(hwnd)}')  # получает позицию окна
            print(f'GetWindowRect {win32gui.GetWindowRect(hwnd)}')  # получает позицию окна
            print(f'GetWindowTextLength {win32gui.GetWindowTextLength(hwnd)}')
            # print(f'G {win32gui.GetDlgItemText(hwnd)}')
        else:
            print(f'class name  {win32gui.GetClassName(hwnd)}')
            print(f'Text name {win32gui.GetWindowText(hwnd)}')


win32gui.EnumWindows(winEnumHandler, None)

# from pywinauto import Desktop
#
# windows = Desktop(backend="uia").windows()
# print([w.window_text() for w in windows])
