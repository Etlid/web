"""new fields in user model

Revision ID: 37f06a334dbf
Revises: 780739b227a7
Create Date: 2017-09-14 10:54:13.865401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37f06a334dbf'
down_revision = '780739b227a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    #op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('path', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('av_name', sa.String(length=140), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
upgrade()