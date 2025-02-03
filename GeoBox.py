import os
import shutil
import subprocess
import datetime

class GeoBox:
    def __init__(self, backup_dir='C:\\GeoBoxBackups', restore_points=None):
        self.backup_dir = backup_dir
        self.restore_points = restore_points if restore_points else []

    def create_backup(self, source_dir):
        """Creates a backup of the specified directory."""
        try:
            now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            backup_path = os.path.join(self.backup_dir, f"backup_{now}")
            shutil.copytree(source_dir, backup_path)
            self.restore_points.append(backup_path)
            print(f"Backup created at {backup_path}")
        except Exception as e:
            print(f"Failed to create backup: {e}")

    def list_restore_points(self):
        """Lists all available restore points."""
        print("Available Restore Points:")
        for idx, point in enumerate(self.restore_points):
            print(f"{idx + 1}: {point}")

    def restore_backup(self, restore_point_index, target_dir):
        """Restores a backup to the specified directory."""
        try:
            restore_point = self.restore_points[restore_point_index - 1]
            if os.path.exists(target_dir):
                shutil.rmtree(target_dir)
            shutil.copytree(restore_point, target_dir)
            print(f"System restored from {restore_point} to {target_dir}")
        except IndexError:
            print("Invalid restore point index.")
        except Exception as e:
            print(f"Failed to restore backup: {e}")

    def schedule_backup(self, source_dir, interval_minutes):
        """Schedules a backup at regular intervals."""
        try:
            subprocess.run([
                'schtasks', '/create',
                '/sc', 'minute',
                '/mo', str(interval_minutes),
                '/tn', 'GeoBoxBackup',
                '/tr', f'python {__file__} --backup {source_dir}'
            ])
            print(f"Scheduled backup every {interval_minutes} minutes.")
        except Exception as e:
            print(f"Failed to schedule backup: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="GeoBox: Data Recovery and System Restore Tool")
    parser.add_argument('--backup', help='Create a backup of the specified directory')
    parser.add_argument('--restore', type=int, help='Restore the system from the specified restore point index')
    parser.add_argument('--list', action='store_true', help='List all available restore points')
    parser.add_argument('--target', help='Target directory for restoration')
    parser.add_argument('--schedule', type=int, help='Schedule backups at regular intervals in minutes')
    args = parser.parse_args()

    geobox = GeoBox()

    if args.backup:
        geobox.create_backup(args.backup)
    if args.list:
        geobox.list_restore_points()
    if args.restore and args.target:
        geobox.restore_backup(args.restore, args.target)
    if args.schedule and args.backup:
        geobox.schedule_backup(args.backup, args.schedule)