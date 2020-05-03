# Changelog

All notable changes to this project will be documented in this file. The format
is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and the
project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

### Fixed
- Fix handling of `SyncFileInfoDatetime` and `int` by `Drive.unicode`
- Bug [#12]: `TypeError` when `gsync` uploads a file on Python3
- Bug [#14]: `TypeError` when `gsync` downloads a file on Python3

## [0.2.0] - 2020-05-03

### Added
- Include `six` as a library dependency
- Include the protocol used by `pickle` explicitly

### Changed
- Replace problematic Python2 syntax (e.g. `__metaclass__`, `raw_input`,
  `basestring`, `unicode`, `str`, `iteritems`) with equivalent expressions
  that use `six`
- Modify handling of streams (`str`, `bytes`) for future compatibility
  with Python3

### Fixed
- Bug [#1]: Remove `basestring` from code
- Bug [#6]: `GsyncOptions` throws `AttributeError` in Python3
- Bug [#9]: Cannot `gsync` with Python2 if `gsync` was used with Python3

### Removed
- `libgsync.hashlib` subpackage
- `simplejson` support

## [0.1.16] - 2020-05-01

### Changed
- Upgrade `CHANGELIST.rst` into `CHANGELOG.md` and use Markdown
- Upgrade `README.rst` into `README.md` and use Markdown
- Update `.pylint` configuration file to use the last up-to-date template
- Refactor all the code in the library to make the port to Python3 easier

## [0.1.15] - 2020-03-14

### Fixed
- Fix inconsistent versions of library dependencies
- Fix issue with local storage of credentials

## [0.1.14] - 2013-10-23

### Added
- Feature [##33]: Option to change the default dir config files (`.gsync` and
  `client.json`) 

## [0.1.13] - 2013-10-21

### Fixed
- Bug [##32]: `MemoryError()` with the checksum option with large files

## [0.1.10] - 2013-10-19

### Added
- Add new filter module for future implementation of `rsync` filters

### Fixed
- Bug [##31]: Files being reported out of date when they are not

## [0.1.9] - 2013-10-17

### Added
- Some improvements to `README` documentation
- Better dependency specifications in `setup.py`

## [0.1.8] - 2013-10-16

### Fixed
- Bug [##25]: Transfer Stats
- Bug [##26]: Error: `TypeError('a float is required',)`

## [0.1.7] - 2013-10-16

### Fixed
- Bug [##29]: `OSError('No such file or directory: h')`

## [0.1.6] - 2013-10-16

### Fixed
- Bug [##27]: Error: `TypeError('a float is required',)`
- Bug [##28]: Command line arguments are not repeatable: e.g. `--filter`

## [0.1.5] - 2013-10-09

### Added
- Feature [##12]: Implement `--checksum` option

### Fixed
- Bug [##22]: Modification time is not being set to match the source
  file modification time when used with `--times` 

## [0.1.4] - 2013-10-04

### Changed
- `setuptools` used in place of `distutils`, meaning easier installation

### Fixed
- Bug [##19]: Latin-1 file names are not supported and throw exceptions

## [0.1.3] - 2013-10-01

### Fixed
- Bug [##17] and [##18]: Does not obey `--recursive` option anymore
- Bug [##16]: Error: `__init__() takes at least 5 arguments (4 given)`

## [0.1.2] - 2013-10-01

### Fixed
- Bug [##15]: Specifying source and/or destination files results in creation
  of directories where there should be files, on the client or server

## [0.1.1] - 2013-09-30

### Fixed
- Bug [##13]: Specifying a file to copy instead of a directory does nothing
- Bug [##14]: Attempted install on a 'Python Fresh' machine

## [0.1.0] - 2013-09-01

### Changed
- Traversal of the Google Drive is now more reliable and requires less CPU
  and network requests
- Intermediate directory creation now occurs through a restructure of the
  directory walking code, ensuring directories are provided to the callback
- Itemized output now occurs without needing to specify the `verbose` option
- Interrupt handling now works, so `Ctrl-C` will halt the sync and output the
  progress (bytes sent/received) up to the interrupt
- Implemented `--progress` functionality so that upload progress can be
  monitored

### Fixed
- Bug: Syncs one file and crashes with division by zero error
- Bug: Always: Error:
  `String or Integer object expected for key, unicode found`
- Bug: Files get updated that are in Trash and do not get restored


[0.2.0]:
https://github.com/molinav/gsync/compare/v0.1.16...v0.2.0
[0.1.16]:
https://github.com/molinav/gsync/compare/v0.1.15...v0.1.16
[0.1.15]:
https://github.com/molinav/gsync/compare/759d7dc9...v0.1.15
[0.1.14]:
https://github.com/iwonbigbro/gsync/compare/01625671...759d7dc9
[0.1.13]:
https://github.com/iwonbigbro/gsync/compare/c7bec5ac...01625671
[0.1.10]:
https://github.com/iwonbigbro/gsync/compare/f38abf44...c7bec5ac
[0.1.9]:
https://github.com/iwonbigbro/gsync/compare/fe37e4fd...f38abf44
[0.1.8]:
https://github.com/iwonbigbro/gsync/compare/b11e2f8a...fe37e4fd
[0.1.7]:
https://github.com/iwonbigbro/gsync/compare/ada55a5c...b11e2f8a
[0.1.6]:
https://github.com/iwonbigbro/gsync/compare/5575a3ff...ada55a5c
[0.1.5]:
https://github.com/iwonbigbro/gsync/compare/2f2ce186...5575a3ff
[0.1.4]:
https://github.com/iwonbigbro/gsync/compare/8aee2d8b...2f2ce186
[0.1.3]:
https://github.com/iwonbigbro/gsync/compare/236bb255...8aee2d8b
[0.1.2]:
https://github.com/iwonbigbro/gsync/compare/50dea079...236bb255
[0.1.1]:
https://github.com/iwonbigbro/gsync/compare/5abf8886...50dea079
[0.1.0]:
https://github.com/iwonbigbro/gsync/commit/5abf8886


[#12]:
https://github.com/molinav/gsync/issues/12
[#9]:
https://github.com/molinav/gsync/issues/9
[#6]:
https://github.com/molinav/gsync/issues/6
[#1]:
https://github.com/molinav/gsync/issues/1
[##33]:
https://github.com/iwonbigbro/gsync/issues/33
[##32]:
https://github.com/iwonbigbro/gsync/issues/32
[##31]:
https://github.com/iwonbigbro/gsync/issues/31
[##29]:
https://github.com/iwonbigbro/gsync/issues/29
[##28]:
https://github.com/iwonbigbro/gsync/issues/28
[##27]:
https://github.com/iwonbigbro/gsync/issues/27
[##26]:
https://github.com/iwonbigbro/gsync/issues/26
[##25]:
https://github.com/iwonbigbro/gsync/issues/25
[##22]:
https://github.com/iwonbigbro/gsync/issues/22
[##19]:
https://github.com/iwonbigbro/gsync/issues/19
[##18]:
https://github.com/iwonbigbro/gsync/issues/18
[##17]:
https://github.com/iwonbigbro/gsync/issues/17
[##16]:
https://github.com/iwonbigbro/gsync/issues/16
[##15]:
https://github.com/iwonbigbro/gsync/issues/15
[##14]:
https://github.com/iwonbigbro/gsync/issues/14
[##13]:
https://github.com/iwonbigbro/gsync/issues/13
[##12]:
https://github.com/iwonbigbro/gsync/issues/12
