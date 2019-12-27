"""''

Revision ID: ba2739bc9958
Revises: 6e11a5792fad
Create Date: 2019-12-27 23:06:52.868322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba2739bc9958'
down_revision = '6e11a5792fad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('book_author', sa.String(length=32), nullable=True))
    op.add_column('book', sa.Column('book_image_url', sa.String(length=100), nullable=False))
    op.create_unique_constraint(None, 'book', ['book_image_url'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='unique')
    op.drop_column('book', 'book_image_url')
    op.drop_column('book', 'book_author')
    # ### end Alembic commands ###