#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from typing import Optional
import re
 
 
class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name:str, price:float) -> None:
        if(isinstance(name, str) and isinstance(price,float)):
            if not re.fullmatch('^[a-zA-Z]+\\d+$', name):
                raise ValueError("Product name should have atleast 1 character and one digit in the right order")
            else:
                self.name=name
                self.price=price
        pass
    def __eq__(self, other):
        if isinstance(other, Product):
            if self.name == other.name:
                return True
            else:
                return False
        else:
            print('Porównywane obiekty nie należą do tej samej klasy')
            return None
 
    def __hash__(self):
        return hash((self.name, self.price))
 
 
class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass
 
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
 
class ListServer:
    pass
 
 
class MapServer:
    pass
 
 
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
    
try:
    produkt1 = Product("x0129", 250.00)
    produkt2 = Product("BB12", 300.50)
    produkt3 = Product("abcd1", 150.75)
except ValueError as e:
    print(f"Błąd: {e}")