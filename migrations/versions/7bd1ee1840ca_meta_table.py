"""Meta Table

Revision ID: 7bd1ee1840ca
Revises: 9ca5901af374
Create Date: 2020-01-30 01:13:40.069188

"""
from alembic import op
import sqlalchemy as sa
import app.model_types


# revision identifiers, used by Alembic.
revision = '7bd1ee1840ca'
down_revision = '9ca5901af374'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meta',
    sa.Column('uuid', app.model_types.GUID(), nullable=False),
    sa.Column('user_id', app.model_types.GUID(), nullable=False),
    sa.Column('note_id', app.model_types.GUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('name_compare', sa.String(), nullable=True),
    sa.Column('kind', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['note.uuid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_meta_uuid'), 'meta', ['uuid'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_meta_uuid'), table_name='meta')
    op.drop_table('meta')
    # ### end Alembic commands ###