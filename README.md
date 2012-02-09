Safari Reading List Recipe
==========================

Safari is Apple's browser for Mac OS X. The current version includes a feature called [Reading List](http://www.apple.com/safari/features.html#browsing) which "lets you save web pages to read or browse later." It is essentially a special set of bookmarks representing a queue of articles you intend to read. Via iCloud, your Reading List can optionally be synced across multiple computers and iOS devices.

[Calibre](http://www.calibre-ebook.com/) is a free and open source ebook library management application. It features an extensible system "for downloading news from the Internet and converting it into an ebook." The scripts Calibre uses to retrieve and format news are known as [recipes](http://manual.calibre-ebook.com/news.html). Custom recipes can be written using Calibre's Python [recipe API](http://manual.calibre-ebook.com/news_recipe.html).

This recipe generates an ebook from the Unread items in your Reading List.

Requirements
------------

This recipe will only work on Mac OS X, for the reason that it loads its list of articles from Safari's bookmarks file (`~/Library/Safari/Bookmarks.plist`) with the help of [`plutil`](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/plutil.1.html). It was developed with Safari 5.1.3 on Mac OS X 10.7.3.

Limitations
-----------

- **Reading List items are not removed or marked as read.** In other words, articles will remain in your Reading List until you manually remove them. (This recipe does not edit or modify your bookmarks file.)
- Since your Reading List may point to articles on any site, there is no way to anticipate exactly what content to extract. This recipe therefore relies on Calibre's `auto_cleanup` function, which is derived from [Readability](https://code.google.com/p/arc90labs-readability/). It works pretty OK.
- Sometimes Safari cannot determine the article title and will just provide the name of the site. This is reflected in the recipe output.
- Minimal testing has been performed. 
- No error checking is performed.

Installation
------------

In Calibre, select *Add a custom news source* from the *Fetch news* toolbar button or menu. Click *Load recipe from file* and select the [`SafariReadingList.recipe`](https://github.com/anoved/Safari-Reading-List-Recipe/blob/master/SafariReadingList.recipe) file downloaded from this repository.

Use
---

To add items to your Reading List in Safari, select *Add to Reading List* from the *Bookmarks* menu. To view and manage your reading list, select *Show Reading List* from Safari's *View* menu. Alternatively, click the *Reading List* button in Safari's toolbar.

To run this recipe and create an ebook from your Unread Reading List items, go to Calibre and select *Schedule news download* from the *Fetch news* toolbar button or menu. Locate the *Safari Reading List* recipe and click *Download now*. Alternatively, set a schedule for Calibre to automatically update your *Safari Reading List* ebook.

Remember that this recipe does not remove items from your Reading List, so you'll have to do so yourself. The oldest unread item in your Reading List appears first in the output ebook.
