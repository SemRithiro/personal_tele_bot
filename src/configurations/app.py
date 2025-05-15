import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
NEWS_API_TOKEN = os.getenv('NEWS_API_TOKEN')

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
        'specified_size': None,
        'message': 'Here is what I can do.',
        'options': {
            'Latest News': {
                'url': None,
                'photo': None,
                'specified_size': 1,
                'message': 'Please select the news',
                'options': {'Buttigieg, eyeing a presidential run, says ‘maybe’ Biden hurt Democrats - The Washington Post': {'url': 'https://www.washingtonpost.com/politics/2025/05/13/buttigieg-president-2028-iowa-biden-trump/', 'photo': 'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/VAOTQICDDGWEZWNRF66T4ZBQJA_size-normalized.JPG&w=1440', 'specified_size': None, 'message': 'The former Biden administration official was in Iowa, where he warned in his highest-profile public appearance since leaving government not to ‘hang back’ against President Donald Trump.', 'options': {}}, 'Omaha poised to have first Black leader after mayor concedes race - CNN': {'url': 'https://www.cnn.com/2025/05/14/politics/john-ewing-omaha-mayoral-race', 'photo': 'https://media.cnn.com/api/v1/images/stellar/prod/ap25080047755168-1.jpg?c=16x9&q=w_800,c_fill', 'specified_size': None, 'message': 'Omaha’s first female mayor has conceded the city’s mayoral race to a man who is poised to become the community’s first Black mayor.', 'options': {}}, 'NBA playoffs: Thunder erase double-digit deficit to take 3-2 lead vs. Nuggets - Yahoo Sports': {'url': 'https://sports.yahoo.com/nba/breaking-news/article/nba-playoffs-thunder-erase-double-digit-deficit-to-take-3-2-lead-vs-nuggets-041022779.html', 'photo': 'https://s.yimg.com/ny/api/res/1.2/M18J5QdfkjbNAJxTKHNMDA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA7Y2Y9d2VicA--/https://s.yimg.com/os/creatr-uploaded-images/2025-05/1be05c70-3079-11f0-beff-472d00725fd6', 'specified_size': None, 'message': 'The Thunder are a win away from surviving the Nuggets.', 'options': {}}, 'Tory Lanez: Convicted killer is named as suspect in prison stabbing of rapper - BBC': {'url': 'https://www.bbc.com/news/articles/cp853w3l6k6o', 'photo': 'https://ichef.bbci.co.uk/news/1024/branded_news/93fe/live/6fd19d40-305f-11f0-a1f0-d3a54ce3ceb7.jpg', 'specified_size': None, 'message': 'Prison authorities have named Santino Casio as the inmate who allegedly stabbed the Canadian hip-hop artist 14 times.', 'options': {}}, 'Trump’s Middle East visit comes as his family deepens its business, crypto ties in the region - AP News': {'url': 'https://apnews.com/article/trump-business-interests-family-middle-east-cryptocurrency-cbb7d2354304ce0308800819944cf3f8', 'photo': 'https://dims.apnews.com/dims4/default/70017ad/2147483647/strip/true/crop/3942x2217+0+205/resize/1440x810!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Fa2%2F6d%2F088b621e6f0779835ef7134d067b%2Fc259e69c1c80464fb80dea9d41e2c158', 'specified_size': None, 'message': 'It’s not just the “gesture” of a $400 million luxury plane that President Donald Trump says he’s smart to accept from Qatar. Or that Trump effectively auctioned off the first destination on his first major foreign trip, heading to Saudi Arabia because the kin…', 'options': {}}, 'Why Cavs collapsed against Pacers in Game 5, ending season: Ashley Bastock - Cleveland.com': {'url': 'https://www.cleveland.com/cavs/2025/05/why-cavs-collapsed-against-pacers-in-game-5-ending-season-ashley-bastock.html', 'photo': 'https://www.cleveland.com/resizer/v2/U7ZVDP6ZQBGMNBTQPCFY7RXWEA.JPG?auth=e4d5470ba27f29ac3fcccb59adad0049e6d58dd99dd32293759a9c62b70e3baf&width=1280&quality=90', 'specified_size': None, 'message': "The Cavs fell apart in the second half against the Indiana Pacers, ending their season. Here's why it happened.", 'options': {}}, 'Trump defends Qatar airplane gift amid Republican criticism - Politico': {'url': 'https://www.politico.com/news/2025/05/13/trump-defends-qatar-airplane-gift-republican-criticism-00347333', 'photo': 'https://static.politico.com/c7/06/beda18d04198a322e9d95c0dd916/trump-qatar-plane-02865.jpg', 'specified_size': None, 'message': 'The president sought to cast the transaction as a win for U.S. taxpayers amid mounting criticism from his allies.', 'options': {}}, 'House Republicans grinding through marathon hearings to push ahead with Trump’s big bill - AP News': {'url': 'https://apnews.com/article/trump-budget-big-beautiful-tax-cuts-republicans-house-5588a1ba31875e5a4a2e23564244851b', 'photo': 'https://dims.apnews.com/dims4/default/73f6bdf/2147483647/strip/true/crop/8256x4644+0+430/resize/1440x810!/quality/90/?url=https%3A%2F%2Fassets.apnews.com%2Ffd%2F25%2F369171fdb34a27b2b876d99e47b4%2F55766a219ddf4338afdcc7480c4d320e', 'specified_size': None, 'message': 'Tax breaks tallying more than $5 trillion. But also sizable reductions in Medicaid health care, food stamps for older Americans and green energy strategies to fight climate change. Those all faced sharp debate as House lawmakers pushed through marathon public…', 'options': {}}, 'Paleontologists discover 506-million-year-old predator - Phys.org': {'url': 'https://phys.org/news/2025-05-paleontologists-million-year-predator.html', 'photo': 'https://scx2.b-cdn.net/gfx/news/hires/2025/manitoba-museum-and-ro.jpg', 'specified_size': None, 'message': 'Paleontologists at the Manitoba Museum and Royal Ontario Museum (ROM) have discovered a remarkable new 506-million-year-old predator from the Burgess Shale of Canada. The results are announced in a paper in the journal Royal Society Open Science.', 'options': {}}, "Celtics' Jayson Tatum undergoes surgery to repair ruptured Achilles tendon - NBA": {'url': 'https://www.nba.com/news/celtics-jayson-tatum-surgery-ruptured-right-achilles', 'photo': 'https://cdn.nba.com/manage/2025/05/GettyImages-2212806091-scaled-e1747171845374.jpg', 'specified_size': None, 'message': "The Celtics All-Star guard was injured late in Game 4 of Boston's East semifinals series against New York.", 'options': {}}, "Cassie Ventura gives testimony at Sean 'Diddy' Combs' trial about violence, 'freak offs' - NBC News": {'url': 'https://www.nbcnews.com/news/us-news/live-blog/sean-diddy-combs-trial-day-2-live-updates-rcna206319', 'photo': 'https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1200-630,f_auto,q_auto:best/rockcms/2024-09/240917-sean-diddy-combs-mn-0905-17d5ac.jpg', 'specified_size': None, 'message': 'Read the latest news on the Sean "Diddy" Combs trial in New York. Cassie Ventura, Combs\' ex-girlfriend, took the stand as the government\'s star witness.', 'options': {}}, "Two-time Academy Award winner blasts 'America's philistine president' at Cannes - SFGATE": {'url': 'https://www.sfgate.com/sf-culture/article/robert-de-niro-blasts-philistine-president-cannes-20325537.php', 'photo': 'https://s.hdnux.com/photos/01/50/26/37/27355107/3/rawImage.jpg', 'specified_size': None, 'message': "Accepting a lifetime achievement award at Cannes, Robert De Niro used his speech to denounce President Donald Trump's defunding of the arts.", 'options': {}}, 'Microsoft Layoffs Impact 7,000 Workers As Company Adjusts For AI - Forbes': {'url': 'https://www.forbes.com/sites/chriswestfall/2025/05/13/microsoft-layoffs-impact-7000-workers-as-company-adjusts-for-ai/', 'photo': 'https://imageio.forbes.com/specials-images/imageserve/6823b106d98e6da1284e8aa8/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds', 'specified_size': None, 'message': "In a move signaling a significant strategic pivot, Microsoft today announced a reduction of its workforce by approximately 7,000 employees. Here's why.", 'options': {}}, 'Trump pulls sanctions on Syria, extends olive branch to Iran - The Washington Post': {'url': 'https://www.washingtonpost.com/politics/2025/05/13/trump-iran-syria-middle-east/', 'photo': 'https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/WNEPOY3YZVX6NQCOWZQMSOSZRE.JPG&w=1440', 'specified_size': None, 'message': 'President Donald Trump’s visit to Saudi Arabia marks a significant shift in U.S. foreign policy in the Middle East.', 'options': {}}, 'The Dallas Mavericks will select Cooper Flagg with first overall pick in the 2025 NBA Draft - Mavs Moneyball': {'url': 'https://www.mavsmoneyball.com/2025/5/13/24429595/nba-draft-lottery-2025-dallas-mavericks-cooper-flagg-first-overall-pick-i', 'photo': 'https://cdn.vox-cdn.com/thumbor/M-I7Pz_6UixkxtltS2xn4NuIG7o=/0x0:5464x2861/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/25993146/2214886068.jpg', 'specified_size': None, 'message': 'According to ESPN’s Tim MacMahon, Dallas won’t do anything crazy', 'options': {}}, "Trump administration's universal flu vaccine project puzzles scientists - NPR": {'url': 'https://www.npr.org/sections/shots-health-news/2025/05/13/nx-s1-5384934/trump-universal-flu-vaccine', 'photo': 'https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5623x3163+0+0/resize/1400/quality/100/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F96%2F83%2F6d70801045b4b5be1f5f0fa1873a%2Fgettyimages-1328336163.jpg', 'specified_size': None, 'message': "The Trump administration has launched a $500 million project to develop a universal flu vaccine that won't need yearly updates. But vaccine experts are mystified by its focus on a dated technology.", 'options': {}}, 'White House welcomes Afrikaners to the U.S., but drops protection for Afghan allies - NPR': {'url': 'https://www.npr.org/2025/05/13/nx-s1-5397007/trump-tps-afghanistan-afrikaner', 'photo': 'https://npr.brightspotcdn.com/dims3/default/strip/false/crop/5672x3191+0+295/resize/1400/quality/100/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Fe1%2Ff0%2Fc45fae1049b3a5848d6dad2c985f%2Fap22292737819258.jpg', 'specified_size': None, 'message': 'Veterans and others express outrage as the Trump administration ends special protective status for Afghans who had relocated to the U.S.', 'options': {}}}
            },
            'Stock Prices': {
                'url': None,
                'photo': None,
                'specified_size': None,
                'message': 'Which one you interested in?',
                'options': {
                    'AAPL': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'AAPL',
                        'options': {}
                    },
                    'TSLA': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'TSLA',
                        'options': {}
                    },
                    'META': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'META',
                        'options': {}
                    },
                    'SBUX': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'SBUX',
                        'options': {}
                    },
                    'GOOG': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'GOOG',
                        'options': {}
                    },
                    'NKE': {
                        'url': None,
                        'photo': None,
                        'specified_size': None,
                        'message': 'NKE',
                        'options': {}
                    },
                }
            }
        }
    }
}