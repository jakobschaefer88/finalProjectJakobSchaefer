'''
INF601 - Programming in Python
Final Project
I, Jakob Schaefer, affirm that the work submitted for this assignment is entirely my own.
I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials.
I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards.
I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies.
By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.

__init__.py file

'''

#importing each of the Widgets
from .fortuneCookie import FortuneCookieWidget
from .joke import JokeWidget
from .quote import QuoteWidget
from .news import NewsWidget
from .wordOfDay import WordOfDayWidget
from .weather import WeatherWidget
from .stocks import StocksWidget
from .tvShow import TVShowsWidget

#order the widgets appear on the screen
registry = [
    FortuneCookieWidget,
    JokeWidget,
    QuoteWidget,
    NewsWidget,
    WordOfDayWidget,
    WeatherWidget,
    StocksWidget,
    TVShowsWidget,
]