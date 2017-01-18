from datetime import datetime, timedelta
from pylxd import Client
from pylxd.exceptions import NotFound


if __name__ == '__main__':
    fmt = '%Y%m%d-%H'

    # List of snapshot names to keep (not to remove)
    now = datetime.now()
    today = now.date()
    last_sunday = today - timedelta(days=(today.weekday() + 1) % 7)
    keep = [now, today] #, last_sunday]
    keep = [x.strftime(fmt) for x in keep]

    # Name of the new snapshot to be created
    sname_new = keep[0]

    client = Client()
    for container in client.containers.all():
        cname = container.name

        # (1) Create new snapshot
        # There is not .snapshots.exists(name) like there is
        # .containers.exists(name)
        # TODO Open an issue
        try:
            # This line produces many warnings when successful
            # see https://github.com/lxc/pylxd/issues/217
            container.snapshots.get(sname_new)
        except NotFound:
            print('Create', cname, sname_new)
            container.snapshots.create(sname_new)

        # (2) Delete old snapshots
        for snapshot in container.snapshots.all():
            sname = snapshot.name
            # Do not remove explicitely created snapshots
            try:
                datetime.strptime(sname, fmt)
            except ValueError:
                continue

            if sname in keep:
                continue

            print('Delete', cname, sname)
            snapshot.delete()
