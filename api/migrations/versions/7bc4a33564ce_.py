"""empty message

Revision ID: 7bc4a33564ce
Revises: 
Create Date: 2018-06-08 12:36:23.108869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bc4a33564ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('photoURL', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Badges',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=100), nullable=False),
    sa.Column('csv', sa.String(length=100), nullable=False),
    sa.Column('text_color', sa.String(length=100), nullable=False),
    sa.Column('badge_size', sa.String(length=100), nullable=False),
    sa.Column('download_link', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('File',
    sa.Column('id', sa.String(length=100), nullable=True),
    sa.Column('filename', sa.String(length=100), nullable=False),
    sa.Column('filetype', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('filename')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('File')
    op.drop_table('Badges')
    op.drop_table('User')
    # ### end Alembic commands ###