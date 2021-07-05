"""remove ayah field.

Revision ID: 6d0e03004042
Revises: 6f706df0e865
Create Date: 2021-06-29 22:53:52.719028

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6d0e03004042'
down_revision = '6f706df0e865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('quran_ayah_text', 'ayah')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quran_ayah_text', sa.Column('ayah', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    # ### end Alembic commands ###