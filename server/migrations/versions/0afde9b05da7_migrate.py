"""’migrate’

Revision ID: 0afde9b05da7
Revises: 
Create Date: 2023-05-04 12:08:44.660129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0afde9b05da7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_doers')),
    sa.UniqueConstraint('username', name=op.f('uq_doers_username'))
    )
    op.create_table('what_youre_bringing',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('top', sa.String(), nullable=True),
    sa.Column('bottom', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_what_youre_bringing'))
    )
    op.create_table('our_recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doer_id', sa.Integer(), nullable=True),
    sa.Column('bringing_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bringing_id'], ['what_youre_bringing.id'], name=op.f('fk_our_recommendations_bringing_id_what_youre_bringing')),
    sa.ForeignKeyConstraint(['doer_id'], ['doers.id'], name=op.f('fk_our_recommendations_doer_id_doers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_our_recommendations'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('our_recommendations')
    op.drop_table('what_youre_bringing')
    op.drop_table('doers')
    # ### end Alembic commands ###
