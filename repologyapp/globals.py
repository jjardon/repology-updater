#!/usr/bin/env python3
#
# Copyright (C) 2016-2017 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import flask

from repology.config import config
from repology.database import Database
from repology.repoman import RepositoryManager


__all__ = [
    'get_db',
    'repometadata',
    'reponames'
]


repoman = RepositoryManager(config['REPOS_DIR'], 'dummy')
repometadata = repoman.GetMetadata(config['REPOSITORIES'])
reponames = repoman.GetNames(config['REPOSITORIES'])


def get_db():
    # XXX: this is not really a persistent DB connection!
    if not hasattr(flask.g, 'database'):
        flask.g.database = Database(config['DSN'], readonly=False, autocommit=True)
    return flask.g.database
