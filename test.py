CHOOSE_OPTION, ENTERING_TEXT = range(2)
options = {
    'Main': {
        'photo': None,
        'message': 'Welcome! How can I help you?',
        'options': {
            'Last News': {
                'photo': None,
                'message': 'latest news',
                'options': {
                    'Progressive influencer Hasan Piker tells of detention at US airport': {
                        'photo': 'https://globalnation.inquirer.net/files/2025/05/Hasan-Piker.jpg',
                        'message': 'WASHINGTON — A high-profile left-wing influencer and political commentator said Monday he was detained for hours by US border officials and interrogated about his political views. US citizen Hasan Piker — who has millions of followers on YouTube, Twitch and X, and been outspoken in his criticism of Israel — says he was held at',
                        'options': {}
                    },
                    'Trump calls US-China trade talks a \'total reset\' as both sides agree to pause tariffs for 90 days': {
                        'photo': 'https://assets.nst.com.my/images/articles/house13_NSTfield_image_listing_featured_v2.var_1747103016.jpg',
                        'message': 'Following trade talks in Geneva, the US and China agreed to pause reciprocal tariffs for 90 days. President Trump called it a “total reset”, noting improved relations and ongoing discussions to address long-term trade concerns.',
                        'options': {}
                    },
                }
            },
            'Stock Prices': {
                'photo': None,
                'message': 'Please select stock',
                'options': {
                    'AAPL': {
                        'photo': None,
                        'message': 'AAPL',
                        'options': {}
                    },
                    'TSLA': {
                        'photo': None,
                        'message': 'TSLA',
                        'options': {}
                    },
                    'META': {
                        'photo': None,
                        'message': 'META',
                        'options': {}
                    },
                    'SBUX': {
                        'photo': None,
                        'message': 'SBUX',
                        'options': {}
                    },
                    'GOOG': {
                        'photo': None,
                        'message': 'GOOG',
                        'options': {}
                    },
                    'NKE': {
                        'photo': None,
                        'message': 'NKE',
                        'options': {}
                    },
                }
            }
        }
    }
}

def chunk_buttons(buttons):
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

options_list, select_options = get_option(options=options, breadcrumbs=[])
print(chunk_buttons(options_list))
print(select_options)