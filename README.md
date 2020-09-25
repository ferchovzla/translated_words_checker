# translated_words_checker
Check if there are words on the site that have not been translated.

You need install the next Python libraries:
 * BeautifulSoup
 * requests
 * pyenchant

The script checks if there are words that are not translated into the default language of the web page. We check against the system dictionary (hunspell, myspell).

To install a specific language, it must be done with apt-get install. Example apt-get install hunspell-it myspell-es myspell-nl (In this example Italian, Spanish and Dutch are installed respectively)
