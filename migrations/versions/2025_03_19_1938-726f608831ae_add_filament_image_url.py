"""add filament image url.

Revision ID: 726f608831ae
Revises: 415a8f855e14
Create Date: 2025-03-19 19:38:51.261233
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '726f608831ae'
down_revision = '415a8f855e14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Perform the upgrade."""
    op.add_column('filament', sa.Column(
        'picture_url', sa.String(length=256), nullable=True))


def downgrade() -> None:
    """Perform the downgrade."""
    op.drop_column('filament', 'picture_url')
