"""empty message

Revision ID: 3b872dc7d648
Revises: 97a829445f98
Create Date: 2022-02-10 09:38:49.684683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b872dc7d648'
down_revision = '97a829445f98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('poke_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('ability', sa.String(length=50), nullable=True),
    sa.Column('base_experience', sa.Integer(), nullable=True),
    sa.Column('stat_name1', sa.String(length=50), nullable=True),
    sa.Column('stat_rating1', sa.Integer(), nullable=True),
    sa.Column('stat_name2', sa.String(length=50), nullable=True),
    sa.Column('stat_rating2', sa.Integer(), nullable=True),
    sa.Column('stat_name3', sa.String(length=50), nullable=True),
    sa.Column('stat_rating3', sa.Integer(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('poke_id')
    )
    op.create_table('user_join_pokemon',
    sa.Column('poke_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['poke_id'], ['pokemon.poke_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('poke_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_join_pokemon')
    op.drop_table('pokemon')
    # ### end Alembic commands ###