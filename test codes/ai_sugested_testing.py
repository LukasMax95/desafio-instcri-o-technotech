from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional, Any
from threading import Lock
import uuid

# Entidades (substituir por models.Model no Django)
@dataclass
class User:
    id: str
    username: str
    email: str
    is_active: bool = True

@dataclass
class Product:
    id: str
    name: str
    price_cents: int

# Repositório em memória genérico
class InMemoryRepo:
    def __init__(self):
        self._store: Dict[str, Any] = {}
        self._lock = Lock()

    def create(self, obj: Any) -> Any:
        with self._lock:
            self._store[obj.id] = obj
        return obj

    def list(self) -> List[Any]:
        with self._lock:
            return list(self._store.values())

    def get(self, id: str) -> Optional[Any]:
        with self._lock:
            return self._store.get(id)

    def update(self, id: str, **kwargs) -> Optional[Any]:
        with self._lock:
            obj = self._store.get(id)
            if not obj:
                return None
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    setattr(obj, k, v)
            return obj

    def delete(self, id: str) -> bool:
        with self._lock:
            return self._store.pop(id, None) is not None

# Serializers simples (mapeamento dataclass <-> dict)
def to_dict(obj) -> dict:
    return asdict(obj)

def user_from_dict(data: dict) -> User:
    return User(
        id=data.get("id", str(uuid.uuid4())),
        username=data["username"],
        email=data["email"],
        is_active=data.get("is_active", True),
    )

def product_from_dict(data: dict) -> Product:
    return Product(
        id=data.get("id", str(uuid.uuid4())),
        name=data["name"],
        price_cents=int(data["price_cents"]),
    )

# Instâncias de repositório
user_repo = InMemoryRepo()
product_repo = InMemoryRepo()

# Simulação de endpoints (funções que a view do Django pode chamar)
def create_user(payload: dict) -> dict:
    user = user_from_dict(payload)
    user_repo.create(user)
    return to_dict(user)

def list_users() -> List[dict]:
    return [to_dict(u) for u in user_repo.list()]

def get_user(user_id: str) -> Optional[dict]:
    user = user_repo.get(user_id)
    return to_dict(user) if user else None

def update_user(user_id: str, payload: dict) -> Optional[dict]:
    updated = user_repo.update(user_id, **payload)
    return to_dict(updated) if updated else None

def delete_user(user_id: str) -> bool:
    return user_repo.delete(user_id)

def create_product(payload: dict) -> dict:
    product = product_from_dict(payload)
    product_repo.create(product)
    return to_dict(product)

# Walkthrough / demo rápido (executar como script para validar lógica)
def run_demo():
    print("=== Demo: criação de usuários e produtos (in-memory) ===")
    u1 = create_user({"username": "alice", "email": "alice@example.com"})
    u2 = create_user({"username": "bob", "email": "bob@example.com"})
    print("Usuários:", list_users())
    print("Atualizando bob para inativo...")
    update_user(u2["id"], {"is_active": False})
    print("Busca bob:", get_user(u2["id"]))
    print("Criando produto de exemplo...")
    p = create_product({"name": "Caneca", "price_cents": 1999})
    print("Produto criado:", p)
    print("Removendo alice:", delete_user(u1["id"]))
    print("Usuários finais:", list_users())
    print("=== Fim demo ===")

# Pequenos cenários de teste (pode portar para pytest)
def scenario_create_and_update_user():
    payload = {"username": "carol", "email": "carol@example.com"}
    u = create_user(payload)
    assert u["username"] == "carol"
    assert get_user(u["id"]) is not None
    update_user(u["id"], {"email": "carol@newdomain.org"})
    assert get_user(u["id"])["email"] == "carol@newdomain.org"
    delete_user(u["id"])
    assert get_user(u["id"]) is None

def run_all_scenarios():
    scenario_create_and_update_user()
    print("Todos os cenários rodaram com sucesso.")

if __name__ == "__main__":
    run_demo()
    run_all_scenarios()