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
    $ cd lxdnap
    $ make install

Add a cronjob to run snap.py once an hour.

Remember the user running the job must belong to the lxd group.
