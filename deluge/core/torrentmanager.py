#! /usr/bin/env python

# Object definitions copy/pasted from deluge/core/torrentmanager.py in the
# Deluge v1.3.15 source tree.

class TorrentState:
    def __init__(self,
            torrent_id=None,
            filename=None,
            total_uploaded=0,
            trackers=None,
            compact=False,
            paused=False,
            save_path=None,
            max_connections=-1,
            max_upload_slots=-1,
            max_upload_speed=-1.0,
            max_download_speed=-1.0,
            prioritize_first_last=False,
            file_priorities=None,
            queue=None,
            auto_managed=True,
            is_finished=False,
            stop_ratio=2.00,
            stop_at_ratio=False,
            remove_at_ratio=False,
            move_completed=False,
            move_completed_path=None,
            magnet=None,
            time_added=-1
        ):
        self.torrent_id = torrent_id
        self.filename = filename
        self.total_uploaded = total_uploaded
        self.trackers = trackers
        self.queue = queue
        self.is_finished = is_finished
        self.magnet = magnet
        self.time_added = time_added

        # Options
        self.compact = compact
        self.paused = paused
        self.save_path = save_path
        self.max_connections = max_connections
        self.max_upload_slots = max_upload_slots
        self.max_upload_speed = max_upload_speed
        self.max_download_speed = max_download_speed
        self.prioritize_first_last = prioritize_first_last
        self.file_priorities = file_priorities
        self.auto_managed = auto_managed
        self.stop_ratio = stop_ratio
        self.stop_at_ratio = stop_at_ratio
        self.remove_at_ratio = remove_at_ratio
        self.move_completed = move_completed
        self.move_completed_path = move_completed_path

    def __eq__(self, other):
        return isinstance(other, TorrentState) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

class TorrentManagerState:
    def __init__(self):
        self.torrents = []

    def __eq__(self, other):
        return isinstance(other, TorrentManagerState) and self.torrents == other.torrents

    def __ne__(self, other):
        return not self == other
