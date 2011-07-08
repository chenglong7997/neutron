# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2011 Cisco Systems, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Sumit Naiksatam, Cisco Systems, Inc.
#

import MySQLdb
import logging as LOG
import sys
import traceback

from quantum.common import exceptions as exc
from quantum.plugins.cisco import cisco_configuration as conf
from quantum.plugins.cisco import cisco_constants as const
from quantum.plugins.cisco import cisco_credentials as cred

LOG.basicConfig(level=LOG.WARN)
LOG.getLogger(const.LOGGER_COMPONENT_NAME)


class DBUtils(object):

    def __init__(self):
        pass

    def _get_db_connection(self):
        db_ip = conf.DB_SERVER_IP
        db_username = cred.Store.getUsername(db_ip)
        db_password = cred.Store.getPassword(db_ip)
        self.db = MySQLdb.connect(db_ip, db_username, db_password,
                                  conf.DB_NAME)
        return self.db

    def execute_db_query(self, sql_query):
        db = self._get_db_connection()
        cursor = db.cursor()
        try:
            cursor.execute(sql_query)
            results = cursor.fetchall()
            db.commit()
            LOG.debug("DB query execution succeeded: %s" % sql_query)
        except:
            db.rollback()
            LOG.debug("DB query execution failed: %s" % sql_query)
            traceback.print_exc()
            db.close()
