def chunk_keyboard_markup_button(buttons):
    total = len(buttons)
    if total == 3:
        return [buttons[:2], [buttons[2]]]
    elif total % 3 == 0:
        size = 3
    elif total % 2 == 0:
        size = 2
    else:
        size = 2
    return [buttons[i:i+size] for i in range(0, total, size)]

def get_option(options: dict = {}, breadcrumbs: list = []):
    selected_options = options
    for breadcrumb in breadcrumbs:
        if breadcrumbs[-1] != breadcrumb:
            selected_options = selected_options[breadcrumb]['options']
        else:
            selected_options = selected_options[breadcrumb]
    return list(selected_options['options'].keys()), selected_options

def generate_html_message(selected_option):
    reponse_message = f'{selected_option["message"]}'
    if selected_option['url'] != None:
        reponse_message = f'{reponse_message}\n\n<b>Full Link:</b> <a href="{selected_option["url"]}">Click here</a>'
    return reponse_message