from flask import Blueprint, request, jsonify
from .models import db, Order, OrderItem

order_bp = Blueprint("order", __name__)


@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    customer_name = data.get("customer_name")
    items = data.get("items", [])

    if not customer_name or not items:
        return jsonify({"error": "Missing required fields"}), 400

    total_price = sum(item['price'] * item['quantity'] for item in items)

    order = Order(customer_name=customer_name, total_price=total_price)
    for item in items:
        order_item = OrderItem(
            game_id=item['game_id'],
            game_title=item['game_title'],
            quantity=item['quantity'],
            price=item['price']
        )
        order.items.append(order_item)

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order created successfully", "order_id": order.id}), 201


@order_bp.route("/orders", methods=["GET"])
def get_all_orders():
    orders = Order.query.all()
    result = []

    for order in orders:
        order_data = {
            "id": order.id,
            "customer_name": order.customer_name,
            "total_price": order.total_price,
            "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "items": [
                {
                    "game_id": item.game_id,
                    "game_title": item.game_title,
                    "quantity": item.quantity,
                    "price": item.price
                } for item in order.items
            ]
        }
        result.append(order_data)

    return jsonify(result), 200


@order_bp.route("/orders/<int:order_id>", methods=["GET"])
def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order_data = {
        "id": order.id,
        "customer_name": order.customer_name,
        "total_price": order.total_price,
        "created_at": order.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "items": [
            {
                "game_id": item.game_id,
                "game_title": item.game_title,
                "quantity": item.quantity,
                "price": item.price
            } for item in order.items
        ]
    }

    return jsonify(order_data), 200