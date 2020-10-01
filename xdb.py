#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, VARCHAR, Date
from sqlalchemy import select, func, Integer, Table, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from enum import Enum

metadata = MetaData()

Base = declarative_base()




    
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Sheet(Base):
    
    __tablename__ = 'sheet'

    id = Column(Integer, primary_key=True)
    request_date = Column(String())
    item_name = Column(String(255))
    description = Column(String(255))
    project = Column(String(255))
    manufacturing_order = Column(String(255))
    order_number = Column(String(255))
    pr = Column(String(255))    
    unit = Column(String(255))
    quantity_to_buy = Column(String(255))
    accepted = Column(String(255))
    remaining = Column(String(255))
    delivery_date = Column(Date())
    supplier = Column(String(255))
    delivery_order_number = Column(String(255))
    notes = Column(String(255))    
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {            
            'id': self.id,
            'request_date': self.request_date,            
            'item_name': self.item_name,
            'description': self.description,
            'project': self.project,
            'manufacturing_order': self.manufacturing_order,
            'order_number': self.order_number,
            'pr': self.pr,
            'unit': self.unit,
            'quantity_to_buy': self.quantity_to_buy,
            'accepted': self.accepted,
            'remaining': self.remaining,
            'delivery_date': self.delivery_date,
            'supplier': self.supplier,
            'delivery_order_number': self.delivery_order_number,
            'notes': self.notes

            
        }   

       
class History(Base):
    __tablename__ = 'history'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    pr = Column(String(20))
    order = Column(String(500))
    suplier = Column(String(500))
    date = Column(String(100))
    #menu_id = Column(Integer, ForeignKey('menu.id'))
    #menu = relationship(Menu)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'pr': self.pr,
            'order': self.order,
            'suplier': self.suplier,
            'date': self.date,
        }   




engine = create_engine('sqlite:///x.db')
Base.metadata.create_all(engine)
