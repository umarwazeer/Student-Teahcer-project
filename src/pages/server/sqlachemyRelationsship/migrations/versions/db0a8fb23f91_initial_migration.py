"""Initial migration

Revision ID: db0a8fb23f91
Revises: 0652af615e99
Create Date: 2023-06-01 02:42:16.810269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db0a8fb23f91'
down_revision = '0652af615e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emp_name', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('emp_id', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('emp_age', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('emp_email', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('emp_image', sa.String(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('name')
        batch_op.drop_column('department_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('department_id', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=100), nullable=False))
        batch_op.create_foreign_key(None, 'department', ['department_id'], ['id'])
        batch_op.drop_column('emp_image')
        batch_op.drop_column('emp_email')
        batch_op.drop_column('emp_age')
        batch_op.drop_column('emp_id')
        batch_op.drop_column('emp_name')

    op.create_table('department',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
