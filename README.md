# GeoBox

GeoBox is a Python-based tool designed to provide data recovery and system restore functionalities for Windows systems. The tool aims to prevent data loss by enabling users to create backups and restore their systems from predefined restore points.

## Features

- Create backups of specified directories.
- List available restore points.
- Restore systems from a selected restore point.
- Schedule regular backups at defined intervals.

## Installation

GeoBox requires Python 3.x to be installed on your system. Clone or download the repository to get started.

```bash
git clone https://github.com/yourusername/geobox.git
cd geobox
```

## Usage

Run the `GeoBox.py` script with various options to perform different tasks:

### Create a Backup

```bash
python GeoBox.py --backup "C:\\Path\\To\\SourceDirectory"
```

### List Restore Points

```bash
python GeoBox.py --list
```

### Restore from a Restore Point

```bash
python GeoBox.py --restore <restore_point_index> --target "C:\\Path\\To\\TargetDirectory"
```

### Schedule Regular Backups

```bash
python GeoBox.py --schedule <interval_minutes> --backup "C:\\Path\\To\\SourceDirectory"
```

## Notes

- Ensure you have the necessary permissions to access and modify the directories specified in the commands.
- Scheduled tasks are created using Windows Task Scheduler and require administrative privileges.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or fixes.

## License

GeoBox is released under the MIT License. See `LICENSE` for more information.