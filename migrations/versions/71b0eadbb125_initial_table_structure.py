"""Initial Table structure

Revision ID: 71b0eadbb125
Revises:
Create Date: 2020-09-27 16:24:29.675690

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

# revision identifiers, used by Alembic.
revision = "71b0eadbb125"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "donation_venue",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column(
            "email", sqlalchemy_utils.types.email.EmailType(length=255), nullable=False
        ),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("phone_number", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("phone_number"),
    )
    op.create_table(
        "event",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("start", sa.DateTime(), nullable=False),
        sa.Column("end", sa.DateTime(), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("username", sa.String(length=20), nullable=False),
        sa.Column(
            "email", sqlalchemy_utils.types.email.EmailType(length=255), nullable=False
        ),
        sa.Column(
            "password",
            sqlalchemy_utils.types.password.PasswordType(max_length=1137),
            nullable=False,
        ),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.BigInteger(), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("phone_number"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "donor",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("covid_last_symptom_date", sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "volunteer",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("start_date_time", sa.DateTime(), nullable=False),
        sa.Column("end_date_time", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "donation_registration",
        sa.Column("donor_id", sa.Integer(), nullable=False),
        sa.Column("venue_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["donor_id"],
            ["donor.id"],
        ),
        sa.ForeignKeyConstraint(
            ["venue_id"],
            ["donation_venue.id"],
        ),
        sa.PrimaryKeyConstraint("donor_id", "venue_id"),
    )
    op.create_table(
        "event_registration",
        sa.Column("volunteer_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["event.id"],
        ),
        sa.ForeignKeyConstraint(
            ["volunteer_id"],
            ["volunteer.id"],
        ),
        sa.PrimaryKeyConstraint("volunteer_id", "event_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("event_registration")
    op.drop_table("donation_registration")
    op.drop_table("volunteer")
    op.drop_table("donor")
    op.drop_table("user")
    op.drop_table("event")
    op.drop_table("donation_venue")
    # ### end Alembic commands ###
