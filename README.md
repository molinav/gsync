# Gsync - RSync for Google Drive

[![Build Status](
    https://travis-ci.org/molinav/gsync.svg?branch=master)
](
    https://travis-ci.org/github/molinav/gsync/builds
)
[![Feature Requests](
    https://img.shields.io/github/issues/molinav/gsync/feature-request.svg)
](
    https://github.com/molinav/gsync/issues?q=is%3Aopen+is%3Aissue+label%3Afeature-request
)
[![Bugs](
    https://img.shields.io/github/issues/molinav/gsync/bug.svg)
](
    https://github.com/molinav/gsync/issues?utf8=✓&q=is%3Aissue+is%3Aopen+label%3Abug
)

Copyright (C) 2013-2014 Craig Phillips. All rights reserved.

Google currently don't produce a Linux variant of their client for Google
Drive. This is my implementation of a multiplatform, command line tool that
for the most part, is intended to behave much like `rsync`. I aim to follow
the same functional implementation of `rsync` and also provide the same
features, enabled or disabled through a similar interface of command line
options.

There was a close contender for being a suitable client called `grive`. This is
ideal if you only intend to sync a small library of files or if the files being
synchronised are small in size. I found the client to be unreliable in other
cases, crashing and failing to synchronise very little. I looked over much of
the code and found that it favours preloading with a hash of the directory to
be synchronised and all sub directories, before it even synchronises any files.
This creates a scenario where synchronisation will never take place if the
preloading fails. Instead, I will opt to process directories depth first and
sequentially in order to allow synchronisation to occur immediately.

The only prerequisite is that you have Python. The `makefile` will take care of
installing any required Python libraries using `pip`, which will also be
obtained.

## Donations:

If you like the software, don't forget to donate to further development of it!

https://github.com/iwonbigbro/gsync/wiki/Donate

## My Blog:

http://mud-slide.blogspot.co.uk/

## Installation:

The GSync package is now available on (pypi.python.org). It can be installed
using `pip`. I recommend using `pip` over `easy_install` or `pypi-install`,
since `pip` takes care of dependencies through `setuptools`. I have found that
`easy_install` only checks for dependencies but doesn't actually install them.
On Debian I installed using the following steps:
```sh
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install gsync
```

To upgrade GSync, you can run `pip` with the `--upgrade` option:
```sh
sudo pip install --upgrade gsync
```

That's it. GSync will be installed along with any required packages.

## Authentication:

Authentication occurs just once, the first time a connection is established
with your drive. To establish a connection, just specify the `--authenticate`
option with no other options or arguments:
```sh
gsync --authenticate
```

Or alternatively, just specify a drive source or destination file like:
```sh
gsync drive://somepath/in/your/drive ~/some/local/path
```

It will provide a URL for which you can obtain a GUID from Google that you
paste into the command line prompt. Once authenticated, it caches the GUID in
your `~/.gsync` directory. To force authentication, just remove this directory.

See: https://developers.google.com/accounts/docs/OAuth2

## RSync options implemented so far:

```
 -v, --verbose               enable verbose output
     --debug                 enable debug output
 -q, --quiet                 suppress non-error messages
 -c, --checksum              skip based on checksum, not mod-time & size
 -r, --recursive             recurse into directories
 -R, --relative              use relative path names
 -u, --update                skip files that are newer on the receiver
 -d, --dirs                  transfer directories without recursing
 -g, --group                 preserve group
 -o, --owner                 preserve owner (super-user only)
 -p, --perms                 preserve permissions
 -i, --itemize-changes       output a change-summary for all updates
     --progress              show progress during transfer
```

## For a list of known issues:

https://github.com/iwonbigbro/gsync/issues?state=open
