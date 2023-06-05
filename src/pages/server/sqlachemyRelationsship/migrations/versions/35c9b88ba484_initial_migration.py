"""Initial migration

Revision ID: 35c9b88ba484
Revises: 2e1409363b2e
Create Date: 2023-06-01 17:01:40.862017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35c9b88ba484'
down_revision = '2e1409363b2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path', sa.String(length=200), nullable=True))
        batch_op.alter_column('emp_name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('emp_id',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=10),
               existing_nullable=True)
        batch_op.alter_column('emp_email',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.create_unique_constraint(None, ['emp_id'])
        batch_op.drop_column('emp_image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emp_image', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('emp_email',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('emp_id',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('emp_name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.drop_column('image_path')

    # ### end Alembic commands ###
