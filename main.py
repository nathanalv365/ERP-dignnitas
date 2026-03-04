"""Aplicación inicial de ERP-dignnitas.

Esta versión es una base ejecutable en consola para validar el flujo MVP:
login -> alta producto -> movimiento de stock -> venta -> reporte.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List
import argparse


@dataclass
class User:
    username: str
    role: str


@dataclass
class Product:
    id: int
    name: str
    price: float
    active: bool = True


@dataclass
class StockMovement:
    product_id: int
    quantity: int
    movement_type: str  # entrada | salida
    created_at: datetime


@dataclass
class SaleItem:
    product_id: int
    quantity: int
    unit_price: float


@dataclass
class Sale:
    id: int
    items: List[SaleItem]
    total: float
    created_at: datetime


class ERPApp:
    def __init__(self) -> None:
        self.users: Dict[str, str] = {"admin": "admin", "operador": "operador"}
        self.products: Dict[int, Product] = {}
        self.stock: Dict[int, int] = {}
        self.stock_movements: List[StockMovement] = []
        self.sales: List[Sale] = []
        self._product_seq = 1
        self._sale_seq = 1

    def login(self, username: str) -> User:
        role = self.users.get(username)
        if not role:
            raise ValueError("Usuario no encontrado")
        return User(username=username, role=role)

    def create_product(self, name: str, price: float) -> Product:
        product = Product(id=self._product_seq, name=name, price=price)
        self.products[product.id] = product
        self.stock[product.id] = 0
        self._product_seq += 1
        return product

    def move_stock(self, product_id: int, quantity: int, movement_type: str) -> None:
        if product_id not in self.products:
            raise ValueError("Producto no existe")
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        current_stock = self.stock.get(product_id, 0)
        if movement_type == "entrada":
            self.stock[product_id] = current_stock + quantity
        elif movement_type == "salida":
            if current_stock < quantity:
                raise ValueError("Stock insuficiente")
            self.stock[product_id] = current_stock - quantity
        else:
            raise ValueError("Tipo de movimiento inválido")

        self.stock_movements.append(
            StockMovement(
                product_id=product_id,
                quantity=quantity,
                movement_type=movement_type,
                created_at=datetime.now(),
            )
        )

    def create_sale(self, items: List[tuple[int, int]]) -> Sale:
        sale_items: List[SaleItem] = []
        total = 0.0

        for product_id, quantity in items:
            product = self.products.get(product_id)
            if not product or not product.active:
                raise ValueError(f"Producto inválido: {product_id}")
            if self.stock.get(product_id, 0) < quantity:
                raise ValueError(f"Stock insuficiente para producto {product_id}")

            self.move_stock(product_id, quantity, "salida")
            sale_item = SaleItem(
                product_id=product_id,
                quantity=quantity,
                unit_price=product.price,
            )
            sale_items.append(sale_item)
            total += product.price * quantity

        sale = Sale(
            id=self._sale_seq,
            items=sale_items,
            total=round(total, 2),
            created_at=datetime.now(),
        )
        self._sale_seq += 1
        self.sales.append(sale)
        return sale

    def sales_report(self, start: datetime, end: datetime) -> Dict[str, float]:
        selected_sales = [s for s in self.sales if start <= s.created_at <= end]
        total_amount = round(sum(s.total for s in selected_sales), 2)
        return {
            "total_ventas": len(selected_sales),
            "monto_total": total_amount,
        }


def run_demo() -> None:
    app = ERPApp()

    user = app.login("admin")
    print(f"[OK] Login: {user.username} ({user.role})")

    product = app.create_product("Teclado", 25.5)
    print(f"[OK] Producto creado: {product}")

    app.move_stock(product.id, 10, "entrada")
    print(f"[OK] Stock actualizado. Stock actual producto {product.id}: {app.stock[product.id]}")

    sale = app.create_sale([(product.id, 2)])
    print(f"[OK] Venta registrada: id={sale.id}, total={sale.total}")

    start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    end = datetime.now()
    report = app.sales_report(start, end)
    print(f"[OK] Reporte ventas: {report}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aplicación inicial ERP-dignnitas")
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ejecuta un flujo completo de demostración del MVP",
    )
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        print("Usa --demo para ejecutar el flujo inicial del ERP.")
