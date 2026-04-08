import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from reports import show_summary, show_highest_order, show_blocked, show_all_orders


def make_order(code="ORD-1", amount=100, status="APPROVED", reason="order within normal rules"):
    return {
        "code": code,
        "amount": amount,
        "age": 25,
        "item_count": 2,
        "payment_approved": "yes",
        "premium_client": "yes",
        "address_confirmed": "yes",
        "status": status,
        "reason": reason,
    }


# --- show_summary ---

def test_summary_counts_correctly(capsys):
    orders = [
        make_order(status="APPROVED"),
        make_order(status="APPROVED"),
        make_order(status="UNDER REVIEW"),
        make_order(status="BLOCKED"),
    ]
    show_summary(orders)
    output = capsys.readouterr().out
    assert "Approved: 2" in output
    assert "Under review: 1" in output
    assert "Blocked: 1" in output
    assert "Total orders processed: 4" in output


def test_summary_empty_list(capsys):
    show_summary([])
    output = capsys.readouterr().out
    assert "No orders registered." in output


# --- show_highest_order ---

def test_highest_order_returns_correct_one(capsys):
    orders = [
        make_order(code="ORD-1", amount=200),
        make_order(code="ORD-2", amount=999),
        make_order(code="ORD-3", amount=50),
    ]
    show_highest_order(orders)
    output = capsys.readouterr().out
    assert "ORD-2" in output
    assert "999" in output


def test_highest_order_empty_list(capsys):
    show_highest_order([])
    output = capsys.readouterr().out
    assert "No orders registered." in output


# --- show_blocked ---

def test_show_blocked_lists_only_blocked(capsys):
    orders = [
        make_order(code="ORD-1", status="APPROVED"),
        make_order(code="ORD-2", status="BLOCKED", reason="payment not approved"),
        make_order(code="ORD-3", status="UNDER REVIEW"),
    ]
    show_blocked(orders)
    output = capsys.readouterr().out
    assert "ORD-2" in output
    assert "ORD-1" not in output
    assert "ORD-3" not in output


def test_show_blocked_none_blocked(capsys):
    orders = [make_order(status="APPROVED")]
    show_blocked(orders)
    output = capsys.readouterr().out
    assert "No blocked orders." in output


def test_show_blocked_empty_list(capsys):
    show_blocked([])
    output = capsys.readouterr().out
    assert "No orders registered." in output


# --- show_all_orders ---

def test_show_all_orders_empty(capsys):
    show_all_orders([])
    output = capsys.readouterr().out
    assert "No orders registered." in output


def test_show_all_orders_displays_each(capsys):
    orders = [
        make_order(code="ORD-A", amount=100),
        make_order(code="ORD-B", amount=200),
    ]
    show_all_orders(orders)
    output = capsys.readouterr().out
    assert "ORD-A" in output
    assert "ORD-B" in output
