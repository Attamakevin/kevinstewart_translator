"""posts table

Revision ID: 9efcdd4a7783
Revises: ecda427ffd59
Create Date: 2023-09-09 20:53:25.724539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9efcdd4a7783'
down_revision = 'ecda427ffd59'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translated_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('translated_text', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_translated_text_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('translated_text', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_translated_text_timestamp'))

    op.drop_table('translated_text')
    # ### end Alembic commands ###
