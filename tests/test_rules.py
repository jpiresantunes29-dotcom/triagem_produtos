import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from rules import classify_order


def approved(**kwargs):
    defaults = dict(
        amount=100,
        age=25,
        item_count=3,
        payment_approved="yes",
        premium_client="yes",
        address_confirmed="yes",
    )
    defaults.update(kwargs)
    return classify_order(**defaults)


# --- BLOCKED ---

def test_blocked_payment_not_approved():
    status, reason = approved(payment_approved="no")
    assert status == "BLOCKED"
    assert reason == "payment not approved"


def test_blocked_underage_client():
    status, reason = approved(age=17)
    assert status == "BLOCKED"
    assert reason == "underage client"


def test_blocked_address_not_confirmed():
    status, reason = approved(address_confirmed="no")
    assert status == "BLOCKED"
    assert reason == "address not confirmed"


def test_blocked_takes_priority_over_under_review():
    # payment not approved + high amount: should still be BLOCKED
    status, reason = approved(payment_approved="no", amount=2000)
    assert status == "BLOCKED"


# --- UNDER REVIEW ---

def test_under_review_high_amount():
    status, reason = approved(amount=1001)
    assert status == "UNDER REVIEW"
    assert reason == "order amount above 1000"


def test_under_review_exact_boundary_amount():
    # amount exactly 1000 should NOT trigger under review by this rule
    status, _ = approved(amount=1000)
    assert status == "APPROVED"


def test_under_review_high_item_count():
    status, reason = approved(item_count=10)
    assert status == "UNDER REVIEW"
    assert reason == "high item count"


def test_under_review_non_premium_above_500():
    status, reason = approved(premium_client="no", amount=501)
    assert status == "UNDER REVIEW"
    assert reason == "non-premium client with order above 500"


def test_under_review_premium_above_500_is_approved():
    # premium client with amount > 500 but <= 1000 should be APPROVED
    status, _ = approved(premium_client="yes", amount=800)
    assert status == "APPROVED"


# --- APPROVED ---

def test_approved_normal_order():
    status, reason = approved()
    assert status == "APPROVED"
    assert reason == "order within normal rules"


def test_approved_minimum_values():
    status, _ = approved(amount=0, age=18, item_count=1)
    assert status == "APPROVED"


def test_approved_non_premium_exactly_500():
    # non-premium with amount exactly 500: rule only triggers above 500
    status, _ = approved(premium_client="no", amount=500)
    assert status == "APPROVED"
