# Copyright 2014 OpenStack Foundation
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

"""set_length_of_description_field_metering

Revision ID: 33c3db036fe4
Revises: b65aa907aec
Create Date: 2014-03-25 11:04:27.341830

"""

# revision identifiers, used by Alembic.
revision = '33c3db036fe4'
down_revision = 'b65aa907aec'

# Change to ['*'] if this migration applies to all plugins

migration_for_plugins = [
    'neutron.services.metering.metering_plugin.MeteringPlugin'
]

from alembic import op
import sqlalchemy as sa

from neutron.db import migration


def upgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    op.alter_column('meteringlabels', 'description', type_=sa.String(1024),
                    existing_nullable=True)


def downgrade(active_plugins=None, options=None):
    if not migration.should_run(active_plugins, migration_for_plugins):
        return

    pass
