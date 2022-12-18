Python iTunes
=============

A simple python wrapper to access iTunes Store API http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html

Installation
------------

Pypi package available at http://pypi.python.org/pypi/python-itunes/1.0

..  code-block:: bash

  $ easy_install python-itunes

Or download the code from https://github.com/ocelma/python-itunes/archives/master and then

..  code-block:: bash

  $ python setup.py install

.. note::

  If you're using python version <= 2.5 you'll need to install simplejson. E.g:

..  code-block:: bash

  $ easy_install simplejson


Examples
--------

Search
~~~~~~
..  code-block:: python

  import itunes
  
  # Search band U2
  artist = itunes.search_artist('u2')[0]
  for album in artist.get_albums():
      for track in album.get_tracks():
          print album.get_name(), album.get_url(), track.get_name(), track.get_duration(), track.get_preview_url()

  # Search U2 videos
  videos = itunes.search(query='u2', media='musicVideo')
  for video in videos:
      print video.get_name(), video.get_preview_url(), video.get_artwork()

  # Search Volta album by Björk
  album = itunes.search_album('Volta Björk')[0]

  # Global Search 'Beatles'
  items = itunes.search(query='beatles')
  for item in items: 
      print '[' + item.type + ']', item.get_artist(), item.get_name(), item.get_url(), item.get_release_date()

  # Search 'Angry Birds' game
  item = itunes.search(query='angry birds', media='software')[0]
  item.get_version()
  item.get_price()
  item.get_url()
  item.get_seller_url()
  item.get_screenshots()
  item.get_languages()
  item.get_avg_rating()
  item.get_num_ratings()

Lookup
~~~~~~

..  code-block:: python

  import itunes

  # Lookup Achtung Baby album by U2
  U2_ACHTUNGBABY_ID = 475390461
  album = itunes.lookup(U2_ACHTUNGBABY_ID)
  
  print album.get_url()
  print album.get_artwork()
  
  artist = album.get_artist()
  tracks = album.get_tracks()
 
  # Lookup song One from Achtung Baby album by U2
  U2_ONE_ID = 475391315
  track = itunes.lookup(U2_ONE_ID)

  artist = track.get_artist()
  album = track.get_album()

Caching JSON results
~~~~~~~~~~~~~~~~~~~~

..  code-block:: python

  import itunes

  if not itunes.is_caching_enabled():
      itunes.enable_caching('/tmp/itunes_cache') #If no param given it creates a folder in /tmp

  #From now on all JSON results are cached here:
  print itunes.__cache_dir

Tests
-----

..  code-block:: bash

  $ nosetests tests
