.. This document is written
   using Semantic Linefeeds.
   See http://rhodesmill.org/brandon/2012/one-sentence-per-line/
   for an explanation
   of why linebreaks are
   the way they are.)

====================
Deluge Split-o-Matic
====================

Introduction
============

This is a tool
for splitting the state file
from a large Deluge instance
(``torrents.state``)
into multiple smaller ones.
I wanted to do this
because I was using a single Deluge instance
to manage over 3,500 torrents,
and performance of everything except downloading was atrocious
(slow restarts,
slow UI,
slow to start new torrents,
rechecks would often take tens of seconds to start,
etc.).

The state definition is expected to match Deluge v1.3.15.
I don't think this changes very often, however,
so the script should be fairly forwards/backwards compatible.

Running
==========

The `torrents.state` file
is just a `pickle`_ dump.
However, because Deluge targets Python 2,
and because pickle's storage format changed dramatically
between Python 2 and 3,
this script also targets Python 2(.7).
Sorry.
(That's also why the project isn't structured properly,
and why there's no ``setup.py``:
I didn't want to take the time
to learn how to do those thing properly
for Python 2.)

.. code-block:: shell

    $ git clone https://github.com/MrDOS/deluge-split
    $ pip install bencode.py
    $ cd deluge-split
    $ # Define what new instance states should be created.
    $ cp instances-example.json instances.json && $EDITOR instances.json
    $ python split.py \
             /path/to/input/deluge/state/torrents.state \
             /path/to/input/deluge/state/torrents.fastresume \
             instances.json

For each instance defined
in ``instances.json``,
an ``ids`` file will be created
containing the IDs of the torrents in the instance,
a ``state`` file will be created
reflecting the state of those torrents,
and a ``fastresume`` file will be created
reflecting historic seeding activity for those torrents.

.. _pickle: https://docs.python.org/2/library/pickle.html

Configuring
===========

Each instance defined
in the ``instances.json`` configuration file
must have a ``name``
and an array of patterns for the ``trackers``
with which that instance is concerned.

Match priority
(for when a single torrent has multiple trackers)
is the order in which instances are given
(that is, the first instance to match gets the torrent).
It's probably useful to have
a catch-all instance at the end of the list
so that nothing gets missed,
and you wouldn't want to have your catch-all at the beginning
lest all of your torrents be added to that instance.

Now with merging!
=================

If you've sliced and diced to your heart's content
and then gave your brain time to catch up
and ask what the hell you were doing,
you'll be elated to learn
that this project now offers a solution
for merging Deluge instances:

.. code-block:: shell

    $ python merge.py \
             /path/to/output/torrents.state \
             /path/to/output/torrents.fastresume \
             /path/to/first/input/torrents.state \
             /path/to/first/input/torrents.fastresume \
             /path/to/second/input/torrents.state \
             /path/to/second/input/torrents.fastresume \
             /path/to/nth/input/torrents.state \
             /path/to/nth/input/torrents.fastresume

License
=======

Normally I slap the WTFPL
on throwaway projects like this.
However, because ``deluge/core/torrentmanager.py``
contains class definitions lifted directly
from the Deluge source,
I feel obliged to license this project
under the terms of the GNU General Public License Version 3 (GPLv3).
