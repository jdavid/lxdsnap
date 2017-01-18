# lxdsnap
Automatic LXD snapshotting

Creates an snapashot of every LXD container in the localhost, once an hour.
The name of the snapshot has the format YYYYMMDD-HH.

After the new snapshot has been created, old ones will be removed, except:

- Those with a different format (to preserve snapshots created by other means).
- The snapshot just created.
- The first snapshot of the current day: YYYYMMMDD-00

**DISCLAIMER** Provided as is. Use at your own risk.

Deploy:

    $ git clone https://github.com/jdavid/lxdsnap.git
    $ cd lxdsnap
    $ make install

Add a cronjob to run snap.py once an hour:

    $ crontab -e
    [...]
    # LXD Snapshots, once an hour
    30 * * * * /home/admin/lxdsnap/venv/bin/python /home/admin/lxdsnap/snap.py

Remember the user running the job must belong to the lxd group.
