import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

CHOOSE_OPTION, ENTERING_TEXT = range(2)

ABOUT_ME_TEXT = (
            "🤖 <b>About This Bot</b>\n"
            "This bot was developed using <b>Python</b> and the <i>python-telegram-bot</i> library.\n\n"
            "👨‍💻 <b>Developer:</b> Sem Rithiro\n"
            "📧 <b>Email:</b> rithiro@gmail.com\n"
            "🌐 <b>Portfolio:</b> <a href='https://semrithiro.github.io/curriculumn_vitae'>semrithiro.github.io</a>"
)

OPTIONS = {
    'Main': {
        'url': None,
        'photo': None,
        'message': 'Here is what I can do.',
        'options': {
            'Latest News': {
                'url': None,
                'photo': None,
                'message': 'Please select the news',
                'options': {
                    'Progressive influencer Hasan Piker tells of detention at US airport': {
                        'url': 'https://globalnation.inquirer.net/276848/progressive-influencer-hasan-piker-tells-of-detention-at-us-airport',
                        'photo': None,
                        'message': 'Progressive influencer Hasan Piker tells of detention at US airport',
                        'options': {}
                    },
                    'Trump calls US-China trade talks a \'total reset\' as both sides agree to pause tariffs for 90 days': {
                        'url': 'https://newsable.asianetnews.com/world/trump-calls-us-china-trade-talks-a-total-reset-as-both-sides-agree-to-pause-tariffs-for-90-days-kmv/articleshow-1oe18xg',
                        'photo': None,
                        'message': 'Trump calls US-China trade talks a \'total reset\' as both sides agree to pause tariffs for 90 days',
                        'options': {}
                    },
                }
            },
            'Stock Prices': {
                'url': None,
                'photo': None,
                'message': 'Which one you interested in?',
                'options': {
                    'AAPL': {
                        'url': None,
                        'photo': None,
                        'message': 'AAPL',
                        'options': {}
                    },
                    'TSLA': {
                        'url': None,
                        'photo': None,
                        'message': 'TSLA',
                        'options': {}
                    },
                    'META': {
                        'url': None,
                        'photo': None,
                        'message': 'META',
                        'options': {}
                    },
                    'SBUX': {
                        'url': None,
                        'photo': None,
                        'message': 'SBUX',
                        'options': {}
                    },
                    'GOOG': {
                        'url': None,
                        'photo': None,
                        'message': 'GOOG',
                        'options': {}
                    },
                    'NKE': {
                        'url': None,
                        'photo': None,
                        'message': 'NKE',
                        'options': {}
                    },
                }
            }
        }
    }
}