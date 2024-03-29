#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from typing import Optional, List, Dict
import re
from abc import ABC, abstractmethod

 
 
class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name:str, price:float) -> None:
        if(isinstance(name, str) and isinstance(price,(float,int))):
            if not re.fullmatch('^[a-zA-Z]+\\d+$', name):
                raise ValueError("Product name should have atleast 1 character and one digit in the right order")
            else:
                self.name=name
                self.price=price
        else:
            raise ValueError('Wrong data type')
    def __eq__(self, other):
        if isinstance(other, Product):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            print('Compared object are not same class')
            return None
 
    def __hash__(self):
        return hash((self.name, self.price))
 
 
class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass
 
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
class Server(ABC):
    n_max_returned_entries:int =5
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def get_entries(self, n_letters)->int:
        prod_name_ex= '^[a-zA-Z]{{{n}}}\\d{{2,3}}$'.format(n=n_letters)
        prod_found= [prod for prod in self.get_all_products(n_letters)if re.fullmatch(prod_name_ex, prod.name)]
        if len(prod_found)> Server.n_max_returned_entries:
            raise TooManyProductsFoundError
        else:
            return prod_found
    @abstractmethod
    def get_all_products(self, n_letters:int )->List[Product]:
        raise NotImplementedError
    
    
    
class ListServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: List[Product] = products 
    def get_all_products(self, n_letters:int) -> List[Product]:
        return self.products

 
 
class MapServer(Server):
    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products: Dict[str, Product] = {p.name: p for p in products}
    def get_all_products(self, n_letters:int) -> List[Product]:
        return list(self.products.values())

 
 
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__ (self, server: Server )->None:
        self.server=server
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            products = self.server.get_all_products(n_letters)
            total_price = sum([prod.price for prod in products])
            return total_price
        except TooManyProductsFoundError:
            print("Too many products found. Please refine your search.")
            return None
    
try:
    produkt1 = Product("x0129", 250.00)
    produkt2 = Product("BB12", 300.50)
    produkt3 = Product("abcd1", 150.75)
except ValueError as e:
    print(f"Błąd: {e}")


    
print('plik servers.py został wykonany')