"""empty message

Revision ID: fd9f1ef74840
Revises: 
Create Date: 2023-06-26 15:45:05.608739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd9f1ef74840'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('developers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('logo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('online', sa.Boolean(), nullable=False),
    sa.Column('number_of_players', sa.Integer(), nullable=False),
    sa.Column('release_year', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('developer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['developer_id'], ['developers.id'], name=op.f('fk_games_developer_id_developers')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('geedees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], name=op.f('fk_geedees_device_id_devices')),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_geedees_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('geedees')
    op.drop_table('games')
    op.drop_table('devices')
    op.drop_table('developers')
    # ### end Alembic commands ###
