"""Adds Genre model

Revision ID: 506e55602564
Revises: d57c7a8f3edb
Create Date: 2025-05-07 14:38:37.165002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '506e55602564'
down_revision = 'd57c7a8f3edb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre')
    # ### end Alembic commands ###
