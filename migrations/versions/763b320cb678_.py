"""empty message

Revision ID: 763b320cb678
Revises: 
Create Date: 2021-12-04 23:15:50.471194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '763b320cb678'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('decks')
    # ### end Alembic commands ###