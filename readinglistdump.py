#!/usr/bin/env python

#
# What does this script do?
#	It prints information about the Unread items in your Safari Reading List.
#	The oldest item is printed first (maybe). Each item is printed on its own
#	line. The line format is "Title", "Preview text", "URL", "bookmark date".
#
# What is the Safari Reading List?
#	A category of bookmarks introduced in Safari 5.1, intended to represent
#	articles you intend to read at a later time. It syncs with iOS Safari.
#

#
# This script uses Beautiful Soup 3.x for xml parsing.
# http://www.crummy.com/software/BeautifulSoup/
#
import BeautifulSoup
import os

#
# Reading List items are stored as Safari bookmarks.
# Safari bookmarks are stored as a binary property list file.
# plutil can convert binary property lists to xml format.
# The -o - option prints the output to stdout.
# We plug our pipe into that.
#
xml_pipe = os.popen('/usr/bin/plutil -convert xml1 -o - ~/Library/Safari/Bookmarks.plist', 'r')
xml_data = xml_pipe.read()
xml_pipe.close()

#
# BeautifulStoneSoup is a generic xml parser.
# We need to tell it a few things about property lists, or it'll get confused.
#
class PropertyListParser(BeautifulSoup.BeautifulStoneSoup):
	NESTABLE_TAGS = BeautifulSoup.buildTagMap([], ['array', 'dict'])
	SELF_CLOSING_TAGS = BeautifulSoup.buildTagMap(None, ['true', 'false'])

#
# Convert the Safari bookmarks data to tag soup.
# Find the array containing reading list items; that's all we need.
# Yank out extraneous newline strings (simplifies stepping from tag to tag).
#
soup = PropertyListParser(xml_data)
rlid = soup.find(text='com.apple.ReadingList').parent
rl_array = rlid.parent.find('array')
if None == rl_array:
	exit()

reading_list = rl_array.extract()
[newline.extract() for newline in reading_list.findAll(text='\n')]

#
# Loop through the list of reading list items, starting with the oldest item.
# Skip items that have been viewed - we only want "Unread" items.
#
reading_list_items = reading_list.contents
reading_list_items.reverse()
for reading_list_item in reading_list_items:
	if None != reading_list_item.find(text='DateLastViewed'):
		continue
	
	#
	# Find item info the easy way, by finding it.
	# Value tags follow the key label tags.
	#
	item_title = reading_list_item.find(text='title').parent.nextSibling.string
	item_preview = reading_list_item.find(text='PreviewText').parent.nextSibling.string
	item_url = reading_list_item.find(text='URLString').parent.nextSibling.string
	item_fetchdate = reading_list_item.find(text='DateLastFetched').parent.nextSibling.string
	print('"%s", "%s", "%s", "%s"' % (item_title, item_preview, item_url, item_fetchdate))
