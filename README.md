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

## Issues

I had issues with the snapshots taking too much resources and sometimes
processes dying. This may be related to my stack, your mileage may vary.
So be careful.

My recommendations:

- Use latest version of LXD.

- Avoid making snapshots of containers with sub-volumes (e.g. docker inside
  lxd), or at least test carefully.

- Start with a low rate, like snapshot once a day when the load is low, and
  increase if you don't see load spikes.
