"""''

Revision ID: 6498dfc09a28
Revises: d00392c4815c
Create Date: 2019-12-27 22:56:15.631212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6498dfc09a28'
down_revision = 'd00392c4815c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('book_name', sa.String(length=32), nullable=False),
    sa.Column('book_url', sa.String(length=100), nullable=False),
    sa.Column('book_describe', sa.Text(), nullable=True),
    sa.Column('book_fire', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('book_url')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=32), nullable=False),
    sa.Column('user_telephone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_telephone')
    )
    op.create_table('user_and_book',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_and_book')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
