"""empty message

Revision ID: 937930df2d1c
Revises: 763b320cb678
Create Date: 2021-12-04 23:18:10.421842

"""
from alembic import op
import sqlalchemy as sa


from api.flashcards.models import Deck

# revision identifiers, used by Alembic.
revision = '937930df2d1c'
down_revision = '763b320cb678'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO decks (name) values ('Default')")
    op.add_column('flashcards', sa.Column('deck_id', sa.Integer(), nullable=False, server_default='1'))
    op.create_foreign_key(None, 'flashcards', 'decks', ['deck_id'], ['id'])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'flashcards', type_='foreignkey')
    op.drop_column('flashcards', 'deck_id')
    # ### end Alembic commands ###
