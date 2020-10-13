"""Added Event name and made phone number of donation venue non-unique

Revision ID: 16560cb60091
Revises: b399c6611153
Create Date: 2020-09-29 20:09:54.276244

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "16560cb60091"
down_revision = "b399c6611153"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("phone_number", table_name="donation_venue")
    op.add_column("event", sa.Column("name", sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("event", "name")
    op.create_index("phone_number", "donation_venue", ["phone_number"], unique=True)
    # ### end Alembic commands ###