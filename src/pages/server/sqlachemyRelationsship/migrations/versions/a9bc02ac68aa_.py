"""empty message

Revision ID: a9bc02ac68aa
Revises: db0a8fb23f91
Create Date: 2023-06-01 11:13:57.116087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9bc02ac68aa'
down_revision = 'db0a8fb23f91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emp_name', sa.String(length=255), nullable=True),
    sa.Column('emp_id', sa.String(length=255), nullable=True),
    sa.Column('emp_age', sa.Integer(), nullable=True),
    sa.Column('emp_email', sa.String(length=255), nullable=True),
    sa.Column('emp_image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    # ### end Alembic commands ###
