#!/usr/bin/env python
# ===========================================================================
# eXe
# Copyright 2004-2006 University of Auckland
# Copyright 2004-2008 eXe Project, http://eXeLearning.org/
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# ===========================================================================

"""
Version Information
"""

# Result initialization
project = "exe"
pkg_version = None

# Try to read the version from the version file
try:
    pkg_version = open('version').readline()
    release = pkg_version[0:-42]
except:
    # If it doesn't exist, we try to get it from debian/changelog
    try:
        line = open('debian/changelog').readline()
        release = line.split(':')[1].split(')')[0]
    except:
        # If the changelog doesn't exist either, we try to use pkg_resources to get the version
        try:
            import pkg_resources
            pkg_version = pkg_resources.require(project)[0].version
            release = pkg_version[0:-42]
        except:
            # If everything else fails, it may be Windows fault
            import sys
            if sys.platform[:3] == "win":
                #print sys.prefix
                pkg_version = "2.1.3-r8396514e5a0e1da4bc25d9b41db39ff96adff9fb"
                release = pkg_version[0:-42]
            else:
                # Or we try to get it from Resources
                pkg_version = open('../Resources/exe/version').readline()
                release = pkg_version[0:-42]

# Try to get the Git information
try:
    import git

    repo = git.Repo()
    revision = repo.head.commit.hexsha
except:
    # If there isn't a Git repo, we try to get the revision from
    # the version file (if it exists)
    revision = pkg_version[-40:] if pkg_version else ''

# Compose version string
version = release + "-r" + revision if revision else release

# If this file is executed directly, we print the project and version info
if __name__ == '__main__':
    print project, version
