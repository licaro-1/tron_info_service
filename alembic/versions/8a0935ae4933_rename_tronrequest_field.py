"""Rename TronRequest field

Revision ID: 8a0935ae4933
Revises: 8625643087bb
Create Date: 2025-03-28 19:29:53.766421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a0935ae4933'
down_revision: Union[str, None] = '8625643087bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tron_request', sa.Column('requested_at', sa.DateTime(), nullable=False))
    op.drop_column('tron_request', 'request_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tron_request', sa.Column('request_at', sa.DATETIME(), nullable=False))
    op.drop_column('tron_request', 'requested_at')
    # ### end Alembic commands ###
